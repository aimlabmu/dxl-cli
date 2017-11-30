import smbus
import RPi.GPIO as GPIO
import time

#  setup button input pins
BTN_1 = 6
BTN_2 = 13
BTN_3 = 19
BTN_4 = 26
SOUND_PIN = 5
MOTOR_PIN = 9

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setup(BTN_1,GPIO.IN)
GPIO.setup(BTN_2,GPIO.IN)
GPIO.setup(BTN_3,GPIO.IN)
GPIO.setup(BTN_4,GPIO.IN)
GPIO.setup(SOUND_PIN, GPIO.OUT)
GPIO.output(SOUND_PIN, GPIO.LOW)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.output(MOTOR_PIN, GPIO.HIGH)

IODIR = 0x00 # I/O DIRECTION REGISTER
GPIO_ROBOT  = 0x09 # Set/Reset GPIO REGISTER
output_mode  = 0x00

bus = smbus.SMBus(1)  # I2C port 1

control_byte = 0x21  # control byte not include R/W bit use just 7 bit

def write_output(control_byte, register_address, value):
        bus.write_byte_data(control_byte, register_address, value)

write_output(control_byte, IODIR, output_mode) # setup output port A

# cut electric power to motor
WriteOutput(control_byte,GPIO_ROBOT,0x00) # Write the output to port A
time.sleep(3)

# resume
write_output(control_byte, GPIO_ROBOT, 0xFF) # Write the output to port A
time.sleep(0.5)