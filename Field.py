import pygame as py
# my import
import Attribute


class FIELD(Attribute.ATTRIBUTE):
    def __init__(self, screen):
        super(FIELD, self).__init__()
        self._screen = screen
        self.__txt_size = self.field_size[0]//7
        self.__font = py.font.SysFont('bahnschrift', self.__txt_size)

    # --- fill field ---
    def background(self):
        """*** Field background ***"""
        x, y = self.line_size, self.head_size + self.line_size - 1
        width, height = self.field_size[0], self.field_size[1]
        background = py.Rect(x, y, width, height)
        py.draw.rect(self._screen, self._background_field, background)
    # ------------------

    # --- create field ---
    def __border(self):
        """*** Screen outline ***"""
        contour = py.Rect(0, 0, self.scr_size[0], self.scr_size[1]),
        py.draw.rect(self._screen, self._color_line, contour, self.line_size)

    def draw(self):
        """*** Create field ***"""
        self.background()
        self.__border()
    # --------------------

    # --- end ---
    def caption(self, num_player='?'):
        """*** Final text ***

        :param num_player: player number"""
        field_center = (self.field_size[0] // 2 + self.line_size,
                        self.head_size + self.field_size[1] // 2 + self.line_size)
        start_cord = (field_center[0] - self.field_size[0] // 3 + 10,
                      field_center[1] - self.field_size[1] // 3)

        up_txt_cord = start_cord
        up_txt = self.__font.render(f'Player #{num_player}', True, self._color_text)
        self._screen.blit(up_txt, up_txt_cord)

        down_txt_cord = (start_cord[0] + 80, start_cord[1] + self.__txt_size + 15)
        down_txt = self.__font.render('Lost!', True, self._color_text)
        self._screen.blit(down_txt, down_txt_cord)
    # -----------
