from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen




class GridAndBoxLayoutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        box_layout = BoxLayout(orientation="vertical", padding=15, spacing=15)

        label = Label(text="Welcome", font_size="30sp", bold=True, color=(0, 0.5, 0.8, 1), size_hint=(1, 0.5))
        box_layout.add_widget(label)


        grid_layout = GridLayout(cols=3, spacing=10, size_hint=(1, 3))
        for i in range(1, 10):
            grid_layout.add_widget(Button(text=f"Button {i}", background_color=(0, 0.5, 0.8, 1), font_size="20sp"))
        box_layout.add_widget(grid_layout) # Adding GridLayout to BoxLayout

        footer = Button(text="Footer Button", background_color=(0, 0.5, 0.8, 1), font_size="20sp")
        box_layout.add_widget(footer)

        self.add_widget(box_layout)