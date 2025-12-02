import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Create keyboard object
kbd = Keyboard(usb_hid.devices)

# Define button pins (using standard Pico W GPIO pinout)
BUTTON_A_PIN = board.GP14
BUTTON_D_PIN = board.GP15

# Setup buttons with internal pull-ups
button_a = digitalio.DigitalInOut(BUTTON_A_PIN)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

button_d = digitalio.DigitalInOut(BUTTON_D_PIN)
button_d.direction = digitalio.Direction.INPUT
button_d.pull = digitalio.Pull.UP

# Debounce delay (in seconds)
DEBOUNCE_DELAY = 0.1

last_a_state = True
last_d_state = True

while True:
    a_pressed = not button_a.value  
    d_pressed = not button_d.value
    
    if a_pressed and last_a_state:
        kbd.send(Keycode.A)
        print("A sent")
        time.sleep(DEBOUNCE_DELAY)
        
    last_a_state = a_pressed
    
    if d_pressed and last_d_state:
        kbd.send(Keycode.D)
        print("D sent")
        time.sleep(DEBOUNCE_DELAY)
        
    last_d_state = d_pressed
    
    time.sleep(0.01)

