import pygame
import time
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
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()
        
    def test_quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(self.game)
    #1
        self.assertFalse(self.game.running)
        
    def test_starting_game(self):
        self.game = GameInit()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_SPACE}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(self.game)
    #2
        self.assertEqual(self.game.state, 1)
    #3
        self.test_quit()
    #4
        self.assertEqual(self.game.main.x, const.start_x)
    #5
        self.assertEqual(self.game.main.y, const.start_y)
    #6
        self.assertEqual(len(self.game.lives), const.lives_count)
    #7
        self.assertEqual(len(self.game.enemies), const.enemies_count)
    #8
        self.assertEqual(self.game.time, const.start_time)
    #9
        self.assertEqual(self.game.score, 0)
    #10
        self.assertEqual(self.game.state, 1)
    #11
        self.assertEqual(self.game.result, 0)
    #12
        self.assertEqual(self.game.main.vx, 0)
    #13
        self.assertEqual(self.game.main.vy, 0)
        
        for enemy in self.game.enemies:
    #14
            self.assertNotIn(enemy.x, range(const.start_x - self.game.main.img.w, const.start_x + self.game.main.img.w + 1))
    #15
            self.assertNotIn(enemy.y, range(const.start_y - self.game.main.img.h, const.start_y + self.game.main.img.h + 1))
        for i in range(len(self.game.lives)):
    #16
            self.assertEqual((self.game.lives[i].x, self.game.lives[i].y), (const.screen_width - (i + 1) * self.game.lives[i].img.w, 0))

    def test_ending_game(self):
        self.game = GameInit()
        self.game.state = 1
        self.game.result = 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(self.game)
    #17
        self.assertEqual(self.game.state, 2)
        
    def test_win_iscalled_1(self):
        self.game = GameInit()
        self.game.state = 2
        self.game.result = 1
        with mock.patch('utils.win') as mock_win:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            MainLoop(self.game)
    #18
            mock_win.assert_called_with(self.game)
        
    def test_lose_iscalled_2(self):
        self.game = GameInit()
        self.game.state = 2
        self.game.result = -1
        with mock.patch('utils.lose') as mock_lose:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            MainLoop(self.game)
    #19
            mock_lose.assert_called_with(self.game)
            
    def test_win_iscalled_2(self):
        self.game = GameInit()
        self.game.state = 1
        self.game.result = 1
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(self.game)
        
        self.game.running = True
        with mock.patch('utils.win') as mock_win:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            MainLoop(self.game)
    #20
            mock_win.assert_called_with(self.game)
            
    def test_lose_iscalled_2(self):
        self.game = GameInit()
        self.game.state = 1
        self.game.result = -1
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        MainLoop(self.game)
        
        self.game.running = True
        with mock.patch('utils.lose') as mock_lose:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
            MainLoop(self.game)
    #21
            mock_lose.assert_called_with(self.game)

class MovCollisionsTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = GameInit()

    def tearDown(self):
        pygame.quit()

    def test_collision_E(self):
        self.game = GameInit()
        self.game.state = 1
        
        # сдвигаем персонажа в координаты одного из врагов
        index = random.randint(0, const.enemies_count - 1)
        self.game.main.x = self.game.enemies[index].x
        self.game.main.y = self.game.enemies[index].y
        
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
    #22
        self.assertEqual(self.game.lives_count, const.lives_count - 1)
    #23
        self.assertEqual(self.game.lives[self.game.lives_count].img.name, const.blank_life_img)
            
    def test_collision_R(self):
        self.game = GameInit()
        self.game.state = 1
        score = self.game.score
        
        self.game.main.x = self.game.res.x
        self.game.main.y = self.game.res.y
        
        with mock.patch.object(self.game.res, 'regen') as mock_regen:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

            MainLoop(self.game)
    #24
            self.assertEqual(self.game.score, score + 1)
    #25
            mock_regen.assert_called()
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
    #26
        self.assertEqual(self.game.main.x, start_x)
    #27
        self.assertLess(self.game.main.y, start_y)

    def test_key_UP(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_UP}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
    #28
        self.assertEqual(self.game.main.x, start_x)
    #29
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
    #30
        self.assertEqual(self.game.main.x, start_x)
    #31
        self.assertGreater(self.game.main.y, start_y)
        
        
    def test_key_DOWN(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_DOWN}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
    #32
        self.assertEqual(self.game.main.x, start_x)
    #33
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
    #34
        self.assertLess(self.game.main.x, start_x)
    #35
        self.assertEqual(self.game.main.y, start_y)
        
    def test_key_LEFT(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_LEFT}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
    #36
        self.assertLess(self.game.main.x, start_x)
    #37
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
    #38
        self.assertGreater(self.game.main.x, start_x)
    #39
        self.assertEqual(self.game.main.y, start_y)
        
    def test_key_RIGHT(self):
        self.game.restart()
        
        start_x = self.game.main.x
        start_y = self.game.main.y
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN,  {'key': pygame.K_RIGHT}))
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        MainLoop(self.game)
    #40
        self.assertGreater(self.game.main.x, start_x)
    #41
        self.assertEqual(self.game.main.y, start_y)
            
if __name__ == '__main__':
    unittest.main()

#ИТОГО: 54 ПОЗИТИВНЫХ ТЕСТА
