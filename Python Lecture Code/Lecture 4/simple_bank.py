# threading examples
import threading
import sys
import time
balance_lock=threading.Lock()
sema_lock=threading.Semaphore(2)

#both clients deposit 1 USD at a time, the var is how much they deposit

def client(action,amt):
    global balance
    for i in range(amt):
        try:
            #MUTEX LOCK
            balance_lock.acquire()
            balance+=action
            time.sleep(0.3)
            if(action>0):
                print('Client 1 deposit 1 and now the balance is ',balance)
            else:
                print('Client 1 withdraw 1 and now the balance is ', balance)
        #FINALLY TO ENSURE THAT NO MATTER WHAT HAPPENED TO PREVIOUS
        #THE LOCK FINALLY RELEASED FOR OTHER PROGRAMS TO RUN
        finally:
            #ONLY ONE THREAD CAN RUN THIS PART (ACQUIRER ... RELEASE)
            balance_lock.release()
def observer(x):
    print('observer',x)
    global balance
    sema_lock.acquire()
    try:
        for i in range(5):
            print('observer ',str(x),str(balance))
            time.sleep(x)
    finally:
        sema_lock.release()

# DEADLOCK: RESULT FROM THE FOLLOWING CODE:
#     x_lock = threading.Lock()
#     y_lock = threading.Lock()


if __name__=='__main__':
    balance = 0
    amt=30
    print('initial balance: ',balance)
    t1=threading.Thread(target=client,args=(1,10))
    t2 = threading.Thread(target=client,args=(-1,10))
    t3=threading.Thread(target=observer,kwargs={'x':1})
    t4 = threading.Thread(target=observer, kwargs={'x':2})
    t5 = threading.Thread(target=observer,kwargs={'x':3})
    t1.start();t2.start();t3.start();t4.start();t5.start()
    t1.join();t2.join();t3.join();t4.join();t5.join();
    #•• Thread scheduling is non deterministic
    #•• Thus, access to any kind of shared data is also non deterministic (remember the Chicken joke)
    #••Note, t2 will join at some random time point (start withdrawing) and each run has different results
    #•• The corruption of shared data due to thread scheduling is often known as a “race condition”.
    #To fix that, we need to use thread synchronization
    print('final balance: ',balance)
'''
OUTCOME
initial balance:  0
observer 1
observer  1 1
observer 2
observer  2 1
observer 3
Client 1 deposit 1 and now the balance is  1
Client 1 deposit 1 and now the balance is  2
Client 1 deposit 1 and now the balance is  3
observer  1 2
Client 1 withdraw 1 and now the balance is  2
Client 1 withdraw 1 and now the balance is  1
Client 1 withdraw 1 and now the balance is  0
observer  2 -1
observer  1 -1
Client 1 withdraw 1 and now the balance is  -1
Client 1 withdraw 1 and now the balance is  -2
Client 1 withdraw 1 and now the balance is  -3
Client 1 withdraw 1 and now the balance is  -4
observer  1 -3
Client 1 deposit 1 and now the balance is  -3
Client 1 deposit 1 and now the balance is  -2
Client 1 deposit 1 and now the balance is  -1
observer  2 -2
observer  1 -2
Client 1 withdraw 1 and now the balance is  -2
Client 1 withdraw 1 and now the balance is  -3
Client 1 withdraw 1 and now the balance is  -4
observer  3 -3
Client 1 deposit 1 and now the balance is  -3
Client 1 deposit 1 and now the balance is  -2
Client 1 deposit 1 and now the balance is  -1
observer  2 0
Client 1 deposit 1 and now the balance is  0
observer  2 0
observer  3 0
observer  3 0
observer  3 0
observer  3 0
final balance:  0
'''