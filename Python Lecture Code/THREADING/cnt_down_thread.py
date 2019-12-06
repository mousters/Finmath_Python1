import threading
import time
class countdown_thread(threading.Thread):
    def __init__(self,count):
        threading.Thread.__init__(self)
        self.count=count
    def run(self):
        original_count=self.count
        while self.count>0:
            print('Counting down, ',self.count)
            self.count-=1
            time.sleep(1)

        print('end of the thread with the timeout %d' % (original_count))
        return
def countown(timeout):
    for i in range(0,timeout):
        print(i)
        time.sleep(1)
    print('end of the thread with the timeout %d' % (timeout))
if __name__ == '__main__':
    t1=threading.Thread(target=countown,args=(6,))
    t2 = threading.Thread(target=countown, args=(3,))
    print('The two COUNTING program starts')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('The two program joins')
    print('END OF COUNTING CODE')
    print()
    print('The two COUNT_DOWN program starts')
    tc1=countdown_thread(6)
    tc2=countdown_thread(3)
    tc1.start()
    tc2.start()
    tc1.join()
    tc2.join()
    print('END OF COUNT_DOWN CODE')



'''
The two COUNTING program starts
0
0
1
1
2
2
3
end of the thread with the timeout 3
4
5
end of the thread with the timeout 6
The two program joins
END OF COUNTING CODE

The two COUNT_DOWN program starts
Counting down,  6
Counting down,  3
Counting down,  2
Counting down,  5
Counting down,  4
Counting down,  1
Counting down,  3
end of the thread with the timeout 3
Counting down,  2
Counting down,  1
end of the thread with the timeout 6
END OF COUNT_DOWN CODE

'''