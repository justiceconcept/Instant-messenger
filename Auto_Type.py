import pyautogui as pg
import time

time.sleep(10)

for i in range(10):
    pg.write('hi, Good Morning, How are you doing!')
    pg.press('enter')
