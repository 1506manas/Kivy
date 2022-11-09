from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

import pymysql
import datetime

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database = 'bike_rental')
cur = connection.cursor()

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class TestApp(App):
    def build(self):
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

        self.value = TextInput(text = "Enter the bike you want to add:")
        self.number = TextInput(text = "Enter the bike number")
        self.rent_per_hour = TextInput(text = 'Enter the rent for an hour:')
        self.rent_per_day = TextInput(text = 'Enter the rent for a day:')
        self.rent_per_month = TextInput(text = 'Enter the rent for a month:')        

        
        layout.add_widget(label)
        layout.add_widget(self.value)
        layout.add_widget(self.number)
        layout.add_widget(self.rent_per_hour)
        layout.add_widget(self.rent_per_day)
        layout.add_widget(self.rent_per_month)        
        layout.add_widget(submit)

        return layout

    def printpress(self, obj):
        sql = "INSERT INTO Bikes(Name, Bike_Number, Rent_Per_Hour, Rent_Per_Day, Rent_Per_Month) VALUES ('{}','{}',{},{},{})".format(self.value.text,self.number.text,self.rent_per_hour.text,self.rent_per_day.text,self.rent_per_month.text)
        cur.execute(sql)

        connection.commit()
        

TestApp().run()
