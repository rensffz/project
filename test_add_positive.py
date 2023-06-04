import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import pygame
from add import Resource, Life, Environment
import constants as const

class ResourceTestCase(unittest.TestCase):
    def test_init(self):
        with patch('random.choice', return_value=100):
            self.res = Resource()
    #1
        self.assertEqual(self.res.x, 100)
    #2
        self.assertEqual(self.res.x, 100)
    
    def test_regen(self):
        self.res = Resource()
        
        with patch('random.randint', return_value=100):
            self.res.regen()
    #1
        self.assertEqual(self.res.x, 100)
    #2
        self.assertEqual(self.res.x, 100)
        
class LifeTestCase(unittest.TestCase):
    def test_destroy(self):
        self.life = Life()
    #1
        self.assertEqual(self.life.img.name, const.life_img)
        
        self.life.destroy()
    #2
        self.assertEqual(self.life.img.name, const.blank_life_img)


if __name__ == '__main__':
    unittest.main()

#ИТОГО: 6 ПОЗИТИВНЫХ ТЕСТОВ
