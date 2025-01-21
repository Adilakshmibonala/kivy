from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyBoxLayout(App):
    def build(self):
        return CustomBoxLayout()
    
class CustomBoxLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(CustomBoxLayout, self).__init__(**kwargs) 

        self.orientation = "horizontal"
        self.add_widget(Label(text="UserName")) # 1
        self.username_text_object = TextInput() # 3
        self.add_widget(self.username_text_object)
        
        self.add_widget(Label(text="Password")) # 4
        self.password_text_obj = TextInput(password=True)
        self.add_widget(self.password_text_obj)


MyBoxLayout().run()
