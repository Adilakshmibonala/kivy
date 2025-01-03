from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen123App(App): # kiwi app name.
    def build(self):
        return LoginScreenGrid()


class LoginScreenGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreenGrid, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text="UserName", height=30, size_hint_y=None))
        self.username_text_object = TextInput(height=30, size_hint_y=None)
        self.add_widget(self.username_text_object)

        self.add_widget(Label(text="Password", height=30, size_hint_y=None))
        self.password_text_obj = TextInput(password=True, height=30, size_hint_y=None)
        self.add_widget(self.password_text_obj)

        button = Button(text="Login", height=30, size_hint_y=None)
        button.bind(on_press=self.validate_user_name_and_password)
  
        self.add_widget(button)
    
    def validate_user_name_and_password(self, kivy_instance):
        print(self.username_text_object.text, self.password_text_obj.text)
        dummy_user_name = "admin"
        dummy_password = "admin"
        label_obj = Label(text="", height=30, size_hint_y=None)
        self.add_widget(label_obj)
        if self.username_text_object.text == dummy_user_name and self.password_text_obj.text == dummy_password:
            label_obj.text = "WELCOME"
        else:
            label_obj.text="Invalid username and password!!"


LoginScreen123App().run()

