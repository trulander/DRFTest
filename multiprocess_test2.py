from multiprocessing import Process
from time import time, sleep


def loop():
    while True:
        sleep(3)
        print('passed 3 sec')

if __name__ == '__main__':
    proc = Process(target=loop())