from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # self.size_hint = (0.6, 0.4)
        # self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.cols = 2 # Changed to 2 columns for better alignment
        
        # Add widgets for username
        self.add_widget(Label(text='User Name: ', size_hint_y=None, height=30))
        self.username = TextInput(size_hint_y=None, height=30)
        self.add_widget(self.username)
        
        # Add widgets for password
        self.add_widget(Label(text='Password:', size_hint_y=None, height=30))
        self.password = TextInput(password=True, size_hint_y=None, height=30)
        self.add_widget(self.password)
        
        # Add a button to validate
        self.login_button = Button(text="Login", size_hint_y=None, height=40)
        self.login_button.bind(on_press=self.validate_credentials)
        self.add_widget(self.login_button)
        
        # Add a label to display the result
        self.result_label = Label(text="", size_hint_y=None, height=30)
        self.add_widget(self.result_label)

    def validate_credentials(self, instance):
        # Check if username and password are "admin"
        print(self.username.text, self.password.text)
        if self.username.text == "admin" and self.password.text == "admin":
            self.result_label.text = "Welcome, Admin!"
        else:
            self.result_label.text = "Invalid username or password."


class LoginScreenApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginScreenApp().run()
