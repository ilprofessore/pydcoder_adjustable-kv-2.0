# improvements from the previous version:
# used 'ids' instead of "ObjectProperty"; skipping importing an extra module.
# used a sustainable pattern of inheritance; can be used to add functionality later.
# methods that are shared by more than one classes are placed in 'ScreenMethod'.
# methods that are unique to a class can be placed in their respective classes.

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import FadeTransition
from kivy.core.clipboard import Clipboard
from encode import encode_module  # my custom made module.
from decode import decode_module  # my custom made module.
from kivy.lang import Builder

Builder.load_file("design.kv")
click = SoundLoader.load("click.wav")
sound = SoundLoader.load("iron.wav")
sound.loop = True
sound.play()


class ScreenMethod(Screen):
    def switch_screen(self, screen_x):
        self.manager.transition = FadeTransition(duration=0.3)
        string = "self.manager.current = " + screen_x
        exec(string)  # it executes the string.

    def clear_field(self, field_name):
        string = 'self.ids.' + field_name + '.text = ""'
        exec(string)

    def paste_text(self, field_name):
        string = 'self.ids.' + field_name + '.text = Clipboard.paste()'
        exec(string)

    def encrypt_decrypt_submit(self, choice):
        if choice == 'encrypt':
            global encrypt  # as long as global works, im fine.
            encrypt = self.ids.encrypt_input.text
            encrypt = encode_module(encrypt)
        elif choice == 'decrypt':
            global decrypt  # not a bad thing.
            decrypt = self.ids.decrypt_input.text
            decrypt = decode_module(decrypt)

    def encrypt_decrypt_set(self, choice):
        if choice == 'encrypt':
            self.ids.encrypt_output.text = encrypt
        elif choice == 'decrypt':
            self.ids.decrypt_output.text = decrypt

    def copy_text(self, choice):
        string = 'Clipboard.copy(self.ids.' + choice + '.text)'
        exec(string)

    @property
    def click_sound(self):
        click.play()

    @property
    def on_exit(self):
        quit()

class ScreenOne(ScreenMethod):
    pass


class ScreenTwo(ScreenMethod):
    pass


class ScreenThree(ScreenMethod):
    pass


class ScreenFour(ScreenMethod):
    pass


class ScreenFive(ScreenMethod):
    pass

class ZainInfo(ScreenMethod):
    pass

class Manager(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return Manager()


if __name__ == '__main__':
    MainApp().run()
