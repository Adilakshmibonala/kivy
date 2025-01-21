from kivy.app import App
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        return Button(text="Login")
LoginApp().run()

