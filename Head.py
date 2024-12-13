import pygame as pg
from Container import CombWindow
pg.init()


class HEAD(CombWindow):
    def __init__(self):
        self.__font = pg.font.SysFont('arial', 30)

    # --- create head ---
    def __text(self):
        """*** Text: 'Player 1: score' and 'Player 2: score' ***"""
        player1 = self.__font.render('Player 1 :', True, self.color_text)
        player2 = self.__font.render('Player 2 :', True, self.color_text)
        txt_cord = {'play1': (10, 7), 'play2': (self.scr_size[0] - 210, 7)}
        self.screen.blit(player1, txt_cord['play1'])
        self.screen.blit(player2, txt_cord['play2'])

    def __line(self):
        """*** Creating a line between the head and the field ***"""
        top_line = {'start': (0, self.head_size),
                    'end': (self.scr_size[0], self.head_size)}
        pg.draw.line(self.screen, self.color_line, top_line['start'], top_line['end'], self.line_size)

    def __background(self):
        """*** Head background ***"""
        top_rect = pg.Rect(0, 0, self.scr_size[0], 50)
        pg.draw.rect(self.screen, self.background_head, top_rect)

    def draw(self):
        """*** Create head ***"""
        self.__background()
        self.__line()
        self.__text()
        self.score()
    # -------------------

    def score(self, play1=0, play2=0):
        """*** Player score change ***

        :param play1: player score #1
        :param play2: player score #2"""
        # --- Clear ---
        clear = {'play1': pg.Rect(145, 7, 100, 35),
                 'play2': pg.Rect(self.scr_size[0] - 75, 7, 70, 35)}
        pg.draw.rect(self.screen, self.background_head, clear['play1'])
        pg.draw.rect(self.screen, self.background_head, clear['play2'])

        # --- Draw ---
        player1 = self.__font.render(str(play1), True, self.color_text)
        player2 = self.__font.render(str(play2), True, self.color_text)
        txt_cord = {'play1': (145, 7), 'play2': (self.scr_size[0] - 75, 7)}
        self.screen.blit(player1, txt_cord['play1'])
        self.screen.blit(player2, txt_cord['play2'])
