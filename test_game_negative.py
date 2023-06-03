import pygame
from game import Game, GameInit, MainLoop
import unittest
from unittest import mock
import characters
import add
import utils
import constants as const
import random

class MainLoopTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_main_loop_state_0(self):
        
        game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_SPACE}))
        game.result = 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
        
        game.running = True
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #1
        self.assertEqual(game.state, 2)
        
        game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_SPACE}))
        game.result = 1000
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #2
        self.assertEqual(game.state, 1)
    
    def test_keydown_start(self):
        game = GameInit()
        start_x = game.main.x
        start_y = game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #1
        self.assertEqual(start_x, game.main.x)
    #2
        self.assertEqual(start_y, game.main.y)
        pygame.event.post(pygame.event.Event(pygame.KEYUP, {'key': pygame.K_ESCAPE}))
    
    def test_movement(self):
        game = GameInit()
        game.state = 1
        
        start_x = game.main.x
        start_y = game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #1
        self.assertEqual(start_x, game.main.x)
    #2
        self.assertEqual(start_y, game.main.y)
        pygame.event.post(pygame.event.Event(pygame.KEYUP, {'key': pygame.K_ESCAPE}))

    def test_keydown_end(self):
        game = GameInit()
        game.state = 2
        start_x = game.main.x
        start_y = game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_ESCAPE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #1
        self.assertEqual(start_x, game.main.x)
    #2
        self.assertEqual(start_y, game.main.y)
        pygame.event.post(pygame.event.Event(pygame.KEYUP, {'key': pygame.K_ESCAPE}))
    
if __name__ == '__main__':
    unittest.main()

