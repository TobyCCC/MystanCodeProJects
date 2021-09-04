"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
NUM_LIVES = 3

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout', num_lives = NUM_LIVES):

        # Create a graphical window, with some extra space
        window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle.filled = True
        self.window.add(self.paddle, (window_width-paddle_width)/2, window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, window_width/2-ball_radius, window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.__dx, self.__dy = self.v_set()

        # Initialize our mouse listeners
        self.__game_start = False                     # 判斷遊戲是否開始
        onmousemoved(self.mouse_move)
        onmouseclicked(self.on_set)

        # Draw bricks
        self._brick_offset = brick_offset
        self._brick_width = brick_width
        self._brick_height = brick_height
        self._brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.__build_brick_col()
        self.brick_break_times = 0
        self.brick_break = False

        # Create score board
        self.score = 0
        self.score_board = GLabel(f"Score : {self.score}")
        self.score_board.font = "Comic Sans MS-15"
        self.window.add(self.score_board, 3, self.score_board.height+15)

        # number of lives
        self.num_lives = num_lives

        # getting object (x,y)
        self.the_brick_x = 0
        self.the_brick_y = 0

    @staticmethod
    def v_set():
        """
        設定速度
        :return:（dx, dy）, int
        """
        vx = random.randint(2, MAX_X_SPEED)
        if random.random() > 0.5:
            vx *= -1
        vy = INITIAL_Y_SPEED
        return vx, vy

    def get_speed(self):
        """
        回傳給user端dx和dy
        :return: （dx, dy）, int
        """
        return self.__dx, self.__dy

    def game_start(self):
        """
        回報遊戲是否開始
        """
        return self.__game_start

    def mouse_move(self, mouse):
        position = mouse.x - self.paddle.width / 2                 # 由滑鼠位置反推paddle的位置
        if position <= 0:
            self.paddle.x = 0
        elif position >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = position

    def on_set(self, mouse):
        self.__game_start = True                                    # 回傳遊戲開始

    def __build_brick_col(self):
        """
        由上至下建造所有的brick
        """
        for i in range(0, self.brick_cols):
            # color = i * 255 // (self.brick_cols + 1)                               # 設定灰階顏色
            self.__build_brick_row(self._brick_offset + i * (self._brick_spacing + self._brick_height))

    def __build_brick_row(self, build_height):
        """
        build_height: int, 建造的高度
        gray_scale: int, RGB值
        """
        for i in range(0, self.brick_rows):
            a_brick = self.__build_a_brick()
            self.window.add(a_brick, i*(self._brick_width+self._brick_spacing), build_height)

    def __build_a_brick(self):
        """
        gray_scale: int, RGB值
        :return: obj, 建造好的brick
        """
        brick = GRect(self._brick_width, self._brick_height)
        brick.filled = True
        gray_scale = random.randrange(0, self.brick_cols) * 255 // (self.brick_cols + 1)
        brick.color = (gray_scale, gray_scale, gray_scale)
        brick.fill_color = (gray_scale, gray_scale, gray_scale)
        return brick

    def reset_ball_position(self):
        """
        把球重置到畫面中央，速度重設
        """
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.__dx, self.__dy = self.v_set()
        self.new_ball_speed()

    def hit_paddle(self):
        """
        判斷是否打到paddle
        :return: boolean
        """
        maybe_paddle = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        if maybe_paddle is not None and maybe_paddle == self.paddle:
            return True
        else:
            maybe_paddle = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
            if maybe_paddle is not None and maybe_paddle == self.paddle:
                return True
            else:
                return False

    def rebound_x(self):
        """
        將dx變號
        """
        self.__dx *= -1

    def rebound_y(self):
        """
        將dy變號
        """
        self.__dy *= -1

    def hit_block(self,death_time):
        """
        判斷是否打到block，並且設定打到磚塊後的反彈速度
        :return: boolean
        """
        # 判斷是否打到磚塊
        maybe_block = self.window.get_object_at(self.ball.x, self.ball.y)
        if maybe_block is None or maybe_block == self.paddle or maybe_block == self.score_board:
            maybe_block = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y)
            if maybe_block is None or maybe_block == self.paddle or maybe_block == self.score_board:
                maybe_block = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
                if maybe_block is None or maybe_block == self.paddle or maybe_block == self.score_board:
                    maybe_block = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y + self.ball.height)
                    if maybe_block is None or maybe_block == self.paddle or maybe_block == self.score_board:
                        return False

        # 判斷打到磚塊的何處，計算反彈
        ball_on_top =  maybe_block.y - self.ball.y > self.ball.height-abs(self.__dy) and maybe_block.y - self.ball.y <= self.ball.height
        ball_under_buttom = self.ball.y-maybe_block.y > self._brick_height-abs(self.__dy) and self.ball.y-maybe_block.y <= self._brick_height
        ball_is_left = maybe_block.x - self.ball.x > self.ball.width-abs(self.__dx) and maybe_block.x - self.ball.x <= self.ball.width
        ball_is_right = self.ball.x-maybe_block.x > self._brick_width-abs(self.__dx) and self.ball.x-maybe_block.x <= self._brick_width
        if ball_on_top or ball_under_buttom:
            self.rebound_y()
        if ball_is_left or ball_is_right:                   # 也可用elif會比較正常，因為大部分是打到磚塊上下
            self.rebound_x()
        self.the_brick_x = maybe_block.x
        self.the_brick_y = maybe_block.y
        if self.count_block_lives(maybe_block) == 1:
            self.window.remove(maybe_block)                     # 將磚塊移除
            self.score += 100*self.score_bonus(death_time)      # 移除磚塊可以拿到100分＊bonus
            self.brick_break_times += 1
            self.brick_break = True
        else:
            color = (self.brick_cols - self.count_block_lives(maybe_block) +1) * 255 // (self.brick_cols + 1)
            maybe_block.color = (color, color, color)                   # 改變磚塊的顏色
            maybe_block.fill_color = (color, color, color)
            self.score += 10*self.score_bonus(death_time)               # 擊中磚塊可以拿到10分＊bonus
            self.brick_break = False
        return True

    def count_block_lives(self, block):
        """
        讀取磚塊RGB數值，將RGB數值反推為磚塊的剩餘壽命
        block：object，磚塊
        :return:  int, 剩餘的命
        """
        colors = block.color.rgb[0]
        lives = self.brick_cols - (colors + 1)*(self.brick_cols + 1) // 255
        return lives

    def score_bonus(self, death_time):
        """
        計算分數的加乘倍數
        :param death_time: 死掉的次數
        :return:int, 加乘倍數
        """
        return self.num_lives - death_time

    def new_ball_speed(self):
        """
        隨著速度增加遊戲速度
        """
        if self.__dy > 0:
            self.__dy = int(INITIAL_Y_SPEED * (1 + self.score / 10000))
        else:
            self.__dy = -int(INITIAL_Y_SPEED * (1 + self.score / 10000))

    def falling_obj_lengthen(self, x, y):
        falling_obj_l = GRect(10, 10)
        falling_obj_l.filled = True
        falling_obj_l.color = "green"
        falling_obj_l.fill_color = "green"
        self.window.add(falling_obj_l, x+self._brick_width/2-5, y+self._brick_height/2-5)
        return falling_obj_l

    def obj_hit_paddle(self, obj):
        maybe_paddle = self.window.get_object_at(obj.x, obj.y + obj.height)
        if maybe_paddle is not None and maybe_paddle == self.paddle:
            return True
        else:
            maybe_paddle = self.window.get_object_at(obj.x + obj.width, obj.y + obj.height)
            if maybe_paddle is not None and maybe_paddle == self.paddle:
                return True
            else:
                return False



    def lengthen_paddle(self):
        self.paddle_width = self.paddle_width*1.2//1
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        # self.paddle.filled = True






