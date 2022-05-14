import pygame as py
from Container import CombWindow


class FIELD(CombWindow):
    def __init__(self):
        self.__txt_size = self.field_size[0]//7
        self.__font = py.font.SysFont('bahnschrift', self.__txt_size)
        self.__rest_font = py.font.SysFont('bahnschrift', self.__txt_size//3)

    # --- fill field ---
    def background(self):
        """*** Field background ***"""
        pos_field = {'x': self.line_size, 'y': self.head_size + self.line_size - 1,
                     'width': self.field_size[0], 'height': self.field_size[1]}
        background = py.Rect(pos_field['x'], pos_field['y'], pos_field['width'], pos_field['height'])
        py.draw.rect(self.screen, self.background_field, background)
    # ------------------

    # --- create field ---
    def __border(self):
        """*** Screen outline ***"""
        contour = py.Rect(0, 0, self.scr_size[0], self.scr_size[1]),
        py.draw.rect(self.screen, self.color_line, contour, self.line_size)

    def draw(self):
        """*** Create field ***"""
        self.background()
        self.__border()
    # --------------------

    # --- end ---
    def __lost_txt(self, num_player, field_center: tuple or list):
        start_cord = (field_center[0] - self.field_size[0] // 3 + 10,
                      field_center[1] - self.field_size[1] // 3)

        up_txt = self.__font.render(f'Player #{num_player}', True, self.color_text)
        self.screen.blit(up_txt, start_cord)

        down_txt_cord = (start_cord[0] + 80, start_cord[1] + self.__txt_size + 15)
        down_txt = self.__font.render('Lost!', True, self.color_text)
        self.screen.blit(down_txt, down_txt_cord)

    def __rest_txt(self, field_center: tuple or list):
        start_cord = (self.line_size + 5, self.head_size + self.field_size[1] + self.line_size - self.__txt_size//2)

        rest_txt = self.__rest_font.render(f'Press "Enter" to reboot', True, self.color_text)
        self.screen.blit(rest_txt, start_cord)

    def caption(self, num_player='?'):
        """*** Final text ***

        :param num_player: player number"""
        field_center = (self.field_size[0] // 2 + self.line_size,
                        self.field_size[1] // 2 + self.head_size + self.line_size)
        self.__lost_txt(num_player, field_center)
        self.__rest_txt(field_center)
    # -----------
