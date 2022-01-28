from kivy.uix.screenmanager import Screen


class Menu(Screen):
    def __init__(self,**kargs):
        Screen.__init__(self,**kargs)
        self.name = "menu"
        self.orientation= "vertical"
        
        
    def play_game(self,*args):
        self.manager.current = "game"
        
    