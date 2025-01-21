from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
class MyGrid(App):
    def build(self):
        return LoginScreenGrid()


class LoginScreenGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreenGrid, self).__init__(**kwargs) # super()

        self.cols = 4
        self.padding = [20, 20, 20, 20]
        self.spacing = 20
        self.size_hint = (0.5, 0.5) # (h, w)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5} # Position

        self.add_widget(Label(text="2", height=30, size_hint_y=None))
        self.add_widget(Label(text="8", height=30, size_hint_y=None))
        self.add_widget(Label(text="7", height=30, size_hint_y=None))
        self.add_widget(Label(text="6", height=30, size_hint_y=None))
        self.add_widget(Label(text="1", height=30, size_hint_y=None))
        self.add_widget(Label(text="12", height=30, size_hint_y=None))
        self.add_widget(Label(text="3", height=30, size_hint_y=None))
        self.add_widget(Label(text="11", height=30, size_hint_y=None))
        self.add_widget(Label(text="5", height=30, size_hint_y=None))
        self.add_widget(Label(text="15", height=30, size_hint_y=None))
        self.add_widget(Label(text="14", height=30, size_hint_y=None))
        self.add_widget(Label(text="4", height=30, size_hint_y=None))
        self.add_widget(Label(text="10", height=30, size_hint_y=None))
        self.add_widget(Label(text="13", height=30, size_hint_y=None))
        self.add_widget(Label(text="9", height=30, size_hint_y=None))
MyGrid().run()
