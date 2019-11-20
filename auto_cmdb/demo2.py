from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


def job(i):
    print('hello world',i)
    time.sleep(10)


ec = ThreadPoolExecutor