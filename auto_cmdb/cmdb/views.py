# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializers import AssetSerializer,ServerSerializer,MemorySerializer,DiskSerializer,TreeNodeSerializer
# from .page import StandardResultsSetPagination
# from .models import Asset,Server,Memory,Disk,TreeNode
# from django.views.generic import DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy

# class AssetViewSet(viewsets.ReadOnlyModelViewSet):  #继承只读的视图
#     queryset = Asset.objects.all()
#     serializer_class = AssetSerializer
#     pagination_class = StandardResultsSetPagination

# class ServerViewSet(viewsets.ReadOnlyModelViewSet):  #继承只读的视图
#     queryset = Server.objects.all()
#     serializer_class = ServerSerializer
#     pagination_class = StandardResultsSetPagination

# class MemoryViewSet(viewsets.ReadOnlyModelViewSet):  #继承只读的视图
#     queryset = Memory.objects.all()
#     serializer_class = MemorySerializer
#     pagination_class = StandardResultsSetPagination

# class DiskViewSet(viewsets.ReadOnlyModelViewSet):  #继承只读的视图
#     queryset = Disk.objects.all()
#     serializer_class = DiskSerializer
#     pagination_class = StandardResultsSetPagination

# class AssetsDetailView(LoginRequiredMixin,DetailView):
#     # login_url = reverse_lazy("users:login")
#     model = Asset
#     context_object_name = "asset"
#     template_name = "cmdb/assets-detail.html"
# # def assets_detail(request,id):
# #       assets = Asset.objects.get(id=id)
# #       console.log('1111')
# #       context  = { 'assets' : assets }
# #       return render(request, 'cmdb/assets-detail.html', context)

# ###组件测试
# class TreeNodeViewSet(viewsets.ModelViewSet):
#     queryset = TreeNode.objects.filter(node_upstream=None)
#     serializer_class = TreeNodeSerializer
      




###cbv_view
from cmdb.models import Server, Memory,Disk,Asset
from django.shortcuts import render, HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView



# class ServerListView(View):
#     def get(self, request):
#         qst_servers = Server.objects.all()
#         return render(request, 'cmdb/server_list.html', {
#             "servers": qst_servers
#         })


class AssetListView(View):
      def get(set,request):
            msg_assets = Asset.objects.all()
            return render(request,'cmdb/assets-list.html',{
                "assets":msg_assets
            })


class MemoryListView(View):
    def get(self,request):
        qst_memorys = Memory.objects.all()
        return render(request,'cmdb/mem-list.html',{
            "memorys" : qst_memorys
        })


class DiskListView(View):
    def get(self,request):
        qst_disks= Disk.objects.all()
        return render(request,'cmdb/disk-list.html',{
          "disks" :qst_disks
        })


class ServerDetailView(DetailView):
    # login_url = reverse_lazy("users:login")
    model = Server
    context_object_name = "asset"
    template_name = "cmdb/assetsdetail.html"



class AssetsDetailView(DetailView):
    model = Asset
    context_object_name = "asset"

    def get_template_names(self):
        names = []
        type_asset = self.object.get_device_type_id_display()
        if type_asset == "服务器":
            names.insert(0, 'cmdb/assetsdetail.html')
        # elif type_asset == "路由器":
        #     names.insert(0, 'cmdb/network-detail.html')

        return names

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asset = context['asset']
        type_map = {
            '服务器': "server"
        }
        asset_type = asset.get_device_type_id_display()
        type_obj = type_map.get(asset_type)
        context[type_obj] = getattr(asset, type_obj)
        server = context[type_obj]
        context["memory"] = getattr(server, "memorys").all()
        context["disk"] = getattr(server, "disks").all()
        # print(context)
        return context


class ServerListView(ListView):
    template_name = 'cmdb/server_list.html'
    context_object_name = 'servers'

    def get_queryset(self):
        node_id = self.request.GET.get("node_id")
        if node_id:
            queryset = Server.objects.filter(asset__node__id=node_id)
        else:
            queryset = Server.objects.all()
        return queryset

