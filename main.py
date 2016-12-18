# Author: Pavlo Dyban
# Repo: https://github.com/pdyban/
# Date: 2016-Dec-18

from microbit import *

SECOND = 1000  # milliseconds
MINUTE = 60 * SECOND  # milliseconds

STAGES = [Image('00000:00000:00100:00000:00000'),
        Image('00000:00000:00200:00000:00000'),
        Image('00000:00000:00300:00000:00000'),
        Image('00000:00000:00400:00000:00000'),
        Image('00000:00000:00500:00000:00000'),
        Image('00000:00000:00600:00000:00000'),
        Image('00000:00000:00700:00000:00000'),
        Image('00000:00000:00800:00000:00000'),
        Image('00000:00000:00900:00000:00000'),
        Image('00000:01110:01910:01110:00000'),
        Image('00000:02220:02920:02220:00000'),
        Image('00000:03330:03930:03330:00000'),
        Image('00000:04440:04940:04440:00000'),
        Image('00000:05550:05950:05550:00000'),
        Image('00000:06660:06960:06660:00000'),
        Image('00000:07770:07970:07770:00000'),
        Image('00000:08880:08980:08880:00000'),
        Image('00000:09990:09990:09990:00000'),
        Image('11111:19991:19991:19991:11111'),
        Image('22222:29992:29992:29992:22222'),
        Image('33333:39993:39993:39993:33333'),
        Image('44444:49994:49994:49994:44444'),
        Image('55555:59995:59995:59995:55555'),
        Image('66666:69996:69996:69996:66666'),
        Image('77777:79997:79997:79997:77777'),
        Image('88888:89998:89998:89998:88888'),
        Image('99999:99999:99999:99999:99999'),]

TOTAL_TIME = 25*MINUTE  # total time to measure, in milliseconds
INCREMENT = TOTAL_TIME/len(STAGES)  # time between stages

pause = False
display.show(STAGES, delay=10)
display.show(reversed(STAGES), delay=10)
time_elapsed = 0
pomodoros = 0
finished = False
reversed_order = False
while True:
    if not pause:
        if time_elapsed > TOTAL_TIME:
            if not finished:
                finished = True
                pomodoros += 1  # count number of achieved pomodoros
            
            display.show(STAGES, delay=10)
            
            if reversed_order:  # split in order to allow interaction during the animation
                display.show(reversed(STAGES), delay=10)
            else:
                reversed_order = not reversed_order
            
        else:
            for index in range(len(STAGES)):
                if time_elapsed < INCREMENT*(index+1): # replace incr w 55555
                    display.show(STAGES[index])
                    break
    
    sleep(100)
    if not pause:
        time_elapsed += 100
        
    if button_a.is_pressed():  # reset button
        display.show(STAGES, delay=10)
        display.show(reversed(STAGES), delay=10)
        pause = False
        finished = False
        reversed_order = False
        time_elapsed = 0
        
    if button_b.is_pressed():  # pause button
        pause = not pause
        if pause:
            display.show(Image.SAD)
        sleep(200)

    if accelerometer.was_gesture('shake'):
        display.scroll(str(pomodoros))
