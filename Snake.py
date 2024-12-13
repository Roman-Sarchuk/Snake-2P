import pygame as pg
from Container import CombWindow, ContNet, NetCharacter, ContSnakeSpawn, ContColor


class SNAKE(CombWindow, ContNet, NetCharacter, ContSnakeSpawn, ContColor):
    def __init__(self):
        # snake
        self._snake_dict = {'cord': [], 'status': []}
        self.__color_head = self.BLACK
        self.__color_body = self.WIGHT
        self._eaten_apple = 0
        self._eat = False
        self._lost = False

    def set_color(self, color_head, color_body):
        """*** Set color snake ***

        :param color_head: ( RGB )
        :param color_body: ( RGB )"""
        self.__color_body = color_body
        self.__color_head = color_head

    # --- draw ---
    def __clear(self, old_cord):
        """*** Cleaning the old snake ***

        :param old_cord: cord of where the snake is now"""
        for cord in old_cord:
            self.net['status'][cord[0]][cord[1]] = '-'
            block = self.net['cord'][cord[0]][cord[1]]
            clear = pg.Rect(block['x'], block['y'], self.block_size, self.block_size)
            pg.draw.rect(self.screen, self.background_field, clear)

    def draw(self, new_cord):
        """*** Start draw ***

        :param new_cord: The cord on which the snake should draw"""
        count = 0
        for cord in new_cord:
            self.net['status'][cord[0]][cord[1]] = 'snake'
            block = self.net['cord'][cord[0]][cord[1]]
            snake = pg.Rect(block['x'], block['y'], self.block_size, self.block_size)
            if self._snake_dict['status'][count] == 'head':
                pg.draw.rect(self.screen, self.__color_head, snake)
            else:
                pg.draw.rect(self.screen, self.__color_body, snake)
            count += 1
    # ------------

    # --- spawn snake ---
    def __spawn_draw(self):
        """*** Start draw ***
        Without status checks!"""
        count = 0
        for cord in self._snake_dict['cord']:
            block = self.net['cord'][cord[0]][cord[1]]
            snake = pg.Rect(block['x'], block['y'], self.block_size, self.block_size)
            if self._snake_dict['status'][count] == 'head':
                pg.draw.rect(self.screen, self.__color_head, snake)
            else:
                pg.draw.rect(self.screen, self.__color_body, snake)
            count += 1

    def __snake_status(self):
        """*** Append snake in status ***"""
        head = True
        for cord in self._snake_dict['cord']:
            self.net['status'][cord[0]][cord[1]] = 'snake'
            if head is True:
                self._snake_dict['status'].append('head')
                head = False
            else:
                self._snake_dict['status'].append('body')
        self._snake_dict['status'].reverse()

    def __spawn_cord(self, side):
        """*** Start cord ***

        :param side: 'left' or 'right'"""
        spawn_cords = []

        # math
        len_net = len(self.net['status'])
        start_block = len_net // 2
        length_1 = self.snake_length // 2
        length_2 = self.snake_length - length_1 - 1

        # margin from the edge
        margin = self.snake_margin
        if side == 'right':
            margin = self.col_net - self.snake_margin - 1

        # create spawn cords
        copy_start_block = start_block
        for i in range(length_1):  # \
            copy_start_block -= 1  # | Up
            spawn_cords.append([copy_start_block, margin])  # /

        spawn_cords.append([start_block, margin])  # Centre

        copy_start_block = start_block  # \
        for i in range(length_2):  # | Down
            copy_start_block += 1  # /
            spawn_cords.append([copy_start_block, margin])

        # end
        spawn_cords.sort()
        if side == 'left':
            spawn_cords.reverse()
        self._snake_dict['cord'] = spawn_cords

    def spawn(self, side):
        """*** Spawn snake ***

        :param side: 'left' / 'right'
        """
        if side == 'left' or side == 'right':
            self.__spawn_cord(side)
            self.__snake_status()
            self.__spawn_draw()
        else:
            raise ValueError("""the side is specified incorrectly!
the side must be: 'left' / 'right'""")
    # -------------------

    # --- collision ---
    # eat
    def eat(self):
        """*** Was an apple eaten ***"""
        eat = self._eat
        self._eat = False
        return eat

    def eaten(self):
        """*** Number of apples eaten ***"""
        return self._eaten_apple

    # lost
    def lost(self):
        """*** Did the snake lose ***"""
        return self._lost
    # -----------------

    # --- move ---
    @staticmethod
    def __change_cord(old_cord, way_x=0, way_y=0):
        """*** Change cord ***

        :param old_cord: cord of where the snake is now
        :param way_x: shift on x
        :param way_y: shift on y"""
        cord = old_cord
        del cord[0]
        cord.append([cord[-1][0] + way_x, cord[-1][1] + way_y])
        return cord

    def __way(self, side):
        """*** The direction of the snake ***

        :param side: 'forward' / 'backward' / 'left' / 'right'"""
        new_cord = []
        if side == 'forward':
            new_cord = self.__change_cord(self._snake_dict['cord'].copy(), way_x=-1)
        elif side == 'backward':
            new_cord = self.__change_cord(self._snake_dict['cord'].copy(), way_x=1)
        elif side == 'left':
            new_cord = self.__change_cord(self._snake_dict['cord'].copy(), way_y=-1)
        elif side == 'right':
            new_cord = self.__change_cord(self._snake_dict['cord'].copy(), way_y=1)
        return new_cord

    def __check_move(self, new_cord):
        """*** Check if the snake did not collide with the wall, the snake or the apple ***

        - If the snake come across an apple then increase -

        :param new_cord: cord at which the snake should appear"""
        if new_cord[-1][0] >= self.row_net or new_cord[-1][1] >= self.col_net or \
                new_cord[-1][0] < 0 or new_cord[-1][1] < 0 or \
                self.net['status'][new_cord[-1][0]][new_cord[-1][1]] == 'snake':
            self._lost = True
        elif self.net['status'][new_cord[-1][0]][new_cord[-1][1]] == 'apple':
            self.net['status'][new_cord[-1][0]][new_cord[-1][1]] = '-'
            self._eaten_apple += 1
            self._eat = True
            self._snake_dict['status'][-1] = 'body'
            self._snake_dict['status'].append('head')
            new_cord.reverse()
            new_cord.append((new_cord[-1][0] - 1, new_cord[-1][1]))
            new_cord.reverse()
        return new_cord

    def move(self, side):  # forward, backward, left, right
        """*** Snake move ***

        :param side: 'up' / 'down' / 'left' / 'right'"""
        new_cord = self.__way(side)
        if new_cord:  # drawing
            self.__check_move(new_cord)
            if self._lost is not True:
                self.__clear(self._snake_dict['cord'].copy())
                self.draw(new_cord)
                self._snake_dict['cord'] = new_cord
    # ------------

    def clear(self):
        """*** Cleaning snake data ***"""
        self._snake_dict = {'cord': [], 'status': []}
        self._eaten_apple = 0
        self._eat = False
        self._lost = False
