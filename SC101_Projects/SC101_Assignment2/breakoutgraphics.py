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

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
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

        # Create score board
        self.score = 0
        self.score_board = GLabel(f"Score : {self.score}")
        self.score_board.font = "Comic Sans MS-15"
        self.window.add(self.score_board, 3, self.score_board.height+15)

    @staticmethod
    def v_set():
        """
        設定速度
        :return:（dx, dy）, int
        """
        vx = random.randint(1, MAX_X_SPEED)
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
            color = i * 255 // (self.brick_cols + 1)                               # 設定灰階顏色
            self.__build_brick_row(self._brick_offset + i * (self._brick_spacing + self._brick_height),
                                   color)

    def __build_brick_row(self, build_height, gray_scale):
        """
        build_height: int, 建造的高度
        gray_scale: int, RGB值
        """
        for i in range(0, self.brick_rows):
            a_brick = self.__build_a_brick(gray_scale)
            self.window.add(a_brick, i*(self._brick_width+self._brick_spacing), build_height)

    def __build_a_brick(self, gray_scale):
        """
        gray_scale: int, RGB值
        :return: obj, 建造好的brick
        """
        brick = GRect(self._brick_width, self._brick_height)
        brick.filled = True
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

    def hit_block(self):
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
        ball_on_top =  maybe_block.y - self.ball.y > self.ball.height-INITIAL_Y_SPEED and maybe_block.y - self.ball.y <= self.ball.height
        ball_under_buttom = self.ball.y-maybe_block.y > self._brick_height-INITIAL_Y_SPEED and self.ball.y-maybe_block.y <= self._brick_height
        ball_is_left = maybe_block.x - self.ball.x > self.ball.width-abs(self.__dx) and maybe_block.x - self.ball.x <= self.ball.width
        ball_is_right = self.ball.x-maybe_block.x > self._brick_width-abs(self.__dx) and self.ball.x-maybe_block.x <= self._brick_width
        if ball_on_top or ball_under_buttom:
            self.rebound_y()
        if ball_is_left or ball_is_right:                   # 也可用elif會比較正常，因為大部分是打到磚塊上下
            self.rebound_x()
        self.window.remove(maybe_block)
        self.score += 10                                    # 打到磚塊後的得分
        return True

