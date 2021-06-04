import time
import threading
# race around condition

ga = 0

def taskA():
    global ga
    ga = ga+1
    print(f"starting task {ga}\n") 
    for i in range(1):
        i=i+1
    print(f"finished task {ga}\n")

def taskB():
    global ga
    ga = ga+1
    print(f"starting task {ga}\n") 
    for i in range(1):
        i=i+1
    print(f"finished task {ga}\n")      


ta = threading.Thread(target=taskA)
tb = threading.Thread(target=taskB)

ta.start()
tb.start()

ta.join()
tb.join()
print("last line of code")

