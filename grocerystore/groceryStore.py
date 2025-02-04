from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button




class GridAndBoxLayoutScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 15

        label = Label(text="Grocery Store", font_size="30sp", bold=True, color=(0, 0.5, 0.8, 1), size_hint=(1, 0.5))
        self.add_widget(label)


        grid_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 3))
        grocery=["apple", "banana", "orange", "eggs", "milk", "cheese", "avocado", "chocolate", "bread", "spinach"]
        for item in grocery:
            print(item)
            grid_layout.add_widget(Button(text=item, background_color=(0, 0.5, 0.8, 1), font_size="20sp"))
        self.add_widget(grid_layout) # Adding GridLayout to BoxLayout

        footer = Button(text="Checkout", background_color=(0, 0.5, 0.8, 1), font_size="20sp")
        self.add_widget(footer)


class GridAndBoxLayout(App):
    def build(self):
        return GridAndBoxLayoutScreen()


GridAndBoxLayout().run()
