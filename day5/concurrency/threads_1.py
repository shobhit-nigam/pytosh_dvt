import time

def taskA():
    for i in range(6, 0, -1):
        print("task A will exit in", i, "seconds")
        time.sleep(1)

def taskB():
    for i in range(9, 0, -1):
        print("task B will exit in", i, "seconds")
        time.sleep(1)        


taskA()
taskB()
for i in range(3, 0, -1):
    print("task Main will exit in", i, "seconds")
    time.sleep(1)

