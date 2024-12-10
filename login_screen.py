from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class LoginScreen123App(App): # kiwi app name.
    def build(self):
        return LoginScreenGrid()


class LoginScreenGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreenGrid, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="UserName"))
        self.add_widget(TextInput())

        self.add_widget(Label(text="Password"))
        self.add_widget(TextInput(password=True))


LoginScreen123App().run()

