# my import
import Attribute
import Head
import Field
import Net
import Snake
import Apple


class ENGINE(Attribute.ATTRIBUTE):
    def __init__(self, screen):
        super(ENGINE, self).__init__()
        # object
        self.head = Head.HEAD(screen)
        self.field = Field.FIELD(screen)
        self.net = Net.NET()
        self.snake1 = Snake.SNAKE(screen)
        self.snake2 = Snake.SNAKE(screen)
        self.apple = Apple.APPLE(screen)

        # other
        self.__net = self.net.get()
        self._snake1_way = None    # forward, backward, left, right
        self._snake2_way = None
        self._count_apple = 0

    # --- create display ---
    def create_display(self):
        """*** Creating main display: the head and the field ***"""
        self.head.draw()
        self.field.draw()
    # ----------------------

    # --- spawn ---
    def spawn_snake(self):
        """*** The initial spawn of the snake ***"""
        self.snake1.set_color(self._color_snake1_head, self._color_snake1_body)
        self.__net = self.snake1.spawn(self.__net, 'left')
        self.snake2.set_color(self._color_snake2_head, self._color_snake2_body)
        self.__net = self.snake2.spawn(self.__net, 'right')

    def spawn_apple(self):
        """*** Create an apple if you don't have enough ***"""
        if self._count_apple != self._max_apple:
            self.__net = self.apple.spawn(self.__net)
            self._count_apple += 1
    # -------------

    # --- way ---
    def set_way(self, flag, way):
        """*** Set way ***

        :param flag: 'snake1' / 'snake2'
        :param way: 'forward' / 'backward' / 'left' / 'right'"""
        if flag == 'snake1':
            self._snake1_way = way
        elif flag == 'snake2':
            self._snake2_way = way
        else:
            raise ValueError("""the flag is specified incorrectly!
the flag must be: 'snake1' / 'sanke2'""")

    def get_way(self, flag):
        """*** Get way ***

        :param flag: 'snake1' / 'snake2'"""
        if flag == 'snake1':
            return self._snake1_way
        elif flag == 'snake2':
            return self._snake2_way
        else:
            raise ValueError("""the flag is specified incorrectly!
the flag must be: 'snake1' / 'snake2'""")
    # -----------

    # --- move ---
    def snake_move(self):
        """*** Snake move and check to eat ***"""
        self.snake1.move(self.__net, self._snake1_way)
        eat1 = self.snake1.eat()
        self.snake2.move(self.__net, self._snake2_way)
        eat2 = self.snake2.eat()
        if eat1 is True or eat2 is True:
            self._count_apple -= 1
            self.head.score(self.snake1.eaten(), self.snake2.eaten())
    # ------------

    # --- end ---
    def check_end(self):
        """*** Whether the snake crashed into a wall or a snake ***"""
        end1 = self.snake1.lost()
        end2 = self.snake2.lost()
        if end1 is True:
            return 'lost1'
        elif end2 is True:
            return 'lost2'

    def message(self, lost):
        """*** End text ***

        :param lost: Who lost?"""
        self.field.background()
        self.field.caption(lost)
    # -----------
