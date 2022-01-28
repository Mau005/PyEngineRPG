#coding: utf-8
#author: mau

from entityGame.Entity import Entity
from core.logic import Logic


class Character(Entity):
    def __init__(self,pos,size,ability_base,tree_ability,textura,**kargs):
        Entity.__init__(self,pos,size,ability_base,tree_ability,textura,**kargs)
        self._solid = True
        self._conteo_pasos = []
        
        
    def set_animation(self,state):
        self.bg_rect.set_animation(state)

    def update(self,size,dt):
        super().update(size,dt)

        
    def move(self,direction,check,dt):
        self.set_direction_default(direction)
        currentx = self.pos[0]
        currenty = self.pos[1]
        prueba = self.get_ability_base_unique("speed")*dt
        
        moving_x= (self.get_ability_base_unique("speed")+Logic.momevements_percentage(self.size)[0] )* dt
        moving_y = (self.get_ability_base_unique("speed")+Logic.momevements_percentage(self.size)[1]) *dt
        
        ultimo_movimiento = [currentx,currenty]
        
        self._check_pasos(ultimo_movimiento)
        if not check:
            self.set_animation(True)
            if direction  == "up":
                currenty+=moving_y
            if direction == "down":
                currenty-=moving_y
            if direction == "left":
                currentx-=moving_x
            if direction == "right":
                currentx+=moving_x
            self.pos=(currentx,currenty)
            
        else:
            if len(self._conteo_pasos) >= 2:
                self.pos=(self._conteo_pasos[-2])
        
        
        
    def _check_pasos(self,paso):
        if len(self._conteo_pasos) >= 30:
            self._conteo_pasos.pop(0)
            self._conteo_pasos.append(paso)
        else:
            self._conteo_pasos.append(paso)
        
    