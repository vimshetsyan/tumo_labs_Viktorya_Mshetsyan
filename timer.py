import time


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        hours = 0
        if mins >= 60:
            hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(timer)

    print("Time's up!")


input_time = input("Enter the time in format hh:mm:ss: ")
hours, minutes, seconds = map(int, input_time.split(':'))
total_seconds = hours*3600 + minutes*60 + seconds
countdown(total_seconds)
