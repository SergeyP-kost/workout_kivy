from kivy.app import App
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config


# Window.size = (720, 1200)
Window.size = (480, 853)

Config.set('kivy', 'keyboard_mode', 'systemanddock')


class Container(GridLayout):

    def button_num(self):

        num = {
            'num_1': self.num_1,
            'num_2': self.num_2,
            'num_3': self.num_3,
            'num_4': self.num_4,
            'num_5': self.num_5,
        }

        num_change = {
            'num_1': self.num_1_change,
            'num_2': self.num_2_change,
            'num_3': self.num_3_change,
            'num_4': self.num_4_change,
            'num_5': self.num_5_change,
        }

        num_plan = {
            'num_1': self.num_1_plan,
            'num_2': self.num_2_plan,
            'num_3': self.num_3_plan,
            'num_4': self.num_4_plan,
            'num_5': self.num_5_plan,
        }
        return [num, num_change, num_plan]

    def reset(self):
        fields = self.button_num()
        for field in fields:
            for key, value in field.items():
                value.text = ''

    def add_number(self):
        fields = self.button_num()
        for key, value in fields[0].items():
            if value.text and not fields[1][key].text:
                fields[1][key].text = value.text
            elif value.text and fields[1][key].text:
                fields[1][key].text = str(int(fields[1][key].text) + int(value.text))
            value.text = ''

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
        return Container()


if __name__ == "__main__":
    WorkoutApp().run()
