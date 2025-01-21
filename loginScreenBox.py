from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class loginScreenPracticeApp(App):
    def build(self):
        return LoginScreenBoxLayout()

class LoginScreenBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreenBoxLayout, self).__init__(**kwargs)
        self.orientation="horizontal"
        self.padding=[20,20,20,20]
        self.spacing = 40
        self.size_hint = (0.5,0.5)
        self.pos_hint = {'center_x': 0.5,'center_y':0.5}
        self.add_widget(Label(text="UserName", height=30, size_hint_y=None))
        self.add_widget(Label(text="Please enter the username:", height=30, size_hint_y=None))
        self.username_text_object = TextInput(height=30, size_hint_y=None)
        self.add_widget(self.username_text_object)

        self.add_widget(Label(text="Password", height=30, size_hint_y=None))
        self.password_text_obj = TextInput(password=True, height=30, size_hint_y=None)
        self.add_widget(Label(text="Please enter the password:", height=30, size_hint_y=None))
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

        
loginScreenPracticeApp().run()