"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


repeat_time = 0                                                                 #紀錄點擊次數


window = GWindow(800, 500, title='bouncing_ball.py')
title = GLabel(f"執行第{repeat_time}次")                                         #顯示點擊次數
ball = GOval(SIZE, SIZE)
on_going = False                                                                #判斷上一次是否有執行完


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    window.add(title, 0, title.height)
    onmouseclicked(simulate)


def simulate(mouse):
    global repeat_time, on_going
    if repeat_time >= 3 or on_going:
        pass
    else:
        on_going = True                                                         #代表正在執行
        repeat_time += 1
        title.text = f"執行第{repeat_time}次"
        vy_origin = 0                                                           #紀錄初始/彈跳後y向速度
        frame = 0                                                               #幀數
        bounce = True                                                           #判斷是否不是反彈後第一幀
        while True:
            if ball.x >= window.width:                                          #整顆球超出右邊界線
                window.add(ball, START_X, START_Y)
                on_going = False                                                #取消執行狀態
                break
            else:
                vy = uniform_acceleration(vy_origin, frame)                     #垂直速度
                ball.move(VX, vy)
                if ball.y+ball.height >= window.height and bounce:              #反彈
                    frame = 0
                    vy_origin = -REDUCE*vy
                    bounce = False                                              #判斷下一次為反彈後第一幀，避免球卡在底部
                else:
                    frame += 1
                    bounce = True
            pause(DELAY)


def uniform_acceleration(vy_origin, frame):
    """
    計算等加速度的位移
    :param vy_origin: int, 原始速度
    :param frame: int, 時間（幀數）
    :return: int, 速度
    """
    return vy_origin + GRAVITY * frame





if __name__ == "__main__":
    main()
