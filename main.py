import pygame as pg
import classes as clss
import sys
import random
import pygame_menu as pgm
pg.init()

def draw_block(color, column, row): 
     pg.draw.rect(screen, color,[size_block + column*size_block + margin*(column+1), 
                                        header_margin + size_block + row*size_block + margin*(row+1), 
                                        size_block, 
                                        size_block])

# COLORs
white = (255,255,255)
blue = (204, 255, 255)
bg_color = (73, 77, 78)
header_color = (50, 50, 50)
snake_color = (0,102,0)
food_color = (224, 0,0)
# SIZEs
count_blocks = 20
margin = 1
size_block = 20
header_margin = 70
size = [size_block * count_blocks + 2*size_block + margin*count_blocks,
        size_block * count_blocks + 2*size_block + margin*count_blocks + header_margin]
timer = pg.time.Clock()
screen = pg.display.set_mode(size)
pg.display.set_caption("Змейка")

def start_the_game():
    def get_random_emty_block():
        x = random.randint(0, count_blocks-1)
        y = random.randint(0, count_blocks-1)
        empty_block = clss.SnakeBlock(x,y)

        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, count_blocks-1)
            empty_block.y = random.randint(0, count_blocks-1)
        return empty_block

    snake_blocks=[clss.SnakeBlock(9,9), clss.SnakeBlock(9,10), clss.SnakeBlock(9,11)]
    apple = get_random_emty_block()
    isGame = True
    isCanTurn = True
    direction = {'x':1 , 'y':0}
    courier = pg.font.SysFont('courier', 36)
    speed = 1

    total_points = 0

    while isGame:
        # checking for exit
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isGame = False
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT or event.key == pg.K_d) and direction['y'] != 0 and isCanTurn == True:
                    direction['x'] = 1
                    direction['y'] = 0
                    isCanTurn = False
                elif (event.key == pg.K_LEFT or event.key == pg.K_a) and direction['y'] != 0 and isCanTurn == True:
                    direction['x'] = -1
                    direction['y'] = 0
                    isCanTurn = False
                elif (event.key == pg.K_DOWN or event.key == pg.K_s) and direction['x'] != 0 and isCanTurn == True:
                    direction['x'] = 0
                    direction['y'] = 1
                    isCanTurn = False
                elif (event.key == pg.K_UP or event.key == pg.K_w) and direction['x'] != 0 and isCanTurn == True:
                    direction['x'] = 0
                    direction['y'] = -1
                    isCanTurn = False
            for block in snake_blocks:
                draw_block(snake_color, block.x, block.y)

        screen.fill(bg_color)
        pg.draw.rect(screen, header_color, [0,0,size[0], header_margin])

        # points text
        text_points = courier.render(f"Очков:{total_points}", 0, white)
        screen.blit(text_points, (size_block, size_block))

        # speed text
        text_speed = courier.render(f"Скорость:{int(speed)}", 0, white)
        screen.blit(text_speed, (size_block + 200, size_block))

        for row in range(count_blocks):
            for column in range(count_blocks):
                color = white if (column+row)%2==0 else blue
                draw_block(color, column, row)
        draw_block(food_color, apple.x, apple.y)
        
        head = snake_blocks[-1]
        if not head.IsInside(size_block):
            # sys.exit()
            break

        for block in snake_blocks:
            draw_block(snake_color, block.x, block.y)
        
        if apple.x == head.x and apple.y == head.y:
            total_points += 1
            speed = total_points/5 + 1
            snake_blocks.append(apple)
            apple = get_random_emty_block()

        head = snake_blocks[-1]
        new_head = clss.SnakeBlock(head.x + direction['x'], head.y + direction['y'])

        if new_head in snake_blocks:
            print("crash yourself")
            # pg.quit()
            # sys.exit()
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)
        
        # redrawing of display
        pg.display.flip()
        isCanTurn = True
        timer.tick(3 + speed)


menu = pgm.Menu('Welcome', size[0], size[1], theme = pgm.themes.THEME_DARK)
menu.add.text_input('Хто ты, воин?: ', default = 'Игрок 1')
menu.add.button('Плау', start_the_game)
menu.add.button('Выход', pgm.events.EXIT)


menu.mainloop(screen)                