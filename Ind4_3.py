import time

def funtime():
    for o in range(5):
        current_time = time.strftime("%H:%M:%S")
        print("Текущее время:", current_time)
        time.sleep(1)


if __name__ == '__main__':
    funtime()
