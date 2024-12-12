import pygame as py
from random import randrange
# my import
import Attribute


class APPLE(Attribute.ATTRIBUTE):
    def __init__(self, screen):
        super(APPLE, self).__init__()
        # Color
        self._color = self._color_apple
        # Other
        self._cord = (0, 0)
        self._screen = screen

    # --- draw ---
    def draw(self, net_cord, apple_cord):
        """*** Draw apple ***

        :param net_cord: net with 'cord'
        :param apple_cord: apple cord for draw"""
        block_cord = net_cord[apple_cord[0]][apple_cord[1]]
        start_pos = (block_cord['x'], block_cord['y'])
        end_pos = (start_pos[0] + self.block_size, start_pos[1] + self.block_size)
        centre = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
        radius = self.block_size/2
        py.draw.circle(self._screen, self._color, centre, radius)
    # ------------

    # --- chek ---
    @staticmethod
    def __check_status(net_status, cord):
        """--- Check if the cell is free ---

        :param net_status: net with 'status'"""
        if net_status[cord[0]][cord[1]] != '-':
            raise ValueError(f'block -> {cord}\n! this block is already taken !')
    # ------------

    # --- add to status ---
    def add_to_status(self, net_status, cord):
        """*** Add apple to status ***

        :param net_status: net with 'status'
        :param cord: apple's cord"""
        self.__check_status(net_status, cord)
        net_status[cord[0]][cord[1]] = 'apple'
    # ---------------------

    # --- spawn ---
    def __cord(self, net_status):
        """*** Cord for spawn apple ***

        :param net_status: net with 'status'"""
        while True:
            try:
                cord = (randrange(len(net_status)), randrange(len(net_status[0])))
                self.__check_status(net_status, cord)
            except ValueError:
                continue
            self._cord = cord
            break

    def spawn(self, net):
        """*** Spawn apple ***

        :param net: net dict with 'cord' and 'status'"""
        self.__cord(net['status'])
        self.add_to_status(net['status'], self._cord)
        self.draw(net['cord'], self._cord)
        return net
    # -------------
