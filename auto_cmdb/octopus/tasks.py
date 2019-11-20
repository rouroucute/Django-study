from __future__ import absolute_import, unicode_literals
from celery import shared_task


from cmdb.models import InventoryPool
from .utils.handle_command import HandleCommand
from .utils import classansibleapi


@shared_task
def exec_commands(command):
    inven = InventoryPool.objects.all()
    handler = HandleCommand(command, inven)
    ret = handler.exec_command()
    return ret


@shared_task
def add(n):
    import time
    time.sleep(10)
    return n + 10


@shared_task
def run_shell(group_name,host_ip,varsdic,modelname,shellname):
    results = classansibleapi.ansible_run(group_name,host_ip,varsdic,modelname,shellname)
    
    return results
