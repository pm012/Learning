from threading import Thread

def th_function(param):
    print(param)


if __name__  == '__main__':
    for i in range(5):
        th = Thread(target=th_function, args=(i,))
        th.start()