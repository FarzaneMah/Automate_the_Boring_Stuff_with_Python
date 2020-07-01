"""When you run this program, there will be a five-second delay ❶ for you to move the mouse
cursor over the drawing program’s window with the Pencil or Brush tool selected.
Then spiralDraw.py will take control of the mouse and click to put the drawing program in focus
❷. A window is in focus when it has an active blinking cursor,
and the actions you take—like typing or, in this case,
dragging the mouse—will affect that window. Once the drawing program is in focus,
spiralDraw.py draws a square spiral pattern like the one in """


import pyautogui, time

time.sleep(5)
pyautogui.click() #click to put drawingn
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance,0, duration=0.1) #move right
    distance = distance - 5
    print(0,distance)
    pyautogui.dragRel(0,distance,duration=0.1) #move down
    print(-distance,0)
    pyautogui.dragRel(-distance,0, duration=0.1) #move left
    distance = distance - 5
    print(0,-distance)
    pyautogui.dragRel(0,-distance,duration=0.1) #move up
