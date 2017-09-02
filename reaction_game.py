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
won_by_left = 0
won_by_right = 0

def pressed(button):
    #print(str(button.pin.number) + ' won the game')
    if button.pin.number == 5:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    play_again = input('play again [S/N]: S')
    if play_again == 'S':
        return (True)
    else:
        return (False)
    #exit()

right_button.when_pressed = pressed
#left_button.when_pressed = pressed
play_again = 'S'

while (pressed):
    led.on()
    sleep(uniform(1, 5))
    led.off()
    sleep(uniform(1, 5))
exit()

  
        

