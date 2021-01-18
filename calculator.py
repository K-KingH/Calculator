from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config 
Config.set('graphics','resizable', 1)

Builder.load_string(""" 
<Cust@Button>:
    font_size: 30
    
<Cal>:
    id: comp
    display: entry
    rows: 6
    padding: 10
    spacing: 10
    
    BoxLayout:
        TextInput:
            id: entry
            font_size: 30
            multiline: False
            
    BoxLayout:
        spacing: 5
        Cust: 
            text: "7"
            on_press: entry.text += self.text
        Cust: 
            text: "8"
            on_press: entry.text += self.text
        Cust: 
            text: "9"
            on_press: entry.text += self.text
        Cust: 
            text: "+"
            on_press: entry.text += self.text
            
    BoxLayout:
        spacing: 5
        Cust: 
            text: "4"
            on_press: entry.text += self.text
        Cust: 
            text: "5"
            on_press: entry.text += self.text
        Cust: 
            text: "6"
            on_press: entry.text += self.text
        Cust: 
            text: "-"
            on_press: entry.text += self.text
            
    BoxLayout:
        spacing: 5
        Cust: 
            text: "1"
            on_press: entry.text += self.text
        Cust: 
            text: "2"
            on_press: entry.text += self.text
        Cust: 
            text: "3"
            on_press: entry.text += self.text
        Cust: 
            text: "*"
            on_press: entry.text += self.text
            
    BoxLayout:
        spacing: 5
        Cust: 
            text: "0"
            on_press: entry.text += self.text
        Cust: 
            text: "AC"
            on_press: entry.text = ""
        Cust: 
            text: "="
            on_press: comp.calculator(entry.text)
        Cust: 
            text: "/"
            on_press: entry.text += self.text
""")

class Cal(GridLayout):
    def calculator(self, user):
        if input:
            try:
                self.display.text = str(eval(user))
            except Exception:
                self.display.text = "Error"
    
            
class CalApp(App):
    def build(self):
        return Cal()

CalApp().run()