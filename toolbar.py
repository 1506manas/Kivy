from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500) 

screen_helper = """
Screen:
    

    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Demo'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            elevation: 20
        MDLabel:
            text: 'Hello World'
            halign: 'center'

        MDBottomAppBar:
            MDTopAppBar:
                left_action_items: [["dog", lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
"""

class DemoApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        return screen

    def navigation_draw(self):
        print("Navigation")

DemoApp().run()
