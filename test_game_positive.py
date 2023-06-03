import pygame
from game import Game, GameInit, MainLoop
import unittest
from unittest import mock
import characters
import add
import utils
import constants as const
import random

class RestartTestCase(unittest.TestCase):
    def setUp(self):
        self.game = GameInit()

    def test_restart(self):
        self.game.restart()
        
    #1
        self.assertEqual(len(self.game.lives), const.lives_count)
    #2
        self.assertEqual(len(self.game.enemies), const.enemies_count)
    #3
        self.assertEqual(self.game.time, const.start_time)
    #4
        self.assertEqual(self.game.score, 0)
    #5
        self.assertEqual(self.game.state, 1)
    #6
        self.assertEqual(self.game.result, 0)
    #7
        self.assertEqual(self.game.main.x, const.start_x)
    #8
        self.assertEqual(self.game.main.y, const.start_y)
    #9
        self.assertEqual(self.game.main.vx, 0)
    #10
        self.assertEqual(self.game.main.vy, 0)
        for enemy in self.game.enemies:
    #11
            self.assertNotIn(enemy.x, range(const.start_x - self.game.main.img.w, const.start_x + self.game.main.img.w + 1))
    #12
            self.assertNotIn(enemy.y, range(const.start_y - self.game.main.img.h, const.start_y + self.game.main.img.h + 1))
        for i in range(len(self.game.lives)):
    #13
            self.assertEqual((self.game.lives[i].x, self.game.lives[i].y), (const.screen_width - (i + 1) * self.game.lives[i].img.w, 0))


class MainLoopTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_main_loop_state_0(self):
        game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #1
        self.assertFalse(game.running)
        
        game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_SPACE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #2
        self.assertEqual(game.state, 1)
    #3
        self.assertFalse(game.running)

    def test_start(self):
        game = GameInit()
        game.restart()
    
    
        game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_SPACE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
        
    #4
        self.assertEqual(game.main.x, const.start_x)
    #5
        self.assertEqual(game.main.y, const.start_y)
    #6
        self.assertEqual(len(game.lives), game.lives_count)
    #7
        self.assertEqual(len(game.lives), const.lives_count)
    #8
        self.assertEqual(game.lives_count, const.lives_count)
    #9
        self.assertEqual(len(game.enemies), const.enemies_count)
    #10
        self.assertEqual(game.time, const.start_time)
    #11
        self.assertEqual(game.score, 0)
    #12
        self.assertEqual(game.state, 1)
    #13
        self.assertEqual(game.result, 0)
    #14
        self.assertEqual(game.main.vx, 0)
    #15
        self.assertEqual(game.main.vy, 0)
        
        for enemy in game.enemies:
    #16
            self.assertNotIn(enemy.x, range(const.start_x - game.main.img.w, const.start_x + game.main.img.w + 1))
    #17
            self.assertNotIn(enemy.y, range(const.start_y - game.main.img.h, const.start_y + game.main.img.h + 1))
        for i in range(len(game.lives)):
    #18
            self.assertEqual((game.lives[i].x, game.lives[i].y), (const.screen_width - (i + 1) * game.lives[i].img.w, 0))

    def test_collision_E(self):
        game = GameInit()
        game.state = 1
        
        # сдвигаем персонажа в координаты одного из врагов
        index = random.randint(0, const.enemies_count - 1)
        game.main.x = game.enemies[index].x
        game.main.y = game.enemies[index].y
        
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(game)
    #19
        self.assertEqual(game.lives_count, const.lives_count - 1)
    #20
        self.assertEqual(game.lives[game.lives_count].img.name, const.blank_life_img)
            
    def test_collision_R(self):
        game = GameInit()
        game.state = 1
        score = game.score
        
        game.main.x = game.res.x
        game.main.y = game.res.y
        
        with mock.patch.object(game.res, 'regen') as mock_regen:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

            MainLoop(game)
    #21
            self.assertEqual(game.score, score + 1)
    #22
            mock_regen.assert_called_once_with()
            
    def test_ending_win(self):
        game = GameInit()
        game.state = 1
        game.result = 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(game)
    #23
        self.assertEqual(game.state, 2)

if __name__ == '__main__':
    unittest.main()
