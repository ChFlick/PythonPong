from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.core.window import Keyboard as KivyKeyboard
from kivy.vector import Vector
from Keyboard import Keyboard

from enum import Enum


class InputType(Enum):
    TOUCH = 1
    KI = 2
    WS = 3
    UPDOWN = 4


class PongPaddle(Widget):
    keyboard = Keyboard()
    score = NumericProperty(0)

    def __init__(self,  **kwargs):
        super(PongPaddle, self).__init__(**kwargs)
        self.__btn_up = None
        self.__btn_down = None

    def init_input(self, inputtype):
        if inputtype == InputType.WS:
            self.__btn_up = KivyKeyboard.keycodes['w']
            self.__btn_down = KivyKeyboard.keycodes['s']
        elif inputtype == InputType.UPDOWN:
            self.__btn_up = KivyKeyboard.keycodes['up']
            self.__btn_down = KivyKeyboard.keycodes['down']

    def reset_paddle(self, window_height):
        self.y = window_height - self.height / 2

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 4)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

    def update(self):
        if self.keyboard.pressedKeys.get(self.__btn_up) and self.y + self.height < self.parent.height:
            self.y += 10
        elif self.keyboard.pressedKeys.get(self.__btn_down) and self.y > 0:
            self.y -= 10
