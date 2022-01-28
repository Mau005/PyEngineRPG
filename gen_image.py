from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


Builder.load_file("kv_windows/gen_image.kv")

class Ventana(BoxLayout):
    imagen = ObjectProperty()
    botton_search = ObjectProperty()
    
    
    def __init__(self, **kwargs):
        BoxLayout.__init__(self,**kwargs)
        self.orientation= "vertical"
        self.rute = ""
        self.spacing= "20dp"
        
    def right(self):
        num = int(self.ids.num_label.text)
        num +=1
        self.ids.num_label.text = str(num)
        self.__update()
        
    def left(self):
        num = int(self.ids.num_label.text)
        num -=1
        self.ids.num_label.text = str(num)
        self.__update()
        
    def __update(self):
        formato = "atlas://"
        self.imagen.source = f"{formato}{self.rute}/{self.ids.num_label.text}"
        
    def search(self,text,condition = True,*args):
        formato = "atlas://"
        self.rute = text
        if condition:
            self.imagen.source = f"{formato}{self.rute}/{self.ids.num_label.text}"
        else:
            self.imagen.source = f"{formato}{self.rute}/{self.ids.id_search_image.text}"
            self.ids.num_label.text = str(self.ids.id_search_image.text)
        

class App(App):
    def build(self):
        return Ventana()
    
    
if __name__ == '__main__':
    App().run()