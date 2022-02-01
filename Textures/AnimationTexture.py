from Textures.Simple_Texture import Simple_Texture
from core.constantes import RATE_TIME_ANIMATION

class AnimationTexture(Simple_Texture):


    def __init__(self,ruta,direction,conf_animation, **kwargs):
        Simple_Texture.__init__(self,ruta,**kwargs)
        self._direction = direction
        self._direction_default = conf_animation["direction_default"]
        self.set_animation(conf_animation["animation"])
        self._frame = conf_animation["frame_init"]
        self._frame_default = conf_animation["frame_default"]
        self._rate = RATE_TIME_ANIMATION
        self._estado = 0
        self.time = 0.0
        
        
    def get_animation(self):
        return self._animation
    
    def set_direction_default(self,direction):
        self._direction_default = direction
    
    def set_animation(self,anim):
        self._animation = anim

    def update(self,pos,size,dt):
        super().update(pos,size)
        self.time += dt
        if self.get_animation():
            self.source = f"{self.get_ruta()}/{str(self._frame)}"
        else:
            self.source = f"{self.get_ruta()}/{self._direction[self._direction_default][self._frame_default]}"
        if (self.time > self._rate):
            self.time -= self._rate
            self._frame = self._direction[self._direction_default][self._estado]
            self._estado +=1
            if (self._estado > 2):
                self._estado = 0