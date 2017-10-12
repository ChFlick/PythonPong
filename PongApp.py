from kivy.app import App
from kivy.clock import Clock

from PongGame import PongGame


class PongApp(App):
    def build(self):
        game = PongGame('touch')
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()