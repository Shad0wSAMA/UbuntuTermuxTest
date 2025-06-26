import threading
import time

def worker(num):
    for(j in range(0,100)):
        print(f"Thread {num} starting", j)
        time.sleep(1)
        print(f"Thread {num} finished", j)
        time.sleep(1)

for i in range(8):
    t = threading.Thread(target=worker, args=(i,))
    t.start()