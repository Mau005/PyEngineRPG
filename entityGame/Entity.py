from kivy.uix.widget import Widget

from core.Pos_Coordinate import Pos_Coordinate
from core.constantes import CIRC_COLLIDE
from core.Collides import Circ, Punto,Rect


class Entity(Widget):
    def __init__(self,pos,size,ability_base,tree_ability,textura, **kwargs):
        Widget.__init__(self,**kwargs)
        self.pos = pos
        self.size = size
        self._ability_base = ability_base
        self.tree_ability = tree_ability
        self.pos_reference = Pos_Coordinate(0, 0, 0)
        
        with self.canvas:
            self.bg_rect = textura
            
        self.collide_cir = Circ(Punto(pos[0],pos[1]),30)
        
        
    def checl_collide_cir(self,obj):
        return self.collide_cir.collide(obj)
        
    def __gen_size(self,size):
        x,y = size
        return (x+y) * CIRC_COLLIDE
    
    def set_direction_default(self,direction):
        self.bg_rect.set_direction_default(direction)
        
    def get_tree_ability_unique(self,state):
        return self.tree_ability.get_tree_ability_unique(state)
    
    def get_ability_base_unique(self,state):
        return self._ability_base.get_ability_base_unique(state)
        
    def set_solid(self,solid):
        self._solid = solid
        
    def get_solid(self):
        return self._solid
    
    def update(self,size,dt):
        self.size = size
        self.bg_rect.update(self.pos,self.size,dt)
        self.collide_cir.update(self.pos,self.__gen_size(self.size))
    
    
        


