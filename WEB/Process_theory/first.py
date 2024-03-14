from multiprocessing import Process
import sys
from time import sleep


def example_work(params):
    print(params)
    sleep(10)
    sys.exit(0)


if __name__=='__main__':
    proces = []
    for i in range(5):
        pr = Process(target=example_work, args=(f'Count process - {i}',))
        pr.start()
        proces.append(pr)

    [print(pr.exitcode, end=' ') for pr in proces]
    print('')
    [pr.join() for pr in proces]
    [print(pr.exitcode, end=' ') for pr in proces]