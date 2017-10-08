from kivy.core.window import Window
from Singleton import Singleton


class Keyboard(metaclass=Singleton):
    def __init__(self):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.pressedKeys = dict()

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.pressedKeys[keycode[0]] = True

    def _on_keyboard_up(self, keyboard, keycode):
        self.pressedKeys[keycode[0]] = False
