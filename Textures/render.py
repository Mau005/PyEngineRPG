# coding: utf-8
# author: mau
from entityGame.Entity import Entity
from items.items import Items
from entityGame.character import Character
from core.Pos_Coordinate import Pos_Coordinate


class Render:

    def __init__(self):
        self._scene = {"1": [], "2": [], "3": [], "4": [], "solid": [], "solid_entity": []}
        self.pos_reference = Pos_Coordinate(0, 0, 1)

    def remove_obj_scene(self, obj, lvl_cape):
        self._scene[lvl_cape].remove(obj)

    def get_scena(self):
        return self._scene

    def get_solid_scene(self):
        return self._scene["solid"]

    def update(self, size_update, dt):
        for elements in range(1, 5):
            for obj in self._scene[str(elements)]:
                obj.update(size_update,dt)

    def __check_solid(self, obj):
        """[summary]
            clase enfrentada a revisar si los objetos son colicionables con el personaje principal
        Args:
            obj ([type]): [description]
        """
        if obj.get_solid() and not isinstance(obj, Character):
            self._scene["solid"].append(obj)

    def register_escene(self, obj_scene):
        if isinstance(obj_scene, Entity):
            self._scene["3"].append(obj_scene)
            self._scene["solid_entity"].append(obj_scene)

        if isinstance(obj_scene, Items):
            self._scene["1"].append(obj_scene)
        self.__check_solid(obj_scene)

    def remove_all(self):
        self._scene.clear()
        self._scene = {"1": [], "2": [], "3": [], "4": [], "solid": [], "solid_entity": []}

    def draw(self, canvas):
        canvas.clear()
        for index in range(1, 5):
            for elements in self._scene[str(index)]:
                canvas.add(elements.bg_rect)
