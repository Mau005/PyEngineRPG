

class Tree_Ability():
    def __init__(self) -> None:
        """Oriented class to be able to manage the skills of percentages, 
        among various classes both characters, enemies or game objects
        """
        self._ability_percentage = {"holy":0,
                                    "death":0,
                                    "shield":0,
                                    "earth":0,
                                    "mana_drain":0,
                                    "life_frain":0,
                                    "fire":0,
                                    "poison":0,
                                    "critical":0,
                                    "chance_atk":0,
                                    "distance_atk":0}
        
        
    def normalize_tree_ability(self,obj):
        self._ability_percentage.update(obj.get_ability_percentage())
        
    def get_tree_ability(self):
        return self._ability_percentage
    
    
    def get_tree_ability_unique(self,ability):
        return self._ability_percentage[ability]