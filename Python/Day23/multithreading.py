#multi threading

import time
import threading

def number():
    for i in range(1,11):
        print("Value :",i)
        time.sleep(2)
def square():
    for i in range(1,11):
        time.sleep(2.5)
        print("Square Value of",i,"is :",i*i)
        

th1=threading.Thread(target=number)
th2=threading.Thread(target=square)

th1.start()
th2.start()
