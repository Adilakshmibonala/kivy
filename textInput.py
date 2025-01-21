from kivy.app import App
from kivy.uix.textinput import TextInput

class loginScreenApp(App):
    def build(self):
        return TextInput()
loginScreenApp().run()
