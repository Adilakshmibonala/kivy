from kivy.app import App  # import
from kivy.uix.label import Label


class FirstApp(App):
    
    def build(self):
        return Label(text="My First kivi app.") ####



FirstApp().run()


"""
1. --> It's kivi app. 
2. --> build --> 1st it will execute.
3. --> run() --> build method inside the App we implemented.
"""
