from items.items import Items



class Edges(Items):
    
    def __init__(self,id_obj,name,descr,weight,texture,solid,**kargs):
        Items.__init__(self,id_obj,name,descr,weight,texture,solid,**kargs)
    
    def update(self,size,dt):
        super().update(size,dt)
    