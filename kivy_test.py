

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDTextButton
from kivy.lang import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        screen = Builder.load_file('my.kv')



        return screen


MainApp().run()