import pygame as pg
from Container import ContApple
import Engine

# init pygame
pg.init()
pg.display.update()
pg.display.set_caption('Snake')

FPS = 200
engine = Engine.ENGINE()
engine.create_display()
engine.spawn_snake()
engine.spawn_apple(ContApple.count_apple)

run = True
while run or run is None:
    pg.time.wait(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            run = False

        if event.type == pg.KEYDOWN:
            # restart
            if event.key == pg.K_RETURN and run is None:
                run = True
                engine.restart()

            if run:
                # snake 1
                snake_way1 = engine.get_way('snake1')
                if event.key == pg.K_w and snake_way1 != 'backward':
                    engine.set_way('snake1', 'forward')
                elif event.key == pg.K_s and snake_way1 != 'forward' and snake_way1 is not None:
                    engine.set_way('snake1', 'backward')
                elif event.key == pg.K_a and snake_way1 != 'right':
                    engine.set_way('snake1', 'left')
                elif event.key == pg.K_d and snake_way1 != 'left':
                    engine.set_way('snake1', 'right')
                # snake 2
                snake_way2 = engine.get_way('snake2')
                if event.key == pg.K_UP and snake_way2 != 'backward' and snake_way2 is not None:
                    engine.set_way('snake2', 'forward')
                elif event.key == pg.K_DOWN and snake_way2 != 'forward':
                    engine.set_way('snake2', 'backward')
                elif event.key == pg.K_LEFT and snake_way2 != 'right':
                    engine.set_way('snake2', 'left')
                elif event.key == pg.K_RIGHT and snake_way2 != 'left':
                    engine.set_way('snake2', 'right')

    if run:
        engine.snake_move()
        if engine.check_end() == 'lost1' or engine.check_end() == 'lost2':
            run = None
            engine.message(engine.check_end()[-1])

    pg.display.flip()

pg.quit()
