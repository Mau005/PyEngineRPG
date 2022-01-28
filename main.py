
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from gui.menu import Menu
from game import Game
Builder.load_file("gui/menu.kv")


class MyApp(App):
    def __init__(self,**kargs):
        App.__init__(self,**kargs)
        self.manager = ScreenManager()
        self.menu = Menu()
        self.game = Game()
        self.conf_window()
        
        
    def conf_window(self):
        self.manager.add_widget(self.menu)
        self.manager.add_widget(self.game)
        
    def build(self):
        return self.manager
    
    

    
if __name__ == '__main__':
    MyApp().run()