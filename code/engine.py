# engine.py 
from dataclasses import dataclass
from enum import Enum
import RPi.GPIO as GPIO

@dataclass
class Engine:
  forward_pin: any
  backward_pin: any
  pwm: GPIO.PWM

  def set(self, direction: any):
    if direction >= 0.0:
      GPIO.output(self.forward_pin, GPIO.HIGH)
      GPIO.output(self.backward_pin, GPIO.LOW)
    else:
      GPIO.output(self.forward_pin, GPIO.LOW)
      GPIO.output(self.backward_pin, GPIO.HIGH)
    self.pwm.ChangeDutyCycle(abs(direction))

  def drop(self):
    GPIO.output(self.forward_pin, GPIO.LOW)
    GPIO.output(self.backward_pin, GPIO.LOW)

class Direction(Enum):
  Stop = 1,
  Forward = 2,
  Backward = 3,
  Left = 4,
  Right = 5

@dataclass
class DigitalDirectionController:
  left: Engine
  right: Engine
  
  def direction(self, direction: Direction):
    match direction:
      case Direction.Stop:
        self.left.set(0)
        self.right.set(0)
      case Direction.Forward:
        self.left.set(1)
        self.right.set(1)
      case Direction.Backward:
        self.left.set(-1)
        self.left.set(-1)
      case Direction.Left:
        self.left.set(-1)
        self.left.set(1)
      case Direction.Right:
        self.left.set(1)
        self.left.set(-1)