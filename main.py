from machine import Pin
import time
led=Pin("LED",Pin.OUT)
print("Led Blinking")
while True:
    led.value(1)
    print("LED ON")
    time.sleep(1)

    led.value(0)
    print("LED OFF")
    time.sleep(0.35)
