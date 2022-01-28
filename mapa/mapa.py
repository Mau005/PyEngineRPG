#coding: utf-8
#author: mau

class Mapa():
    """[summary] clase destinada a creacion de mapa
    """
    
    def __init__(self,max_x= 100,max_y= 100,default = False) -> None:
        self.asig_map(max_x,max_y)
        if default:
            self.gen_automatic_map()
            
       
    def gen_automatic_map(self):
        for x in range(0,len(self._mapa)):
            for y in range(0,len(self._mapa[x])):
                self._mapa[x][y].append(1)
                 
        
    def asig_map(self,max_x,max_y):
        self._max_x = max_x
        self._max_y = max_y
        self._mapa = [[[] for y in range(max_y)] for x in range(max_x)]
        
    def get_len_map(self):
        return len(self._mapa)
        
    
        
    
    def get_mapa(self):
        return self._mapa
    
    
    
    def set_pos_obj(self,x,y,capa,obj):
        if len(self._mapa[x][y])>= capa:
            self._mapa[x][y][capa].append(obj)
        else:
            self._mapa[x][y].append(obj)
        
        
        
        
    def set_pos(self,x,y,z,id_obj):
        if len(self._mapa[x][y][z]):
            self._mapa[x][y][z] = id_obj
        
        
    def get_mapa(self):
        return self._mapa
        
        
    def get_pos(self,x,y):
        return self._mapa[x][y][:-1]
    
    def set_pos(self,x,y,obj):
        self._mapa[x][y] = obj
    
        
