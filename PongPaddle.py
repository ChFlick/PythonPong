from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.core.window import Keyboard as KivyKeyboard
from kivy.vector import Vector
from Keyboard import Keyboard
from math import sin, cos, sqrt
import numpy as np

from enum import Enum


class InputType(Enum):
    TOUCH = 1
    KI = 2
    WS = 3
    UPDOWN = 4


class PongPaddle(Widget):
    MAX_BOUNCE_ANGLE = 1.0472
    keyboard = Keyboard()
    score = NumericProperty(0)

    def __init__(self,  **kwargs):
        super(PongPaddle, self).__init__(**kwargs)
        self.__btn_up = None
        self.__btn_down = None
        self.__input = None

    def init_input(self, inputtype):
        if inputtype == InputType.WS:
            self.__btn_up = KivyKeyboard.keycodes['w']
            self.__btn_down = KivyKeyboard.keycodes['s']
        elif inputtype == InputType.UPDOWN:
            self.__btn_up = KivyKeyboard.keycodes['up']
            self.__btn_down = KivyKeyboard.keycodes['down']
        elif inputtype == InputType.KI:
            self.__input = InputType.KI

    def reset_paddle(self, window_height):
        self.y = window_height - self.height / 2

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            dir = -1 if vx > 0 else 1
            ballspeed = np.linalg.norm((vx, vy))
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounceAngle = offset * self.MAX_BOUNCE_ANGLE
            vx = dir * ballspeed * 1.1 * cos(bounceAngle)
            vy = ballspeed * 1.1 * sin(bounceAngle)
            ball.velocity = float(vx), float(vy)

    def update(self):
        if self.__input == InputType.KI:
            if self.center_y - 20 > self.parent.ball.center_y:
                self.y -= self.parent.ball.center_x / 100
            elif self.center_y + 20 < self.parent.ball.center_y:
                self.y += self.parent.ball.center_x / 100

        if self.keyboard.pressedKeys.get(self.__btn_up) and self.y + self.height < self.parent.height:
            self.y += 10
        elif self.keyboard.pressedKeys.get(self.__btn_down) and self.y > 0:
            self.y -= 10
