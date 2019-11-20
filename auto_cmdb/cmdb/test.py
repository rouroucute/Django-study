import subprocess

status,a = subprocess.getstatusoutput("sh /root/copyssh.sh  22  root 172.17.0.2 123456  &&  echo $?")

print(status)
print(a)
# if status == 0:
#     print(status)
# else:
#     print("不成功")