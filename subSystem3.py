from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from docx import Document
import sqlite3
from kivy.uix.screenmanager import ScreenManager,Screen

class Manager(ScreenManager):
    ...
class HomeScreen(Screen):
    ...

class SearchScreen(Screen):
    def Find(*args) :
        print("click") 
    
class Search(MDApp):
    def build(self):
        Window.size = (300, 430)
        Window.clearcolor = "#6C847046"
        self.theme_cls.primary_palette = "White"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("search.kv")

Search().run()