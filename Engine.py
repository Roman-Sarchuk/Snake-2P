from Container import ContSnakeColor, ContApple, ContNet, NET
import Head
import Field
import Snake
import Apple


class OBJ:
    head = Head.HEAD()
    field = Field.FIELD()
    snake1 = Snake.SNAKE()
    snake2 = Snake.SNAKE()
    apple = Apple.APPLE()


class ENGINE(OBJ, ContSnakeColor):
    def __init__(self):
        # way: 'forward' / 'backward' / 'left' / 'right'
        self._snake1_way = None
        self._snake2_way = None

    def create_display(self):
        """*** Creating main display: the head and the field ***"""
        self.head.draw()
        self.field.draw()

    # --- spawn ---
    def spawn_snake(self):
        """*** The initial spawn of the snake ***"""
        self.snake1.set_color(ContSnakeColor.color_snake1_head, ContSnakeColor.color_snake1_body)
        self.snake1.spawn('left')
        self.snake2.set_color(ContSnakeColor.color_snake2_head, ContSnakeColor.color_snake2_body)
        self.snake2.spawn('right')

    def spawn_apple(self, number=1):
        """*** Create an apple if you don't have enough ***"""
        for _ in range(number):
            self.apple.spawn()
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
        self.snake1.move(self._snake1_way)
        eat1 = self.snake1.eat()
        self.snake2.move(self._snake2_way)
        eat2 = self.snake2.eat()
        if eat1 is True or eat2 is True:
            self.apple.subtract_count()
            self.spawn_apple()
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

    # --- restart ---
    @staticmethod
    def __rest_net():
        ContNet.net = NET().clear()

    def __rest_window(self):
        self.head.score()
        self.field.background()

    def __rest_snake(self):
        self.set_way('snake1', None)
        self.set_way('snake2', None)
        self.snake1.clear()
        self.snake2.clear()
        self.spawn_snake()

    def __rest_apple(self):
        self.apple.clear()
        self.spawn_apple(ContApple.count_apple)

    def restart(self):
        self.__rest_net()
        self.__rest_window()
        self.__rest_snake()
        self.__rest_apple()
    # ---------------
