# main.py 
import RPi.GPIO as GPIO
import engine
import input
import time

def main():
    GPIO.setmode(GPIO.BCM)
    engine_left = engine.Engine(
        forward_pin = GPIO.setup(14, GPIO.OUT),
        backward_pin= GPIO.setup(15, GPIO.OUT),
        pwm = GPIO.PWM(18, 20),
    )
    engine_left.pwm.Start(0)

    engine_right = engine.Engine(
        forward_pin = GPIO.setup(26, GPIO.OUT),
        backward_pin = GPIO.setup(13, GPIO.OUT),
        pwm = GPIO.PWM(19, 20)
    )
    engine_right.pwm.Start(0)
    
    ddc = engine.DigitalDirectionController(
        left = engine_left,
        right = engine_right
    )

    inp = input.ButtonInput(
        forward = GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP),
        backward = GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP),
        left = GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP),
        right = GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    )

    while True:
        direction = inp.get_direction()
        print(f"Direction: {direction}")
        ddc.direction(direction)
        time.sleep(0.050)

if __name__ == "__main__":
    main()