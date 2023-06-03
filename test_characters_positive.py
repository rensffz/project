import unittest
from unittest.mock import patch
import constants as const
import sprites
import random
from characters import Main, Enemy


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    def test_reset(self):
        prev_vx = self.main.vx
        prev_vy = self.main.vy
        self.main.reset()
    #1
        self.assertEqual(self.main.x, const.start_x)
    #2
        self.assertEqual(self.main.y, const.start_y)
    #3
        self.assertEqual(self.main.vx, prev_vx)
    #4
        self.assertEqual(self.main.vy, prev_vy)

    def test_regen(self):
    
        self.main.regen()
    #1
        self.assertEqual(self.main.x, const.start_x)
    #2
        self.assertEqual(self.main.y, const.start_y)
    #3
        self.assertEqual(self.main.vx, 0)
    #4
        self.assertEqual(self.main.vy, 0)
        
class EnemyTestCase(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy()

    def test_regen(self):
        
        main = Main()
        self.enemy.x = main.x
        self.enemy.y = main.y
        original_x = self.enemy.x
        original_y = self.enemy.y
        with patch('random.choice', return_value=100):
            self.enemy.regen()
    #1
        self.assertNotEqual(self.enemy.x, original_x)
    #2
        self.assertNotEqual(self.enemy.y, original_y)
    #3
        self.assertEqual(self.enemy.x, 100)
    #4
        self.assertEqual(self.enemy.y, 100)
        
if __name__ == '__main__':
    unittest.main()
    
