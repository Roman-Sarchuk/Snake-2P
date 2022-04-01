import pygame as py
# my import
import Attribute


class SNAKE(Attribute.ATTRIBUTE):
    def __init__(self, screen):
        super(SNAKE, self).__init__()
        # snake
        self._snake_dict = {'cord': [], 'status': []}
        self.__color_head = self.BLACK
        self.__color_body = self.WIGHT
        self._eaten_apple = 0
        self._eat = False
        self._lost = False

        # other
        self._screen = screen

    # --- color ---
    def set_color(self, color_head, color_body):
        """*** Set color snake ***

        :param color_body: ( RGB )
        :param color_head: ( RGB )"""
        self.__color_body = color_body
        self.__color_head = color_head
    # -------------

    # --- draw ---
    def __clear(self, net, old_cord):
        """*** Cleaning the old snake ***

        :param net: net with 'cord' and 'status'
        :param old_cord: cord of where the snake is now"""
        for cord in old_cord:
            net['status'][cord[0]][cord[1]] = '-'
            block = net['cord'][cord[0]][cord[1]]
            clear = py.Rect(block['x'], block['y'], self.block_size, self.block_size)
            py.draw.rect(self._screen, self._background_field, clear)

    def draw(self, net, new_cord):
        """*** Start draw ***

        :param net: net with 'cord' and 'status'
        :param new_cord: The cord on which the snake should draw"""
        count = 0
        for cord in new_cord:
            net['status'][cord[0]][cord[1]] = 'snake'
            block = net['cord'][cord[0]][cord[1]]
            snake = py.Rect(block['x'], block['y'], self.block_size, self.block_size)
            if self._snake_dict['status'][count] == 'head':
                py.draw.rect(self._screen, self.__color_head, snake)
            else:
                py.draw.rect(self._screen, self.__color_body, snake)
            count += 1
    # ------------

    # --- spawn snake ---
    def __spawn_draw(self, net_cord):
        """*** Start draw ***
        Without status checks!

        :param net_cord: net with 'cord'"""
        count = 0
        for cord in self._snake_dict['cord']:
            block = net_cord[cord[0]][cord[1]]
            snake = py.Rect(block['x'], block['y'], self.block_size, self.block_size)
            if self._snake_dict['status'][count] == 'head':
                py.draw.rect(self._screen, self.__color_head, snake)
            else:
                py.draw.rect(self._screen, self.__color_body, snake)
            count += 1

    def __snake_status(self, net_status):
        """*** Append snake in status ***

        :param net_status: net with 'status'"""
        head = True
        for cord in self._snake_dict['cord']:
            net_status[cord[0]][cord[1]] = 'snake'
            if head is True:
                self._snake_dict['status'].append('head')
                head = False
            else:
                self._snake_dict['status'].append('body')
        self._snake_dict['status'].reverse()

    def __spawn_cord(self, net_any, side):
        """*** Start cord ***

        :param net_any: net with 'cord' or status
        :param side: 'left' or 'right'"""
        spawn_cords = []

        # math
        len_net = len(net_any)
        start_block = len_net // 2
        length_1 = self._snake_length // 2
        length_2 = self._snake_length - length_1 - 1

        # margin from the edge
        margin = self._snake_margin
        if side == 'right':
            margin = self._col_net - self._snake_margin - 1

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

    def spawn(self, net, side):
        """*** Spawn snake ***

        :param net: net dict with 'cord' and 'status'
        :param side: 'left' / 'right'
        """
        if side == 'left' or side == 'right':
            self.__spawn_cord(net['status'], side)
            self.__snake_status(net['status'])
            self.__spawn_draw(net['cord'])
        else:
            raise ValueError("""the side is specified incorrectly!
the side must be: 'left' / 'right'""")
        return net
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

    def __check_move(self, net_status, new_cord):
        """*** Check if the snake did not collide with the wall, the snake or the apple ***

        - If the snake come across an apple then increase -

        :param net_status: net dict with 'status'
        :param new_cord: cord at which the snake should appear"""
        if new_cord[-1][0] >= self._row_net or new_cord[-1][1] >= self._col_net or \
                new_cord[-1][0] < 0 or new_cord[-1][1] < 0 or \
                net_status[new_cord[-1][0]][new_cord[-1][1]] == 'snake':
            self._lost = True
        elif net_status[new_cord[-1][0]][new_cord[-1][1]] == 'apple':
            net_status[new_cord[-1][0]][new_cord[-1][1]] = '-'
            self._eaten_apple += 1
            self._eat = True
            self._snake_dict['status'][-1] = 'body'
            self._snake_dict['status'].append('head')
            new_cord.reverse()
            new_cord.append((new_cord[-1][0] - 1, new_cord[-1][1]))
            new_cord.reverse()
        return new_cord

    def move(self, net, side):  # forward, backward, left, right
        """*** Snake move ***

        :param net: net dict with 'cord' and 'status'
        :param side: 'up' / 'down' / 'left' / 'right'"""
        new_cord = self.__way(side)
        if new_cord:  # drawing
            self.__check_move(net['status'], new_cord)
            if self._lost is not True:
                self.__clear(net, self._snake_dict['cord'].copy())
                self.draw(net, new_cord)
                self._snake_dict['cord'] = new_cord
    # ------------

    # --- clear ---
    def clear(self):
        """*** Cleaning the snake to the starting version ***"""
        self._snake_dict = {'cord': [], 'status': []}
        self._eat = False
        self._lost = False
    # -------------
