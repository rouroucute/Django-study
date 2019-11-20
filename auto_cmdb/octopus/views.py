import subprocess,ansible,pexpect


from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .utils.handle_command import HandleCommand
from .tasks import exec_commands,add,run_shell
from celery.result import AsyncResult
# Create your views here.

from cmdb.models import Server,InventoryPool

class ConnectionView(View):
    def get(self,request):
        conninfo = Server.objects.filter(connection__user__isnull=False)
        return render(request,"octopus/connection.html",{"connection": conninfo})

    def post(self,requset):
        server_id = requset.POST.get("server_id")
        server = Server.objects.filter(id=server_id).first()
        user = server.connection.user
        port = server.connection.port
        pwd = server.connection.password
        ip = server.manager_ip
        status,result = subprocess.getstatusoutput("sh /root/copyssh.sh {} {} {} {}".format(port,user,ip,pwd))
        if status == 0 and "logging" in result:
            server.connection.authed = True
            server.connection.save()
            return JsonResponse({"status":True})
        else :
            return JsonResponse({"status":False})



class ExecCommandView(View):
    def get(self,request):
        inven = InventoryPool.objects.all()
        return render(request,"octopus/runshell.html",{"inven": inven})

    def post(self,request):
        command = request.POST.get('command')
        if command.startswith("ansible "):    
            ret = exec_commands.delay(command)
            return JsonResponse({'task_id': ret.id})
        else:
            return JsonResponse({'task_id':"命令有误"})


class ExecCommandGetTaskView(View):
    def get(self,request):
        task_id = request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)


class AsyncDemoView(View):
    def get(self,request):
        return render(request,"octopus/async-demo.html")
    def post(self,request):
        num = request.POST.get("num")
        num = int(num)
        task = add.delay(num)
        return JsonResponse({"task_id":task.id})


class AsyncDemoGetTaskView(View):
    def get(self,request):
        task_id = request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)


class DonamicGetTaskView(View):
    def get(self,request):
        inven = InventoryPool.objects.all()
        return render(request,"octopus/dona-shell.html",{"inven": inven})
    def post(self,request):
        group_name = request.POST.get("group_name")
        host_ip = request.POST.get("host_ip")
        varsdic = request.POST.get("varsdic")
        modelname = request.POST.get("modelname")
        shellname = request.POST.get("shellname")
        ret = run_shell.delay(group_name,host_ip,varsdic,modelname,shellname)
        return JsonResponse({'task_id': ret.id})



class DonamicGetResultView(View):
    def get(self,request):
        task_id = request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)