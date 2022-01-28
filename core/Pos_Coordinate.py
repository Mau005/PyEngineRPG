#coding: utf-8
#author: mau

class Pos_Coordinate:

    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    def set_pos(self,pos):
        self._x,self._y,self._z = pos

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def get_pos(self):
        return [self._x,self._y,self._z]

    def update_cordinates(self,pos):
        """
        pos [int]: posisiones entre 2 len o 3, para transpasar el sistema del canvas a la matriz
        """
        len_pos = len(pos)
        if len_pos == 2:
            self._x, self._y = pos
        elif len_pos == 3:
            self.set_pos(pos)
