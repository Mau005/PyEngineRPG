from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from Textures.render import Render
Builder.load_file("kv_windows/game.kv")

#constantes;
from core.constantes import ANIMATION_HUMAN,CONF_ANIMATION_HUMAN

#Core del jogo
from entityGame.character import Character
from entityGame.ability import Ability
from entityGame.tree_ability import Tree_Ability
from Textures.AnimationTexture import AnimationTexture
from core.list_obj import List_Obj

#mapa
from mapa.mapa import Mapa

class Game(Screen):
    canvas_render =  ObjectProperty()
    def __init__(self,**kargs):
        Screen.__init__(self,**kargs)
        self.name = "game" #screen del manager, identifica la clase a mostrar
        self.scene = Render()
        self.player = None
        self.state_game = True
        
        
        self.listas_objetos = List_Obj()
        self.init_mapa()
        
        
        Clock.schedule_interval(self.update,1/60)
        Clock.schedule_interval(self.draw,1/60)
        
    def conf_player(self):
        ab = Ability(10,10,100,10,10,10,10)
        tab = Tree_Ability()
        texture = AnimationTexture("atlas://assets/character/male1",ANIMATION_HUMAN,CONF_ANIMATION_HUMAN)
        self.player = Character((0,100),(32,32),ab,tab,texture)
        self.scene.register_escene(self.player)
        
    def init_mapa(self):
        mapa = Mapa(100,100,default = True)
        contenido = mapa.get_mapa()
        cuadro = 32
        
        for x in range(0,len(contenido)):
            for y in range(0,len(contenido[x])):
                self.scene.register_escene(self.listas_objetos.get_id_obj(contenido[x][y][0],[x*cuadro,y*cuadro],[cuadro,cuadro]))
                    
                    
        
    def update(self,dt):
        if self.state_game:
            self.scene.update((32,32),dt)
    
    def draw(self,dt):
        if self.state_game:
            self.scene.draw(self.canvas_render.canvas)
        