class Logic():
    
    @classmethod
    def collides(cls,character,enemy):
        r1x = character.pos[0]
        r1y = character.pos[1]
        r2x = enemy.pos[0]
        r2y = enemy.pos[1]
        r1w = character.size[0]- cls.normalize_size(character,.2)[0]
        r1h = character.size[1] - cls.normalize_size(character,.2)[1]
        r2w = enemy.size[0]
        r2h = enemy.size[1]
        
        if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False

    @classmethod        
    def check_collides_solid(cls,character,colicion_scene):
        for obj in colicion_scene:
            result = cls.collides(character,obj) 
            if result:
                return True
            else:
                continue
        return False
    
    
    @classmethod
    def momevements_percentage(cls,size):
        a = round(size[0]*.1,2)
        b = round(size[1]*.1,2)
        return [a,b]
    
    
    @classmethod
    def normalize_size(cls,character,porce):
        if porce >= 0.0 and porce <= 1:
            return [(character.size[0] * porce),(character.size[1] * porce)]
        return character.size