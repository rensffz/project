import pygame
import characters
import add
import utils
import constants as const

class Game():
    
    main = characters.Main()

    res = add.Resource()

    lives = [add.Life(const.screen_width - (i + 1) * add.Life.img.w, 0) for i in range(const.lives_count)]

    enemies = [characters.Enemy() for i in range(const.enemies_count)]

    time = const.start_time
    score = 0
    lives_count = const.lives_count
    state = 0
                #0 - стартовое положение
                #1 - основной процесс
                #2 - конец

    result = 0
    
    def restart(self):
        self.main.regen()
        self.lives = [add.Life(const.screen_width - (i + 1) * add.Life.img.w, 0) for i in range(const.lives_count)]
        self.enemies = [characters.Enemy() for i in range(const.enemies_count)]
        self.time = const.start_time
        self.score = 0
        self.lives_count = const.lives_count
        self.state = 1
        self.result = 0
    
def GameInit():
    global screen, font, Timer, game
    
    pygame.init()
    game = Game()
    game.screen = pygame.display.set_mode((const.screen_width, const.screen_height))
    game.font = pygame.font.Font(const.font, const.font_size)
    game.timer = pygame.time.Clock()
    
def MainLoop():
    global game, screen, font, Timer
    
    running = True
    while running:
        match game.state:
            case 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key ==pygame.K_SPACE:
                            game.state += 1
                utils.start(game)
            case 1:
                game.timer.tick(60)
                
                game.time -= game.timer.get_time() / 1000
                
                time_text = game.font.render("Time: {:02d}:{:02d}".format(int(game.time) // 60, int(game.time) % 60), True, (0, 0, 0))
                score_text = game.font.render("Score: {:02d}".format(game.score), True, (0, 0, 0))
                
                game.env = add.Environment(time_text, score_text)
                
                
                
                # обработка ввода с клавиатуры
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            game.main.vx -= const.character_vx
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            game.main.vx += const.character_vx
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            game.main.vy -= const.character_vy
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            game.main.vy += const.character_vy
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            game.main.vx += const.character_vx
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            game.main.vx -= const.character_vx
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            game.main.vy += const.character_vy
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            game.main.vy -= const.character_vy
                
                if (game.main.x + game.main.vx >= const.left_border) and (game.main.x + game.main.vx <= const.right_border - game.main.img.w):
                    game.main.x += game.main.vx
                if (game.main.y + game.main.vy >= const.upper_border) and (game.main.y + game.main.vy <= const.bottom_border - game.main.img.h):
                    game.main.y += game.main.vy
                    
                for i in range(const.enemies_count):
                
                    if (game.enemies[i].x + game.enemies[i].vx >= const.left_border) and (game.enemies[i].x + game.enemies[i].vx <= const.right_border - game.enemies[i].img.w):
                        game.enemies[i].x += game.enemies[i].vx
                    else:
                        game.enemies[i].x -= game.enemies[i].vx
                        game.enemies[i].vx *= -1
                        
                    if (game.enemies[i].y + game.enemies[i].vy >= const.upper_border) and (game.enemies[i].y + game.enemies[i].vy <= const.bottom_border - game.enemies[i].img.h):
                        game.enemies[i].y += game.enemies[i].vy
                    else:
                        game.enemies[i].y -= game.enemies[i].vy
                        game.enemies[i].vy *= -1
                        
                if (game.main.x + game.main.img.w >= game.res.x and game.main.x <= game.res.x + game.res.img.w) and (game.main.y + game.main.img.h >= game.res.y and game.main.y <= game.res.y + game.res.img.h):
                    game.score += 1
                    game.res.regen()
                    
                    if game.score == const.res_count:
                        game.main.reset()
                        game.result = 1
                        game.state += 1

                for i in range(const.enemies_count):
                
                    if game.main.x + game.main.img.w >= game.enemies[i].x and game.main.x <= game.enemies[i].x + game.enemies[i].img.w and game.main.y + game.main.img.h >= game.enemies[i].y and game.main.y <= game.enemies[i].y + game.enemies[i].img.h:
                        game.lives_count -= 1
                        game.lives[game.lives_count].destroy()
                        game.main.reset()
                        for j in range(const.enemies_count):
                            game.enemies[j].regen()
                        
                        if game.lives_count == 0:
                            game.result = -1
                            game.state += 1
                            
                if game.time <= 0:
                    game.state += 1
                            
                utils.draw(game)


            case 2:
                if game.result == 1:
                    utils.win(game)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game.restart()
                        
                else:
                    utils.lose(game)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                game.restart()

