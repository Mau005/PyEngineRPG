#coding: utf-8
#author: mau

    
from kivy.graphics import Rectangle


class Simple_Texture(Rectangle):
    
    def __init__(self,ruta, **kwargs):
        Rectangle.__init__(self,**kwargs)
        self.set_ruta(ruta)
        self.set_animation(False)
        try:
            self.source = ruta
        except:
            self.source = ""
        
    def set_animation(self,anim):
        self._animation = anim

    def get_ruta(self):
        return self._ruta
    
    def set_ruta(self,ruta):
        self._ruta = ruta
        
    def update(self,pos,size):
        self.pos = pos
        self.size = size
        