import time
import threading
# race around condition

ga = 0
la = threading.Lock()

def taskA():
    global ga
    global la
    print("A trying to take the lock\n")
    la.acquire()
    print("A gets the lock\n")
    ga = ga+1
    print(f"starting task {ga}\n") 
    for i in range(100000000):
        i=i+1
    print(f"finished task {ga}\n")
    print("A will release the lock\n")
    la.release()

def taskB():
    global ga
    global la
    print("B trying to take the lock\n")
    if la.acquire(timeout=3):
        
        print("B gets the lock\n")
        ga = ga+1
        print(f"starting task {ga}\n") 
        for i in range(1):
            i=i+1
        print(f"finished task {ga}\n")
        print("B will release the lock\n")
        la.release()
    else:
        print("A is taking too long, B will come back later")


ta = threading.Thread(target=taskA)
tb = threading.Thread(target=taskB)

ta.start()
tb.start()

ta.join()
tb.join()
print("last line of code")

