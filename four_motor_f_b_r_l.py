import RPi.GPIO as GPIO

GPIO.setwarnings(False)

in1 = 23
in2 = 24
in3 = 17
in4 = 27
en_a = 4
en_b = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

power_a = GPIO.PWM(en_a,100)
power_b = GPIO.PWM(en_b,100)
power_a.start(80)
power_b.start(80)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


while(True):

user_input = input()
try:
if user_input =='w': #forward
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.HIGH)
           
         
elif user_input =='s': #reverce
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)
 


elif user_input =='d': #right
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)


elif user_input =='a': #left
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.HIGH)

elif user_input =='':
continue
else:
print("!!! INVALID INPUT!!!\n\n !!PROVIDE PROPER INPUT !!!")

except KeyboardInterrupt:
power_a.stop()
power_b.stop()
GPIO.cleanup()

print("CODE TERMINTING...")
