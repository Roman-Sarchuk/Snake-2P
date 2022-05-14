import pygame as pg
from random import randrange
from Container import ContScreen, ContSize, ContNet, ContApple


class APPLE(ContScreen, ContSize, ContNet, ContApple):
    def __init__(self):
        self._cord = (0, 0)
        self._count = 0

    # --- count ---
    def add_count(self):
        self._count += 1

    def subtract_count(self):
        self._count -= 1
    # -------------

    def draw(self, apple_cord):
        """*** Draw apple ***

        :param apple_cord: apple cord for draw"""
        block_cord = self.net['cord'][apple_cord[0]][apple_cord[1]]
        start_pos = (block_cord['x'], block_cord['y'])
        end_pos = (start_pos[0] + self.block_size, start_pos[1] + self.block_size)
        centre = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
        radius = self.block_size/2
        pg.draw.circle(self.screen, self.color_apple, centre, radius)

    # --- chek ---
    def __check_status(self, cord):
        """--- Check if the cell is free ---"""
        if self.net['status'][cord[0]][cord[1]] != '-':
            raise ValueError(f'block -> {cord}\n! this block is already taken !')
    # ------------

    # --- add to status ---
    def add_to_status(self, cord):
        """*** Add apple to status ***

        :param cord: apple's cord"""
        self.__check_status(cord)
        self.net['status'][cord[0]][cord[1]] = 'apple'
    # ---------------------

    # --- spawn ---
    def __cord(self):
        """*** Cord for spawn apple ***"""
        while True:
            try:
                cord = (randrange(len(self.net['status'])), randrange(len(self.net['status'][0])))
                self.__check_status(cord)
            except ValueError:
                continue
            self._cord = cord
            break

    def spawn(self):
        """*** Spawn apple ***"""
        self.add_count()
        self.__cord()
        self.add_to_status(self._cord)
        self.draw(self._cord)
    # -------------

    def clear(self):
        """*** Clearing apple data ***"""
        self._cord = (0, 0)
        self._count = 0
