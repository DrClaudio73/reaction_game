from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

left_name = input('left player name is ')
right_name = input('right player name is ')

led = LED(6)
right_button = Button(5)
#left_button = Button(14)
print(' start the game')
led.on()
sleep(uniform(1, 5))
led.off()

def pressed(button):
    print(str(button.pin.number) + ' won the game')
    exit()

right_button.when_pressed = pressed
#left_button.when_pressed = pressed


