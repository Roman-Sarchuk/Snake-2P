from pygame import display


# *** BASE ***
class ContSize:
    """not-variable"""
    scr_size = (584, 380)
    head_size = 50
    line_size = 3
    field_size = (scr_size[0] - line_size * 2,
                  scr_size[1] - head_size - line_size * 2 + 1)
    block_margin = 3
    block_size = 20


class ContColor:
    """not-variable"""
    WIGHT = (255, 255, 255)
    BLACK = (0, 0, 0)
    ORANGE = (255, 103, 0)
    RED = (255, 0, 0)


class ContScreen:
    """not-variable"""
    screen = display.set_mode(ContSize.scr_size)


# *** Net ***
class NetCharacter:
    """not-variable"""
    row_net = 14
    col_net = 25


class NET(ContSize, NetCharacter):
    """auxiliary"""
    def __init__(self):
        self._net = {'cord': self.__create_net_cord(), 'status': self.__create_net_status()}

    # --- get ---
    def get(self):
        """*** Get a net of 'cord' and 'status' ***"""
        return self._net
    # -----------

    # --- create net ---
    def __create_net_cord(self):
        """*** Creating a net of coordinates ***"""
        x, y = self.line_size, self.head_size + self.line_size - 1
        net_cord = []
        for row in range(self.row_net):
            net_cord.append([])
            for col in range(self.col_net):
                net_cord[row].append({'x': x + col * self.block_size + self.block_margin * (col + 1),
                                      'y': y + row * self.block_size + self.block_margin * (row + 1)})
        return net_cord

    def __create_net_status(self):
        """*** Creating a status net ***"""
        net_status = []
        for row in range(self.row_net):
            net_status.append([])
            for col in range(self.col_net):
                net_status[row].append('-')
        return net_status
    # ------------------

    def clear(self):
        return {'cord': self.__create_net_cord(), 'status': self.__create_net_status()}


class ContNet:
    """variable"""
    net = NET().get()


# *** OTHER ***
class ContDisplay:
    """not-variable"""
    color_text = ContColor.WIGHT
    color_line = ContColor.WIGHT
    background_head = ContColor.ORANGE
    background_field = ContColor.BLACK


class ContSnakeColor:
    """not-variable"""
    color_snake1_head = (0, 255, 0)
    color_snake1_body = (0, 115, 0)
    color_snake2_head = (0, 0, 255)
    color_snake2_body = (0, 0, 115)


class ContSnakeSpawn:
    """not-variable"""
    snake_length = 4
    snake_margin = 3


class ContApple:
    """not-variable"""
    color_apple = ContColor.RED
    count_apple = 2


# *** Combine ***
class CombWindow(ContScreen, ContSize, ContDisplay):
    """Combine: ContScreen, ContSize, ContDisplay"""
    pass
