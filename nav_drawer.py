from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


Window.size = (300,500) 

screen_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
        
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: "Navigation Drawer"
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 10
                        
                    Widget:
                    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'vani.jpg'
                    ScreenManager:
                        ImageScreen:

                MDLabel:
                    text: 'Manas'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'manasbrnwal15@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'profile'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'LogOut'
                            IconLeftWidget:
                                icon: 'logout'
<ImageScreen>:
    name: 'img'
    MDIconButton:
        icon: 'vani.jpg'
        on_press: root.manager.current = 'profile'
"""

class ImageScreen(Screen):
    pass

sm = ScreenManager()
sm.add.widget(ImageScreen(name='img'))

class DemoApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(screen_helper)
        
        return screen

DemoApp().run()
