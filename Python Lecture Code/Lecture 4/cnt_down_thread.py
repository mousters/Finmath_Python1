import threading
import time
def countown(timeout):
    for i in range(0,timeout):
        print(i)
        time.sleep(1)
    print('end of the thread with the timeout %d' % (timeout))
if __name__ == '__main__':
    t1=threading.Thread(target=countown,args=(6,))
    t2 = threading.Thread(target=countown, args=(3,))
    t1.start()
    t2.start()
    print('The two program starts')
    t1.join()
    t2.join()
    print('The two program joins')
    print('END OF MY CODE')
