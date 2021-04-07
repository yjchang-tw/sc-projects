"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3





def main():
    global NUM_LIVES

    graphics = BreakoutGraphics()
    # bricks_num is the number of existing bricks  in the game
    bricks_num = 100

    # Add animation loop here!
    while True:
        dx = graphics.dx_get()
        dy = graphics.dy_get()
        graphics.ball.x =(graphics.window.width - graphics.ball.width) / 2
        graphics.ball.y=(graphics.window.height - graphics.ball.height) / 2

        while True:
            if dx == 0 and dy == 0:
                dx = graphics.dx_get()
                dy = graphics.dy_get()
                pause(FRAME_RATE)
            else:
                graphics.ball.move(dx,dy)

                # when ball is touching the paddle, it will just work the function of "check_object".
                # And when the ball is touching the other thing, it means the ball touched the bricks.
                # It will remove the brick and bricks_num subtract one.

                if graphics.window.get_object_at(graphics.ball.x,graphics.ball.y) is not None:
                    if graphics.paddle.x <= graphics.ball.x <= graphics.paddle.x+graphics.paddle.width and graphics.paddle.y <= graphics.ball.y <= graphics.paddle.y + graphics.paddle.height:
                        dy = abs(dy)
                    else:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x,graphics.ball.y))
                        bricks_num -= 1
                    dy = -dy
                elif graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height) is not None:
                    if graphics.paddle.x <= graphics.ball.x <= graphics.paddle.x+graphics.paddle.width and graphics.paddle.y <= graphics.ball.y+graphics.ball.height  <= graphics.paddle.y + graphics.paddle.height:
                        dy = abs(dy)
                    else:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height))
                        bricks_num -= 1
                    dy = -dy
                elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width , graphics.ball.y) is not None:
                    if graphics.paddle.x <= graphics.ball.x+graphics.ball.width <= graphics.paddle.x+graphics.paddle.width and graphics.paddle.y <= graphics.ball.y  <= graphics.paddle.y + graphics.paddle.height:
                        dy = abs(dy)
                    else:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width ,graphics.ball.y))
                        bricks_num -= 1
                    dy = -dy
                elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y + graphics.ball.height) is not None:
                    if graphics.paddle.x <= graphics.ball.x+graphics.ball.width <= graphics.paddle.x+graphics.paddle.width and graphics.paddle.y <= graphics.ball.y + graphics.ball.height  <= graphics.paddle.y + graphics.paddle.height:
                        dy = abs(dy)
                    else:
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y + graphics.ball.height))
                        bricks_num -= 1
                    dy = -dy

                # when the ball touches the bounder of the window,
                # it will change the velocity except the bottom of the window.
                if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    dx = - dx
                if graphics.ball.y <= 0:
                    dy = -dy

                # 1. bricks_num =0 means winning, so we have bto break.
                # 2. When ball is touching the bottom of the window, NUM_LIVES will minus one and break.
                if bricks_num == 0:
                    break
                elif graphics.ball.y + graphics.ball.height >= graphics.window.height :
                    NUM_LIVES -= 1
                    graphics.trigger =0

                    break

                pause(FRAME_RATE)

        # check the winning condition and losing condition
        if NUM_LIVES == 0 :
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.game_over)
            break
        elif bricks_num ==0:
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.win)
            break

if __name__ == '__main__':

    main()




