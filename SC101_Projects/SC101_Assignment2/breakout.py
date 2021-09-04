"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    while not graphics.game_start():                        # 點擊啟動的開關
        pause(FRAME_RATE)

    dx, dy = graphics.get_speed()                           # 速度
    death_times = 0
    win = 10*graphics.brick_rows*graphics.brick_cols        # 全部磚塊打完的分數

    # Add animation loop here!
    while death_times < NUM_LIVES and graphics.score < win:

        # 移動
        graphics.ball.move(dx, dy)

        # 判斷條件
        if graphics.hit_block():                            # 打到磚塊
            dx, dy = graphics.get_speed()
            graphics.score_board.text = f"Score : {graphics.score}"
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:    # 打到左右牆壁
            graphics.rebound_x()
            dx, dy = graphics.get_speed()
        if graphics.hit_paddle():                           # 打到paddle
            if dy > 0:                                      # 確保球不會卡在paddle中
                graphics.rebound_y()
                dx, dy = graphics.get_speed()
            else:
                pass
        elif graphics.ball.y <= 0:                          # 打到最上面
            graphics.rebound_y()
            dx, dy = graphics.get_speed()
        elif graphics.ball.y >= graphics.window.height-graphics.ball.height:           # 打到最下面而死亡
            graphics.reset_ball_position()
            dx, dy = graphics.get_speed()
            death_times += 1
            pause(FRAME_RATE*120)                           # 使死亡後能暫停一下再開始

        # 執行暫停
        pause(FRAME_RATE)

    # 印出結束字樣
    if death_times == NUM_LIVES:
        final_label = GLabel("You Lose! ¯\_(ツ)_/¯")
    else:
        final_label = GLabel("You Win! ¯\_(ツ)_/¯")
    final_label.color = "navy"
    final_label.font = "Comic Sans MS-40"
    graphics.window.remove(graphics.ball)
    graphics.window.add(final_label, (graphics.window.width-final_label.width)/2, (graphics.window.height-final_label.height)/2+60)


if __name__ == '__main__':
    main()
