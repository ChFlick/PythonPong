from random import randint

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from PongPaddle import InputType


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def __init__(self, movementoption, **kwargs):
        super(PongGame, self).__init__(**kwargs)

        self.movementoption = movementoption
        if movementoption == 'keyboard':
            self.player1.init_input(InputType.WS)
            self.player2.init_input(InputType.UPDOWN)
        elif movementoption == 'ki':
            self.player1.init_input(InputType.WS)
            self.player2.init_input(InputType.KI)

    def update(self, dt):
        self.ball.move()

        self.player1.update()
        self.player2.update()

        self.__check_player_hit()
        self.__check_wall_hit()
        self.__check_score()

    def serve_ball(self, vel=(4 if randint(0, 1) is 0 else -4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def reset_paddles(self):
        posY = self.height / 2
        self.player1.reset_paddle(posY)
        self.player2.reset_paddle(posY)

    def restart(self):
        self.serve_ball()
        self.reset_paddles()

    def __check_player_hit(self):
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def __check_wall_hit(self):
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

    def __check_score(self):
        if self.ball.x < self.x:
            self.player2.score += 1
            self.restart()
        elif self.ball.x > self.width:
            self.player1.score += 1
            self.restart()

    '''move the player paddles by touching the sides'''
    def on_touch_move(self, touch):
        if self.movementoption != 'keyboard':
            if touch.x < self.width / 3:
                self.player1.center_y = touch.y
            if self.movementoption == 'touch' and touch.x > self.width - self.width / 3:
                self.player2.center_y = touch.y