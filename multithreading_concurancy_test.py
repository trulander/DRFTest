from multiprocessing import Lock, Process
from threading import Lock, Thread
from time import sleep
from unittest import mock

lock = Lock()
lock = mock.MagicMock()
g = 0


def add_one():
    global g
    lock.acquire()
    sleep(1)
    g += 1
    lock.release()

    print('1')


def add_two():
    global g
    lock.acquire()
    a = g + 1
    sleep(1)
    g = a
    lock.release()

    print('2')



def add_three():
    global g
    lock.acquire()
    a = g + 1
    sleep(1)
    g = a
    print('3')
    lock.release()

def add_four():
    global g
    lock.acquire()
    a = g + 1
    sleep(1)
    g = a

    print('4')
    lock.release()

def add_five():
    global g
    lock.acquire()
    sleep(2)
    g += 1

    print('5')
    lock.release()




if __name__ == '__main__':
    threads = []
    for func in [add_one, add_two, add_three, add_four, add_five]:
        #threads.append(Process(target=func))
        threads.append(Thread(target=func))
        threads[-1].start()

    for thread in threads:
        thread.join()

    print('----',g,'----')