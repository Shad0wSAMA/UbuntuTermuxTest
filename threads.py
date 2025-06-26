import threading
import time

def worker(num):
    print(f"Thread {num} starting")
    time.sleep(2)
    print(f"Thread {num} finished")

for i in range(4):
    t = threading.Thread(target=worker, args=(i,))
    t.start()