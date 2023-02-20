from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.properties import ObjectProperty


# Window.size = (720, 1200)
Window.size = (480, 853)

Config.set('kivy', 'keyboard_mode', 'systemanddock')


class VariableContainer:
    def __init__(self):
        self.dict_var = {}
        self.cnt = 0

    def variable_dict(self):
        key = 'num'
        self.dict_var[self.cnt] = {key: '', key + '_change': '', key + '_plan': ''}
        self.cnt += 1


class Container(GridLayout, VariableContainer):

    gridLayout_workout = ObjectProperty()
    stopwatch = ObjectProperty()

    def start_workout(self):
        while len(self.dict_var) < 10:
            self.variable_dict()

            layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
            text_input_workout = TextInput(multiline=False)
            text_input_plan = TextInput(multiline=False, input_filter='int', size_hint_x=0.4)
            label_current = Label(size_hint_x=0.4)
            text_input_change = TextInput(multiline=False, input_filter='int', size_hint_x=0.4)
            layout.add_widget(text_input_workout)
            layout.add_widget(text_input_plan)
            layout.add_widget(label_current)
            layout.add_widget(text_input_change)
            self.gridLayout_workout.add_widget(layout)
        self.change_number()

    def change_number(self):
        for key, value in self.dict_var.items():
            num = self.children[1].children[key].children[0]
            num_change = self.children[1].children[key].children[1]
            num_plan = self.children[1].children[key].children[2]
            for i in value:
                if i == 'num':
                    self.dict_var[key][i] = num
                elif i == 'num_change':
                    self.dict_var[key][i] = num_change
                elif i == 'num_plan':
                    self.dict_var[key][i] = num_plan

    def reset(self):
        for fields in self.dict_var.values():
            for value in fields.values():
                value.text = ''

    def add_number(self):
        for key, value in self.dict_var.items():
            if value['num'].text and not value['num_change'].text:
                value['num_change'].text = value['num'].text
            elif value['num'].text and value['num_change'].text:
                value['num_change'].text = str(int(value['num_change'].text) + int(value['num'].text))
            value['num'].text = ''

    def time_workout_start(self):
        Clock.schedule_interval(self.callback, 1)

    def callback(self, dt):
        try:
            self.stopwatch.text = str(int(self.stopwatch.text) + 1)
        except:
            self.stopwatch.text = '-5'

    def time_workout_pause(self):
        Clock.unschedule(self.callback)

    def time_workout_stop(self):
        Clock.unschedule(self.callback)
        self.stopwatch.text = '00:00'


class WorkoutApp(App):
    title = 'Workout'
    icon = 'barbell.png'

    def build(self):
        Window.clearcolor = (0, 0, 0.1, .8)
        return Container()


if __name__ == "__main__":
    WorkoutApp().run()
