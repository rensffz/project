import unittest
import pygame
from sprites import Sprite

class SpriteTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        sprite_path = 'invalid/path/character.png'
    #1
        with self.assertRaises(FileNotFoundError):
            sprite = Sprite(sprite_path)

if __name__ == '__main__':
    unittest.main()
