import constants as const
import sprites
import random

#a = start_x - characters.Main.img.w
#b = start_x + characters.Main.img.w

#A = start_y + characters.Main.img.h
#B = start_y - characters.Main.img.h

class Main:
    img = sprites.Sprite(const.character_img)
    
    def __init__(self):
        self.x = const.start_x
        self.y = const.start_y
        self.vx = 0
        self.vy = 0
    
    def reset(self):
        self.x = const.start_x
        self.y = const.start_y
    def regen(self):
        self.reset()
        self.vx = 0
        self.vy = 0
        
class Enemy:
    img = sprites.Sprite(const.enemy_img)
    def __init__(self):
        self.x = random.choice([x for x in range(const.left_border, const.right_border - self.img.w + 1) if x < const.start_x - Main.img.w - self.img.w or x > const.start_x + Main.img.w + self.img.w])
        self.y = random.choice([y for y in range(const.upper_border, const.bottom_border - self.img.h + 1) if y > const.start_y + Main.img.h + self.img.h or y < const.start_y - Main.img.h - self.img.h])
        self.vx = random.randint(1, const.enemy_vx) * random.choice([-1, 1])
        self.vy = random.randint(1, const.enemy_vy) * random.choice([-1, 1])

    def regen(self):
        if (self.x >= const.start_x - Main.img.w - self.img.w and self.x <= const.start_x + Main.img.w + self.img.w) and (self.y <= const.start_y + Main.img.h + self.img.h and self.y >= const.start_y - Main.img.h - self.img.h):
            self.x = random.choice([x for x in range(const.left_border, const.right_border - self.img.w + 1) if x < const.start_x - Main.img.w or x > const.start_x + Main.img.w])
            self.y = random.choice([y for y in range(const.upper_border, const.bottom_border - self.img.h + 1) if y > const.start_y + Main.img.h or y < const.start_y - Main.img.h])
    

