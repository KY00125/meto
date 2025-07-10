from kivy.app import app
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.metronome_screen import MetronomeScreen
from screens.ocr_screen import OcrScreen
from screens.task_screen import TaskScreen
from screens.settings_screen import SettingScreen

class MetoronameApp(App):
  def build(self):
    sm=ScreenManager()
    sm.add_widget(HomeScreen(name='home))
    sm.add_widget(MetronomeSceen(name='metronome'))
    sm.add_widget(OcrScreen(name='ocr'))
    sm.add_widget(TaskScreen(name='tasks'))
    sm.add_Widget(SettingsScreen(name='settings'))
    return sm
                             
if __name__ == '__main__':
    MetronomeApp().run()
