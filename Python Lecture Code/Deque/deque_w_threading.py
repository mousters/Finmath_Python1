import threading
from collections import deque

channel=deque()
lock_queu = threading.Lock()
id=0
def send_item(item):
    lock_queu.acquire()
    channel.append(item)
    lock_queu.release()

def receive_item():
    lock_queu.acquire()
    a=channel.popleft()
    lock_queu.release()
    print('receive',a)


def producer():
    global id
    producer_id='Producer: '+str(id)
    for i in range(10):
        print(producer_id,'send')
        send_item((producer_id,i))
    id+=1

def consumer():
    while True:
        try:
            receive_item()
        except:
            pass

if __name__=='__main__':
    t1=threading.Thread(target=producer)
    t2=threading.Thread(target=producer)
    t3=threading.Thread(target=producer)
    t4=threading.Thread(target=producer)

    t5=threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()