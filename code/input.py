# input.py 
from dataclasses import dataclass
import RPi.GPIO as GPIO
from engine import Direction

@dataclass
class ButtonInput:
  forward: any
  backward: any
  left: any
  right: any

  def get_direction(self) -> Direction:
    if GPIO.input(self.forward):
      return Direction.Forward
    if GPIO.input(self.left):
      return Direction.Left
    if GPIO.input(self.right):
      return Direction.Right
    if GPIO.input(self.backward):
      return Direction.Backward
    return Direction.Stop