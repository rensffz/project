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
        self.main.x = 123456789
        self.main.y = 987654321
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
    
        self.main.x = 10**5
        self.main.y = 10**7
        self.main.vx = 1000
        self.main.vy = -1000
        self.main.regen()
    #1
        self.assertEqual(self.main.x, const.start_x)
    #2
        self.assertEqual(self.main.y, const.start_y)
    #3
        self.assertEqual(self.main.vx, 0)
    #4
        self.assertEqual(self.main.vy, 0)
        
if __name__ == '__main__':
    unittest.main()
    
