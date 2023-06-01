import pygame
import game
import constants as const

def start(game):

    greet_texts_arr = ['hi!', 'in this game you need to collect',  '{} carrots without running into enemies'.format(const.res_count), 'for the allotted time.',
    '', 'to control the character', 'you can use arrow keys or W,A,S,D keys', 'good luck!']
    game.screen.fill(const.bg)
    clue = game.font.render('press SPACE to play', True, (255, 255, 255))
    tw, th = game.font.size('press SPACE to play')
    game.screen.blit(clue, ((const.screen_width // 2) - (tw // 2) , const.screen_height - th))
    for i in range(len(greet_texts_arr)):
        prnt = game.font.render(greet_texts_arr[i], True, (0, 0, 0))
        game.screen.blit(prnt, (0, i * const.font_size))
    pygame.display.update()
    
def draw(game):

    game.screen.fill(const.bg)
    game.screen.blit(game.main.img.sprite, (game.main.x, game.main.y))

    game.screen.blit(game.res.img.sprite, (game.res.x, game.res.y))
    
    for life in game.lives:
        game.screen.blit(life.img.sprite, (life.x, life.y))
        
    for enemy in game.enemies:
        game.screen.blit(enemy.img.sprite, (enemy.x, enemy.y))
        
    game.screen.blit(game.env.time_text, (0, 0))
    game.screen.blit(game.env.score_text, (0, const.font_size))
    pygame.display.update()
    
def win(game):
    game.screen.fill(const.bg)
    clue = game.font.render('press SPACE to play again', True, (255, 255, 255))
    clue_tw, clue_th = game.font.size('press SPACE to play again')
    game.screen.blit(clue, ((const.screen_width // 2) - (clue_tw // 2) , const.screen_height - clue_th))
    congrats = game.font.render('congratulations! you won', True, (0, 0, 0))
    tw, th = game.font.size('congratulations! you won')
    game.screen.blit(game.env.time_text, (0, 0))
    game.screen.blit(congrats, (const.screen_width // 2 - (tw // 2), const.screen_height // 2 - th))
    pygame.display.update()

def lose(game):
    game.screen.fill(const.bg)
    texts = ['unfortunately, you lost!', 'do you want to try again?']
    clue = game.font.render('press SPACE to try again', True, (255, 255, 255))
    tw, th = game.font.size('press SPACE to try again')
    game.screen.blit(clue, ((const.screen_width // 2) - (tw // 2) , const.screen_height - th))
    
    for i in range(len(texts)):
        w, h = game.font.size(texts[i])
        prnt = game.font.render(texts[i], True, (0, 0, 0))
        game.screen.blit(prnt, (0, i * const.font_size))
    pygame.display.update()
