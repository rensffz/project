import unittest
import pygame
from sprites import Sprite

class SpriteTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        sprite_path = 'assets/character.png'
        sprite = Sprite(sprite_path)
    #1
        self.assertEqual(sprite.name, sprite_path)
    #2
        self.assertIsInstance(sprite.sprite, pygame.Surface)
    #3
        self.assertEqual(sprite.w, sprite.sprite.get_width())
    #4
        self.assertEqual(sprite.h, sprite.sprite.get_height())

if __name__ == '__main__':
    unittest.main()
    
#ИТОГО: 4 ПОЗИТИВНЫХ ТЕСТА
