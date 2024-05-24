import time
from pygame import mixer

def pomodoro_timer():
    work_time = 25 * 60  
    short_break = 5 * 60  
    long_break = 15 * 60  

    cycles = 0  

    while True:
        print("Start working! Pomodoro timer started.")
        for i in range(work_time, 0, -1):
            mins = i // 60
            secs = i % 60
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)

        cycles += 1

        
        if cycles % 4 == 0:
            print("Time for a long break!")
            mixer.init()
            mixer.music.load('/Users/lmh/Downloads/Clock-chimes-sound/ting-tong.mp3')
            mixer.music.play()
            time.sleep(4)
            mixer.music.stop()
            for j in range(long_break, 0, -1):
                mins = j // 60
                secs = j % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end='\r')
                time.sleep(1)

        else:
            print("Time for a short break!")
            mixer.init()
            mixer.music.load('/Users/lmh/Downloads/Clock-chimes-sound/ting-tong.mp3')
            mixer.music.play()
            time.sleep(4)
            mixer.music.stop()
            for k in range(short_break, 0, -1):
                mins = k // 60
                secs = k % 60
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end='\r')
                time.sleep(1)
                

        exit = input("Continue? (if yes press y else press n): ")
        if exit.lower() != 'y':
           print("Sayonara!")
           break


pomodoro_timer()
