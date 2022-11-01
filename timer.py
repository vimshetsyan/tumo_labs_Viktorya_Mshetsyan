import time


def countdown(count):
    while count:   # it is to say while 'count' > 0 or is True
        minutes, seconds = divmod(count, 60)  # Divmod display the quotient and the remainder of 'count' divided by 60:
        timer = '{:02d}:{:02d}'.format(minutes, seconds)  # Formatting timer to be visually more understandable
        print(timer)  # printing remaining time
        time.sleep(1)  # it waits a second because we need to countdown every second
        count -= 1  # we need to subtract 1 from the initial second's /
        # value because we just coded the program to sleep 1 second

    print('Your time is up') 


count_down = input("Enter the time in seconds: ")  # inputting value as seconds

countdown(int(count_down))  # assigning value of 'count_down' to 'countdown' function
