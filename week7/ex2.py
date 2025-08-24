import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35,GPIO.OUT)
for x in range(0,3):
  GPIO.output(35,True)
  time.sleep(1)
  GPIO.output(35,False)
  time.sleep(1)
  GPIO.cleanup()
