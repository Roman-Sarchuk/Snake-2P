class ATTRIBUTE:
    """*** Imported into all parts of the code ***"""
    def __init__(self):
        # --- size ---
        self.scr_size = (584, 380)
        self.head_size = 50
        self.line_size = 3
        self.field_size = (self.scr_size[0] - self.line_size * 2,
                           self.scr_size[1] - self.head_size - self.line_size * 2 + 1)
        self.block_margin = 3
        self.block_size = 20

        # --- color ---
        self.WIGHT = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ORANGE = (255, 103, 0)
        self.RED = (255, 0, 0)

        # --- DISPLAY ---
        self._color_text = self.WIGHT
        self._color_line = self.WIGHT
        self._background_head = self.ORANGE
        self._background_field = self.BLACK

        # --- NET ---
        self._row_net = 14
        self._col_net = 25

        # --- SNAKE ---
        # color
        self._color_snake1_head = (0, 255, 0)
        self._color_snake1_body = (0, 115, 0)
        self._color_snake2_head = (0, 0, 255)
        self._color_snake2_body = (0, 0, 115)
        # spawn
        self._snake_length = 4
        self._snake_margin = 3

        # --- APPLE ---
        self._color_apple = self.RED
        self._max_apple = 2
