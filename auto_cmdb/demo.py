import multiprocessing
import threading
import time


def job(i):
    print('hello world',i)
    time.sleep(10)

task = []
for i in range(10):
    t1 = threading.Thread(target=job,args=(i,))
    # t1 = multiprocessing.process(target=job,args=(i,))
    task.append(t1)

for i in  task:
    i.start()


for i in task:
    i.join()

