import constants as const
import sprites
import random

#a = start_x - characters.Main.img.w
#b = start_x + characters.Main.img.w

#A = start_y + characters.Main.img.h
#B = start_y - characters.Main.img.h

class Main:
    img = sprites.Sprite(const.character_img)
    x = const.start_x
    y = const.start_y
    vx = 0
    vy = 0
    
    def reset(self):
        self.x = const.start_x
        self.y = const.start_y
        #self.vx = 0
        #self.vy = 0
    def regen(self):
        self.reset()
        self.vx = 0
        self.vy = 0
        
class Enemy:
    img = sprites.Sprite(const.enemy_img)
    def __init__(self):
        self.x = random.choice([x for x in range(const.left_border, const.right_border - self.img.w + 1) if x < const.start_x - Main.img.w or x > const.start_x + Main.img.w])
        self.y = random.choice([y for y in range(const.upper_border, const.bottom_border - self.img.h + 1) if y > const.start_y + Main.img.h or y < const.start_y - Main.img.h])
        self.vx = random.randint(-const.enemy_vx, const.enemy_vx)
        self.vy = random.randint(-const.enemy_vy, const.enemy_vy)

    def regen(self):
        if (self.x >= const.start_x - Main.img.w and self.x <= const.start_x + Main.img.w) and (self.y >= const.start_y + Main.img.h and self.y <= const.start_y - Main.img.h):
            x = random.choice([x for x in range(const.left_border, const.right_border - img.w + 1) if x < const.start_x - Main.img.w or x > const.start_x + Main.img.w])
            y = random.choice([y for y in range(const.upper_border, const.bottom_border - img.h + 1) if y > const.start_y + Main.img.h or y < const.start_y - Main.img.h])
    

