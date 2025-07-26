import os
import sys
import time
import kivy
from kivy.uix.widget import Widget
from watchdog.events import FileSystemEventHandler
from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Ellipse, Color
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class CircleAnimationWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_circles = 9
        self.circles = []
        self.current_index = 0
        self.direction = 1
        self.is_running = False
        self.clock_event = None
        self.interval = 1/self.num_circles  # Default interval for animation
        
        for i in range(self.num_circles):
            with self.canvas:
                color = Color(1, 1,1, 0.2)  # Initial color with alpha
                widget_width = self.width
                spacing = widget_width / (self.num_circles + 1)
                circle = Ellipse(size=(spacing, spacing))
                self.circles.append({"color": color, "circle": circle})
                
        self.bind(pos=self.update_positions, size=self.update_positions)
        self.update_positions()
        
    def update_positions(self, *args):
        widget_width = self.width
        widget_height = self.height
        spacing = widget_width / (self.num_circles + 1)
        circle_diameter = widget_width / (self.num_circles +1)  # 高さの80%か100の小さい方
        for i, circle_info in enumerate(self.circles):
            circle = circle_info["circle"]
            circle.size = (circle_diameter, circle_diameter)
            circle.pos = (
                spacing * (i + 1) - circle.size[0] / 4,
                widget_height - circle.size[1] / 4
            )

    def update_animation(self, dt):
        for circle_info in self.circles:
            circle_info["color"].rgba = (1, 1, 1, 0.2)  # Reset color to white with 0.2 alpha
           
        self.circles[self.current_index]["color"].rgba = (1, 0, 0, 1)  # Highlight current circle
            
        self.current_index += self.direction
        if self.current_index >= self.num_circles or self.current_index < 0:
            self.direction *= -1
            self.current_index += self.direction  # Adjust index to stay within bounds  
            
    def toggle_animation(self,button):
        if self.is_running:
            self.stop_animation()
            button.text = "Start"
        else:
            self.start_animation()
            button.text = "Stop"

    def start_animation(self):
        if not self.is_running:
            self.is_running = True
            self.clock_event = Clock.schedule_interval(self.update_animation, self.interval)
            
    def stop_animation(self):
        if self.is_running:
            
            self.current_index = 0
            for circle_info in self.circles:
                circle_info["color"].rgba = (1, 1, 1, 0.2)  # Reset color to white with 0.2 alpha
           
            self.circles[self.current_index]["color"].rgba = (1, 0, 0, 1)  # Highlight current circle
            self.is_running = False
            Clock.unschedule(self.clock_event)
            self.clock_event = None
        
    def update_speed(self, speed):
        self.interval = 60 / (speed * self.num_circles)
        if self.is_running:
            self.stop_animation()
            self.start_animation()
            
class CircleAnimationApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        # サークル部分
        circle_widget = CircleAnimationWidget(size_hint=(1, 0.25))  # 上部を75%使う
        root.add_widget(circle_widget)

        # 下部コントロール部分（スライダー＋ボタン）
        controls = BoxLayout(orientation='vertical', size_hint=(1, 0.25))

        slider_label = Label(text="BPM: 60", size_hint=(1, 0.25))
        speed_slider = Slider(min=40, max=200, value=60, step=5)  # stepを5に
        speed_slider.bind(value=lambda instance, value: [
            setattr(slider_label, 'text', f"BPM: {int(value)}"),
            circle_widget.update_speed(int(value))
        ])

        button_layout = BoxLayout(size_hint=(1, 0.25))
        toggle_button = Button(text="Start")
        toggle_button.bind(on_press=lambda instance: circle_widget.toggle_animation(toggle_button))
        button_layout.add_widget(toggle_button)
        
        controls.add_widget(slider_label)
        controls.add_widget(speed_slider)
        controls.add_widget(button_layout)

        root.add_widget(controls)
        return root
    
class FileChangeHandler(FileSystemEventHandler):
    
    def __init__(self, app):
        self.app = app
        
    def on_modified(self, event):
        if event.src_path.endswith('meto.py'):
            print(f"File {event.src_path} has been modified. Restarting the app...")
            os.execv(sys.executable, [sys.executable] + sys.argv)
            

if __name__ == '__main__':
    CircleAnimationApp().run()
    