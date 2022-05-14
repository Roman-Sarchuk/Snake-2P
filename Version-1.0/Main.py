import pygame as py
# my import
import Attribute
import Engine

# --- Create display ---
py.init()
screen = py.display.set_mode(Attribute.ATTRIBUTE().scr_size)
py.display.update()
py.display.set_caption('Snake')
# ----------------------

FPS = 50
engine = Engine.ENGINE(screen)
engine.create_display()
engine.spawn_snake()

game = True
while game:
    for event in py.event.get():
        if event.type == py.QUIT or event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
            game = False

        if event.type == py.KEYDOWN:
            # Move: forward, backward, left, right
            # snake 1
            if event.key == py.K_w and engine.get_way('snake1') != 'backward':
                engine.set_way('snake1', 'forward')
            elif event.key == py.K_s and engine.get_way('snake1') != 'forward' \
                    and engine.get_way('snake1') is not None:
                engine.set_way('snake1', 'backward')
            elif event.key == py.K_a and engine.get_way('snake1') != 'right':
                engine.set_way('snake1', 'left')
            elif event.key == py.K_d and engine.get_way('snake1') != 'left':
                engine.set_way('snake1', 'right')
            # snake 2
            if event.key == py.K_UP and engine.get_way('snake2') != 'backward' \
                    and engine.get_way('snake1') is not None:
                engine.set_way('snake2', 'forward')
            elif event.key == py.K_DOWN and engine.get_way('snake2') != 'forward':
                engine.set_way('snake2', 'backward')
            elif event.key == py.K_LEFT and engine.get_way('snake2') != 'right':
                engine.set_way('snake2', 'left')
            elif event.key == py.K_RIGHT and engine.get_way('snake2') != 'left':
                engine.set_way('snake2', 'right')

    py.time.wait(FPS)
    end = engine.check_end()
    if end != 'lost1' and end != 'lost2':
        engine.spawn_apple()
        py.time.wait(150)
        engine.snake_move()
    else:
        engine.message(end[-1])

    py.display.flip()

py.quit()
