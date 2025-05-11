from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen



class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "screen 1", color = "red", font_size = 50)
        btn = Button(text = "Click Me to go to screen 2")
        btn.on_press = self.swap_to_screen2
        hl = BoxLayout(orientation = "horizontal")
        hl.add_widget(txt)
        hl.add_widget(btn)
        self.add_widget(hl)
    
    def swap_to_screen2(self):
        self.manager.transition.direction = "down"
        self.manager.current = "screen2"

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "screen 2", color = "blue", font_size = 50)
        btn = Button(text = "Click Me to go to screen 1")
        btn.on_press = self.swap_to_screen1
        hl = BoxLayout(orientation = "horizontal")
        hl.add_widget(txt)
        hl.add_widget(btn)
        self.add_widget(hl)

    def swap_to_screen1(self):
        self.manager.transition.direction = "up"
        self.manager.current = "screen1"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name="screen1"))
        sm.add_widget(Screen2(name="screen2"))

        return sm

app = MyApp()
app.run()