'''threading examples'''
import threading
import sys
import time
balance_lock=threading.Lock()
#both clients deposit 1 USD at a time, the var is how much they deposit
def client(action):
    global balance
    for i in range(30):
        try:
            balance_lock.acquire()
            balance+=action
            time.sleep(1)
            if(action>0):
                print('Client 1 deposit 1 and now the balance is ',balance)
            else:
                print('Client 1 withdraw 1 and now the balance is ', balance)
        finally:
            balance_lock.release()
if __name__=='__main__':
    balance = 0
    amt=30
    print('initial balance: ',balance)
    t1=threading.Thread(target=client,args=(1,))
    t2 = threading.Thread(target=client,args=(-1,))
    t1.start();t2.start()
    t1.join();t2.join()
    print('final balance: ',balance)