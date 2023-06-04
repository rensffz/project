import pygame
from game import Game, GameInit, MainLoop
import unittest
from unittest import mock
import characters
import add
import utils
import constants as const
import random

class MovUp(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()
        
    def test_key_W(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_w}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
                
        self.assertEqual(self.game.main.x, start_x)
        self.assertLess(self.game.main.y, start_y)

    def test_key_UP(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_UP}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertEqual(self.game.main.x, start_x)
        self.assertLess(self.game.main.y, start_y)
        
class MovDown(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()

    def test_key_S(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_s}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertEqual(self.game.main.x, start_x)
        self.assertGreater(self.game.main.y, start_y)
        
        
    def test_key_DOWN(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_DOWN}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertEqual(self.game.main.x, start_x)
        self.assertGreater(self.game.main.y, start_y)
        
        
class MovLeft(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()

    def test_key_A(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_a}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertLess(self.game.main.x, start_x)
        self.assertEqual(self.game.main.y, start_y)
        
    def test_key_LEFT(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_LEFT}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertLess(self.game.main.x, start_x)
        self.assertEqual(self.game.main.y, start_y)
        
class MovRight(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()

    def test_key_D(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_d}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertGreater(self.game.main.x, start_x)
        self.assertEqual(self.game.main.y, start_y)
        
    def test_key_RIGHT(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_RIGHT}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
        
        self.assertGreater(self.game.main.x, start_x)
        self.assertEqual(self.game.main.y, start_y)

if __name__ == '__main__':
    unittest.main()
