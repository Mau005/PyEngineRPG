
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from core.Pos_Coordinate import Pos_Coordinate
from core.constantes import MARGE_WIDTH, MARGE_HEIGHT
from items.edges import Edges
from items.grounds import Grounds

Builder.load_file("kv_windows/mapeditor.kv")

from core.list_obj import List_Obj
from kivy.uix.button import Button
from Textures.render import Render
from kivy.clock import Clock

from kivy.uix.popup import Popup

from mapa.mapa import Mapa


def size_update():
    window_x,window_y = Window.size
    return [window_x/MARGE_WIDTH,window_y/MARGE_HEIGHT]

class popMenu(Popup):
    x_obj = ObjectProperty()
    y_obj = ObjectProperty()
    def __init__(self, mapa,**kwargs):
        super().__init__(**kwargs)
        self.auto_dismiss = True
        self.x = 0
        self.y = 0
        self.state = False
        self.mapa = mapa
        
    def exit(self,*args):
        self.dismiss()
        
    def ok(self,*args):
        if int(self.x_obj.text) >= 1 and int(self.y_obj.text) >= 1:  
            a,b = int(self.x_obj.text),int(self.y_obj.text)
            if a > 0 and  b > 0:
                self.x = a
                self.y = b
                self.mapa.asig_map(a,b)
                self.dismiss()
                print(f"Len mapa: {self.mapa.get_len_map()}")
            


class ButtonItems(Button):
    def __init__(self,obj, pincel,**kwargs):
        super().__init__(**kwargs)
        self.obj = obj
        self.pincel = pincel
        self.text = str(self.obj.get_id())
        self.bind(on_release=self.cambio)

    def cambio(self,*Args):
        self.pincel.select = self.obj.get_id()
        
        
class Pincel():
    def __init__(self):
        self.select = None
        self.pincel = None
        self.capa = 0

class Ventana(FloatLayout):
    contenedor_obj = ObjectProperty()
    render = ObjectProperty()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.lista_objetos = List_Obj()
        self.objetos_en_contenedor = []
        self.pincel = Pincel()
        self.organizar_objetos()
        self.scene = Render()
        self.mapa = Mapa()
        self.reference_player = Pos_Coordinate(0,0,0)
        
        self.menu_mapa_tamanio = popMenu(self.mapa)
        Clock.schedule_interval(self.update,1/60)
        Clock.schedule_interval(self.draw,1/60)
        
    def apretar(self,*args):
        self.menu_mapa_tamanio.open()
        
    def draw(self,dt):
        #self.scene.remove_all()
        self.scene.draw(self.render.canvas)
    
    def update(self,dt):
        self.scene.update(size_update(),dt)
        self.scene.draw(self.render.canvas)
        
        if self.menu_mapa_tamanio.state:
            pass

    def __press_touch(self,touch):
        cuadro = size_update()
        x = int(touch.pos[0] / cuadro[0])
        y = int(touch.pos[1] / cuadro[1])


        if self.pincel.select:
            obj_temp = self.lista_objetos.get_id_obj(self.pincel.select, [x * cuadro[0], y * cuadro[1]], cuadro)

            if isinstance(obj_temp, Grounds):
                self.mapa.set_pos(self.reference_player.get_x() + x, self.reference_player.get_y() + y, 0, obj_temp.get_id())
            elif isinstance(obj_temp, Edges):
                self.mapa.set_pos(self.reference_player.get_x() + x, self.reference_player.get_y() + y, 1,
                                  obj_temp.get_id())
            self.scene.register_escene(
                self.lista_objetos.get_id_obj(self.pincel.select, [x * cuadro[0], y * cuadro[1]], cuadro))

    def on_touch_down(self, touch):
        self.__press_touch(touch)
        FloatLayout.on_touch_down(self,touch)
    
    def on_touch_up(self, touch):
        FloatLayout.on_touch_up(self,touch)
    
    def on_touch_move(self, touch):
        self.__press_touch(touch)
        FloatLayout.on_touch_move(self,touch)
        
    def organizar_objetos(self):
        for items in range(1,self.lista_objetos.get_len_obj()):
            contenedor_temp = GridLayout(cols=2)
            obj = self.lista_objetos.get_image(items)
            obj_btn = ButtonItems(obj,self.pincel)
            contenedor_temp.add_widget(obj)
            contenedor_temp.add_widget(obj_btn)
            self.contenedor_obj.add_widget(contenedor_temp)



class MyMapEditor(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ventana = Ventana()
    
    def build(self):
        return Ventana()
    
    
if __name__ == '__main__':
    MyMapEditor().run()
    
    
    