class Control():
    
    def __init__(self,size) -> None:
        self.height = size[1]
        self.width = size[0]
        self._state_display = {"x":800,"y":600}
        self._state = False
        
        
        
    def set_size(self,w,h):
        self.height = h
        self.width = w
        
    def get_state(self):
        return self._state
    
    def set_state(self,state):
        if isinstance(state,bool):
            self._state =state
        else:
            print("No Cambio el estado de tu hermana")
    
        
        
    def update(self,size):
        self._state = self.__check_size(size) 
    
    def __check_size(self,size):
        
        if size[0] == self.width and size[1] == self.height:
            print("retorna faail")
            return False
        print("retorna true")
        return True
        
    def get_size(self):
        return [self.width,self.height]