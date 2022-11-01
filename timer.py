import time


def countdown(count):
    while count:
        minutes, seconds = divmod(count, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer)
        time.sleep(1)
        count -= 1

    print('Your time is up')


count_down = input("Enter the time in seconds: ")

countdown(int(count_down))
