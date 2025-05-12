from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen, direction = "right", goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation = "horizontal")
        left_box = BoxLayout()
        txt = Label(text = "Вибери екран")
        left_box.add_widget(txt)

        right_box = BoxLayout(orientation = "vertical",
                              padding = 10,
                              spacing = 10)
        btn1 = ScrButton(self,
                            goal="screen1",
                            text = "1",
                            size_hint = (1, 0.25))
        btn2 = ScrButton(self,
                            goal="screen2",
                            text = "2",
                            size_hint = (1, 0.25))
        btn3 = ScrButton(self,
                            goal="screen3",
                            text = "3",
                            size_hint = (1, 0.25))
        btn4 = ScrButton(self,
                            goal="screen4",
                            text = "4",
                            size_hint = (1, 0.25))
        
        right_box.add_widget(btn1)
        right_box.add_widget(btn2)
        right_box.add_widget(btn3)
        right_box.add_widget(btn4)
        hl.add_widget(left_box)
        hl.add_widget(right_box)
        self.add_widget(hl)

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation = "horizontal",
                        padding = 200,
                        spacing = 10)
        btn = Button(text = "Вибір 1",
                        size_hint = (1, 0.5),
                        pos_hint = {"x": 0.5, "y": 0.5},)
        btn1 = ScrButton(self,
                        goal="main",
                        text = "Назад",
                        size_hint = (1, 0.5))
        hl.add_widget(btn)
        hl.add_widget(btn1)
        self.add_widget(hl)

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation = "vertical")
        txt = Label(text = "Вибір 2")
        hl.add_widget(txt)
        vr = BoxLayout(orientation = "horizontal",
                       size_hint = (1, 0.1),
                       padding = [0, 0, 100, 0],)
        txt1 = Label(text = "Введіть пароль:",
                                size_hint = (1, 0.5))
        passw_input = TextInput(multiline = False,
                                password = True,
                                password_mask = "*",
                                size_hint = (1, 0.5))
        vr1 = BoxLayout(orientation = "horizontal",
                        size_hint = (1, 0.3),
                        padding = [150, 0, 150, 0],)
        bnt1 = ScrButton(self,
                        goal="main",
                        text = "OK!")
        btn2 = ScrButton(self,
                        goal="main",
                        text = "Назад")
        vr.add_widget(txt1)
        vr.add_widget(passw_input)
        vr1.add_widget(bnt1)
        vr1.add_widget(btn2)
        hl.add_widget(vr)
        hl.add_widget(vr1)
        self.add_widget(hl)

class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation = "vertical",)
        txt = Label(text = "Твій власний екран")
        btn = ScrButton(self,
                        goal="main",
                        text = "Назад",
                        size_hint = (1, 0.1))
        hl.add_widget(txt)
        hl.add_widget(btn)
        self.add_widget(hl)

class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        hl = BoxLayout(orientation = "vertical",)
        txt = Label(text = "Додатковий завдання", size_hint = (1, 0.2))
        btn = ScrButton(self,
                        goal="main",
                        text = "Назад",
                        size_hint = (1, 0.2))
        self.label = Label(text = "Введіть текст:\n" + "Багато" * 600,
                     size_hint_y = None,
                     font_size = 20,
                     halign = "left",
                     valign = "top")
        self.label.bind(size=self.resize)
        self.scroll = ScrollView(size_hint=(1, 1))
        self.scroll.add_widget(self.label)
        
        hl.add_widget(txt)
        hl.add_widget(btn)
        hl.add_widget(self.scroll)
        self.add_widget(hl)
    def resize(self, *args):
        self.label.text_size = (self.label.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name="main"))
        sm.add_widget(Screen1(name="screen1"))
        sm.add_widget(Screen2(name="screen2"))
        sm.add_widget(Screen3(name="screen3"))
        sm.add_widget(Screen4(name="screen4"))

        return sm

app = MyApp()
app.run()