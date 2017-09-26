from random import randint

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4 if randint(0, 1) is 0 else -4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.__checkPlayerHit()
        self.__checkWallHit()
        self.__checkScore()

    def __checkPlayerHit(self):
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def __checkWallHit(self):
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

    def __checkScore(self):
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(-4, 0))
        elif self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(4, 0))

    '''move the player paddles by touching the sides'''
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
