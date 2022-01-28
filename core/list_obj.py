from items.edges import Edges
from items.grounds import Grounds
from kivy.uix.image import Image

from Textures.Simple_Texture import Simple_Texture


class ImageMapEditor(Image):
    
    def __init__(self, id_obj, **kwargs):
        super().__init__(**kwargs)
        self.id_obj = id_obj
        
    def get_id(self):
        return self.id_obj

class List_Obj():
    def __init__(self):
        """[if weight is None, it means that the object cannot be moved]
        """
        self._list_obj = {}
        
        self._len_obj = 0
        
        #"1":{"id": ,"name": ,"ruta": ,"descr": ,"weight": ,"class": ,"solid":}
        self._register_items()
        
    def get_len_obj(self):
        return self._len_obj
        
    def _register_items(self):
        self.gen_items_cant("rock","atlas://assets/scene/enviroment_green.atlas/","rock",None,"edges",True,(1,15),1)
        self.gen_items_cant("pasture","atlas://assets/scene/enviroment_green.atlas/","pasture",None,"grounds",False,(15,18),15)
        
    def gen_items_cant(self,name,ruta,descr,weight,clase,solid,range_item,id_init):
        min, max = range_item
        ruta_tem = ruta
        id_init_tem = id_init
        for items in range(min,max):
            self._list_obj.update({str(id_init_tem):{"id": id_init_tem,"name": name,"ruta": ruta+str(items),"descr": descr,"weight": weight,"class": clase,"solid":solid}})
            id_init_tem+=1
        self._len_obj = id_init_tem
        
    def get_image(self,id_image):
        obj = self._list_obj[str(id_image)]
        return ImageMapEditor(id_image,source= obj["ruta"])
            
    def get_id_obj(self,id_obj,pos,size):
        obj = self._list_obj[str(id_obj)]
        
        if obj["class"] == "grounds":
            return Grounds(obj["id"],obj["name"],obj["descr"],obj["weight"],Simple_Texture(obj["ruta"]),obj["solid"],pos = pos, size = size)
        elif obj["class"] == "edges":
            return Edges(obj["id"],obj["name"],obj["descr"],obj["weight"],Simple_Texture(obj["ruta"]),obj["solid"],pos = pos, size = size)
    
     