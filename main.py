import pyautogui as pt
from time import sleep
from datetime import datetime as d
import pyperclip
import random
import os





## PROGRAM LOCATES BUTTONS NEAR TO RECENT USER MSG
position1 = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]





## GETS MSG
def get_message():
    global x, y

    position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x+80, y-60, duration=.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()

    whatsapp_msg = pyperclip.paste()
    print("Message received:", whatsapp_msg)

    return whatsapp_msg





## SEND REPLY TO MSG
def post_response(msg):
    global x, y
    position = pt.locateOnScreen("smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]

    pt.moveTo(x+170, y+40, duration=.05)
    pt.click()
    pt.typewrite(msg, interval=.001)         ## write
    pt.typewrite("\n", interval=.001)        ## send (program presses enter)





## PROCESSES RESPONSE
def process_response(msg):
    num = random.randrange(5)
    # if "?" in str(msg).lower():
    #     return "Don't ask me any questions"
    if num == 0:
        return "_Nadra is not responding to any further messages. You're not up to her standards :/_"
    elif num == 1:
        return "_Nadra is not responding to any further messages. You kinda smell._"
    elif num == 2:
        return "_Nadra is not responding to any further messages. She has potentially better candidates waiting in line._"
    elif num == 3:
        return "_Nadra is not responding to any further messages. In other words, let's stop talking :D_"
    elif num == 4:
        return "_Nadra is not responding to any further messages. Straight up, you suck._"




## CHECK FOR NEW MSGS
def check_for_new_messages():
    # pt.moveTo(x+50, y-45, duration=.05)      # msgs
    # pt.moveTo(x+169, y-52, duration=.05)     # stickers

    while True:
        ## RESET
        pt.moveTo(x-100, y+50, duration=.05)
        pt.click()
        ## CONTINUOUSLY CHECKS FOR GREEN DOT & NEW MSGS
        try:
            position = pt.locateOnScreen("green_dot.png", confidence=.7)
            
            if position is not None:
                date = d.now()
                print(f"New message from user opened. {date.strftime('%H:%M:%S')}")
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new messages from new users.")

        ## CHECK IF THERE IS A MSG FROM OTHER USER
        if pt.pixelMatchesColor(int(x+50), int(y-45), (38,45,49), tolerance=10) or pt.pixelMatchesColor(int(x+169), int(y-52), (38,45,49), tolerance=10):
            print('New message from user located.')
            processed_message = process_response(get_message())
            post_response(processed_message)
            print("Response sent.")
        else:
            date = d.now()
            print(f'No new messages from user yet. {date.strftime("%I:%M:%S %p")}')
        sleep(5)





## MAIN
def main():
    os.system('pause')
    check_for_new_messages()
            

if __name__ == '__main__':
    main()