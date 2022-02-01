from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock

from core.list_obj import List_Obj
from Textures.render import Render

from Textures.AnimationTexture import AnimationTexture
from core.constantes import ANIMATION_HUMAN,CONF_ANIMATION_HUMAN,MARGE_WIDTH, MARGE_HEIGHT,RESOLUTION
from entityGame.character import Character
from entityGame.ability import Ability
from entityGame.tree_ability import Tree_Ability
from core.logic import Logic
from core.control import Control


def size_update():
    window_x,window_y = Window.size
    return [window_x/MARGE_WIDTH,window_y/MARGE_HEIGHT]
    


class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down = self._on_key_down)
        self._keyboard.bind(on_key_up = self._on_key_up)

        self.scene= Render()
        self.List_Obj = List_Obj()
        self.control = Control(size_update())

            
        self.conf_player()
        
        
        self.keysPressed= set()
        
        self.scene.draw(self.canvas)
        
        Clock.schedule_interval(self.move_step,0)
        Clock.schedule_interval(self.update,1/60)
        
        
        
    def conf_player(self):
        ab = Ability(10,10,100,10,10,10,10)
        tab = Tree_Ability()
        texture = AnimationTexture("atlas://assets/character/male1",ANIMATION_HUMAN,CONF_ANIMATION_HUMAN)
        self.player = Character((0,100),(32,32),ab,tab,texture)
        self.scene.register_escene(self.player)
        

    def update(self,dt):
        self.player.update([32,32],dt)
        self.scene.update(size_update(),dt)

        

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_up = self._on_key_up)
        self._keyboard.unbind(on_key_down = self._on_key_down)
        self._keyboard = None
        

    def _on_key_down(self,keyboard,keycode,text,modifiers):
        self.keysPressed.add(keycode[1])
        

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)


    
    def move_step(self,dt):
        self.player.set_animation(False)
        if "w" in self.keysPressed:
            self.player.move("up",Logic.check_collides_solid(self.player,self.scene.get_solid_scene()), dt)
        if "s" in self.keysPressed:
            self.player.move("down",Logic.check_collides_solid(self.player,self.scene.get_solid_scene()),dt)
        if "a" in self.keysPressed:
            self.player.move("left",Logic.check_collides_solid(self.player,self.scene.get_solid_scene()),dt)
        if "d" in self.keysPressed:
            self.player.move("right",Logic.check_collides_solid(self.player,self.scene.get_solid_scene()),dt)
        if "spacebar" in self.keysPressed:
            pass
        

class MyApp(App):

    def build(self):
        Window.fullscreen =False
        Window.size = RESOLUTION["800x600"]
        return Game()


if __name__ == '__main__':
    MyApp().run()


