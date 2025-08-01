from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.storage.jsonstore import JsonStore

class MainWidget(BoxLayout):
    background_color= ListProperty([1, 1, 1, 1])  # Default white color
    button_color = ListProperty([0.5, 0.5, 0.5, 1])  # Default black color
    text_color = ListProperty([1, 1, 1, 1])  # Default black text
    
    store = JsonStore('settings.json')
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_settings()
        
    def change_style(self, new_background, new_button, new_text):
        self.background_color = new_background
        self.button_color = new_button
        self.text_color = new_text
        
        self.store.put('background', color=new_background)
        self.store.put('button', color=new_button)
        self.store.put('text', color=new_text)
        
    def load_settings(self):
        if self.store.exists('background'):
            self.background_color = self.store.get('background')['color']
        if self.store.exists('button'):
            self.button_color = self.store.get('button')['color']
        if self.store.exists('text'):
            self.text_color = self.store.get('text')['color']
            
class ColorChangeApp(App):
    def build(self):
        return MainWidget() 
    
if __name__ == '__main__':
    ColorChangeApp().run()