from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

#class PongGame(Widget):
    #pass

class TestApp(App):
    def build(self):

        #layout by Grid
        """layout = GridLayout(cols = 2, row_force_default = True, row_default_height = 40)"""

        #layout by Box
        layout = BoxLayout(orientation = 'vertical', spacing = 10, padding =40)
        
        #adding text to window
        label = Label(text = 'Please Enter Your Height and Weight', font_size = '20sp',
                      bold = True,
                      color = (0,0,0,1),
                      italic = True)

        #adding a button on window
        submit = Button(text = 'Submit', size_hint = (None,None),
                        height = 50, width = 100,
                        font_size = '20sp', pos_hint = {'center_x': 0.5},
                        on_press = self.printpress)
        
        """button2 = Button(text = 'Dont Click Here', size_hint = (None,None),
                        height = 50, width = 150,
                        font_size = '20sp', pos_hint = {'center_x': 0.5},
                        on_press = self.printpress)"""

        #adding an image on window
        """img = Image(source = 'vani.jpg', height = 200, width = 200)"""

        #adding InputText
        self.height = TextInput(text = 'Enter The Height:')
        self.weight = TextInput(text = 'Enter The Weight:')

        
        layout.add_widget(label)
        #layout.add_widget(img)
        #layout.add_widget(button2)
        layout.add_widget(self.height)
        layout.add_widget(self.weight)
        layout.add_widget(submit)
        
        #return label
        #return button
        return layout

    #function called when button is pressed
    def printpress(self, obj):
        print("Height is"+self.height.text)
        print("weight is:"+ self.weight.text)

TestApp().run()
