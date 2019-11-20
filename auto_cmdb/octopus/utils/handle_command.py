import subprocess
from auto_cmdb.settings import INVENT_PATH as invent_path
class HandleCommand:
    ret_msg = {
        "status": False,
        "msg": '命令格式错误'
    }
    def __init__(self, command,inven):
        self.command = command
        self.invent_path = invent_path
        self.inven = inven
        self.command_tpl = '{} -i {} -{}'
        self.rewrite()

    def rewrite(self):
        tpl_group = "[{}]\n"
        tpl_host = '{}\n'
        content_list = []
        for g in self.inven:
           content_list.append(tpl_group.format(g.group))
           for h in g.server.all():
               content_list.append(tpl_host.format(h.manager_ip))
        with open(self.invent_path, 'w', encoding='utf-8') as f:
            f.writelines(content_list)

    def checked(self):
        """检查命令格式"""
        ansib, arg = self.command.split('-', 1)
        self.command = self.command_tpl.format(ansib,self.invent_path, arg)
        return self.command

    def exec_command(self):
        comm = self.checked()
        if comm:
            status, r = subprocess.getstatusoutput(comm)
            if status == 0:
                self.ret_msg['status'] = True
            self.ret_msg['msg'] = r
            return self.ret_msg
        else:
            return False
