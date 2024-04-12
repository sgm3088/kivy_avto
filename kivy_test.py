

from kivymd.app import MDApp
from kivy.lang import Builder


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"

        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_file('my.kv')



        return screen


MainApp().run()