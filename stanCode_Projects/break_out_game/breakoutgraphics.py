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

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.



class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=window_height - PADDLE_OFFSET)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2*BALL_RADIUS, 2*BALL_RADIUS, x=(window_width - 2*BALL_RADIUS) / 2,
                          y=(window_height - 2*BALL_RADIUS) / 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # # Default initial velocity for the ball.
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1,MAX_X_SPEED)
        if (random.random() > 0.5):
            self.__dx = -self.__dx

        # Initialize our mouse listeners.
        onmouseclicked(self.starter)
        self.trigger = 0
        onmousemoved(self.paddle_move)

        # Draw bricks. 問coding style
        self.paddle_set()

        self.check_object()

        # game over and win message setting
        self.game_over = GLabel('Game over!',x=window_width*1/4 , y=2/3*window_height)
        self.game_over.font = '-50'
        self.win = GLabel("Win!",x=window_width/2-50 , y=2/3*window_height)
        self.win.font = '-50'

    '''
    when trigger = 0, it means game is stopped. The mouseclick will take trigger to 1 and enter the game.
    When trigger is 1, it means game is playing. The mouseclick will not work.
    '''
    def starter(self, mouse):
        if self.window.get_object_at(((self.window.width - BALL_RADIUS) / 2)+ self.ball.width/2 ,((self.window.height - BALL_RADIUS) / 2)+ self.ball.height/2) is not None :
            self.trigger=1

    def dx_get(self):
        if self.trigger ==0:
            return 0
        else:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if (random.random() > 0.5):
                self.__dx = -self.__dx
            return self.__dx

    def dy_get(self):
        if self.trigger ==0:
            return 0
        else:
            self.__dy = INITIAL_Y_SPEED
            return self.__dy

    def paddle_set(self):
        brick_x = 0
        brick_y = BRICK_OFFSET
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT) # 放在constructor外面可以嗎
                self.brick.filled = True
                self.brick.color = 'black'
                self.brick.fill_color = 'black'
                self.window.add(self.brick, x=brick_x, y=brick_y)
                brick_x = brick_x + BRICK_WIDTH + BRICK_SPACING
            brick_x = 0
            brick_y = brick_y + BRICK_HEIGHT + BRICK_SPACING

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        if mouse.x <= self.paddle.width / 2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width-PADDLE_WIDTH

    def check_object(self):
        if self.window.get_object_at(self.ball.x, self.ball.y) is not None:
            self.__dx = -self.__dx
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height) is not None:
            self.__dx = -self.__dx
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y) is not None:
            self.__dx = -self.__dx
            self.__dy = -self.__dy
        elif self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y + self.ball.height) is not None:
            self.__dx = -self.__dx
            self.__dy = -self.__dy





