#coding: utf-8
#author: mau
from kivy.uix.widget import Widget

from core.Pos_Coordinate import Pos_Coordinate

class Items(Widget):
    def __init__(self,id_obj,name,descr,weight,texture,solid,**kargs):
        """[summary]
        Args:
            name ([str]): [description]
            descr ([str]): [description]
            weight ([None-Float]): [description]
            texture ([Simple_Texture-AnimationTexture]): [description]
            solid ([Bool]): [description]
        """
        Widget.__init__(self,**kargs)
        self._id_obj = id_obj
        self._name = name
        self._descr = descr
        self._weight = weight
        self.set_solid(solid)
        self.size_hint= (None,None)
        self.pos_reference = Pos_Coordinate(0,0,0)
        
        with self.canvas:
            self.bg_rect = texture
            
    def update(self,size,dt):
        self.size = size
        self.bg_rect.update(self.pos,self.size)
        
    def draw(self,pos,size):
        pass
    
         
    def get_id(self):
        return self._id_obj
    
    def set_solid(self,solid):
        self._solid = solid
        
    def get_solid(self):
        return self._solid