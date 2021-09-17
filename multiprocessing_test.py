import os
from multiprocessing import Process, Lock, Pool, Queue
from time import sleep


def counter(num: int):
    summ: int = 0
    for i in range(num):
        summ += i

    print(os.getpid(), summ)

def summer(nums: [int], queue: Queue):
    for num in nums:
        queue.put(num)
        sleep(1)


def getter_queue(queue: Queue):
    while True:
        value = queue.get()
        print(value)
        sleep(1)

        if value == 100000000:
            break


if __name__ == '__main__':
    numders: [int] = [500000000, 400000000, 300000000, 200000000, 100000000, 100000000, 100000000]
    procs: [Process] = []
    queue: Queue = Queue()



    # for num in numders:
    #     _proc: Process = Process(target=counter, args=(num,))
    #     procs.append(_proc)
    #     _proc.start()
    #
    # for _proc in procs:
    #     _proc.join()



    # pool: Pool = Pool(processes=7)
    # pool.map(counter, numders)



    process_one = Process(target=summer, args=(numders, queue))
    process_two = Process(target=getter_queue, args=(queue,))

    process_one.start()
    process_two.start()

    queue.close()
    queue.join_thread()

    #process_one.join()
    #process_two.join()
    print('1111111111111')