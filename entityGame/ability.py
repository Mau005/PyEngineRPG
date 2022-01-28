#coding: utf-8
#author: mau


from core.constantes import DEFENSE,MELE,SPEED,LIFE,MANA

class Ability():
    
    def __init__(self,defense,mele,speed,life,life_max,mana,mana_max):
        """[summary]

        Args:
            defense (float): It is an ability to determine a percentage aid tho 0.0 - 1.0
            mele (float): It is an ability to determine a percentage aid tho 0.0 - 1.0
            speed (float): It is an ability to determine a percentage aid tho 0.0 - 1.0
            life (int): determines, the more to add to its attribute
            mana (int): determines, the more to add to its attribute
        """
        
        self._base = {"defense":DEFENSE,
                      "mele":MELE,
                      "speed":SPEED,
                      "life":LIFE,
                      "life_max":LIFE,
                      "mana":MANA,
                      "mana_max":MANA}
        
        self._base_human = {"defense":defense,
                            "mele":mele,
                            "speed":speed,
                            "life":life,
                            "life_max":life_max,
                            "mana":mana,
                            "mana_max":mana_max}
        
    def get_ability_base_unique(self,state):
        return self._base_human[state]
    
    def get_ability_base(self):
        return self._base_human
    
    def normalize_ability_base(self,ability_base):
        self._base_human.update(ability_base)