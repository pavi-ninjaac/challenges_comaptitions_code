import threading
import time
global x 
def incr():
    global x
    x+=1
def t_call(lock):
    lock.acquire()
    for i in range(20):
        print('increamenting thre',threading.current_thread().name)
        
        incr()
        
        #time.sleep(1)
        print("the value incremented x:",x,'by',threading.current_thread().name)
    lock.release()

def main():
    global x
    x=0
    lock = threading.Lock()
    t1 = threading.Thread(target = t_call,  args=(lock,))
    t2 = threading.Thread(target = t_call ,  args=(lock,))

    print("t1 started")
    t1.start()
    print('t2 started')
    t2.start()
    t1.join()
    t2.join()
    print('done')
if __name__ == "__main__":
    main()