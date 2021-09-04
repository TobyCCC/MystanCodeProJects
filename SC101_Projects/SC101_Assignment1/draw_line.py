"""
File: .py
Name: draw_line
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 20                                                                                   #圓的大小
window = GWindow(title="Draw line")
second_click = False                                                                        #判斷是否是第二次點擊
position = [0, 0]                                                                           #儲存原點的位置


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_lines)                                                               #畫線的主程式


def draw_lines(mouse):
    global second_click
    if second_click:                                                                        #如果是第二次點擊
        origin = window.get_object_at(position[0], position[1])                             #取得第一次點擊圓圈的儲存位置
        line = GLine(origin.x+origin.width/2, origin.y+origin.height/2, mouse.x, mouse.y)   #畫線
        window.add(line)
        window.remove(origin)                                                               #將圓刪除
        second_click = False
    else:
        origin = GOval(SIZE, SIZE)
        window.add(origin, mouse.x-origin.width/2, mouse.y-origin.height/2)
        second_click = True
        position[0] = mouse.x                                                               #暫存x,y座標
        position[1] = mouse.y



if __name__ == "__main__":
    main()
