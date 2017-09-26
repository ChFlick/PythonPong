from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    score = NumericProperty(0)

    def reset_paddle(self, window_height):
        self.y = window_height - self.height / 2

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 4)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
