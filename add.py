import random
import characters
import constants as const
import sprites

#a = start_x - characters.Main.img.w
#b = start_x + characters.Main.img.w

#A = start_y + characters.Main.img.h
#B = start_y - characters.Main.img.h

# Условие генерации:
# (x < a or x > b) and (y > A or y < B)
        
class Resource:
    img = sprites.Sprite(const.resource_img)
    
    def __init__(self):
        self.x = random.choice([x for x in range(const.left_border, const.right_border - self.img.w + 1) if x < const.start_x - characters.Main.img.w or x > const.start_x + characters.Main.img.w])
        self.y = random.choice([y for y in range(const.upper_border, const.bottom_border - self.img.h + 1) if y > const.start_y + characters.Main.img.h or y < const.start_y - characters.Main.img.h])

    def regen(self):
        self.x = random.randint(const.left_border, const.right_border - self.img.w)
        self.y = random.randint(const.upper_border, const.bottom_border - self.img.h)

class Life:
    img = sprites.Sprite(const.life_img)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def destroy(self):
        self.img = sprites.Sprite(const.blank_life_img)
        
class Environment:
    def __init__(self, time_text, score_text):
        self.time_text = time_text
        self.score_text = score_text
        
