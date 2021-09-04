"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GArc, GPolygon
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked
from draw_line import draw_lines



pixel_x = 0
pixel_y = 0
pixel = GLabel(f"({pixel_x},{pixel_y})")
window = GWindow(800, 600)


def main():
    """
    創作理念:學鋼琴的孩子不會變壞，學程式的應該也不會吧？
    """
    window.add(pixel, 0, pixel.height)
    onmouseclicked(draw_lines)
    onmousemoved(find_pixel)                                                    #找出滑鼠座標
    build_main_body()                                                           #畫出中間的圓形
    build_spike_protein_1()                                                     #畫出旁邊的棘蛋白
    build_spike_protein_2()
    build_spike_protein_3()
    build_spike_protein_4()
    build_spike_protein_5()
    build_spike_protein_6()
    build_spike_protein_7()
    build_spike_protein_8()
    build_spike_protein_9()
    build_spike_protein_10()
    build_spike_protein_11()
    build_spike_protein_12()
    build_left_eye()                                                            #畫出眼睛
    build_right_eye()
    build_smile()                                                               #畫出微笑
    build_blush_right()                                                         #畫出腮紅
    build_blush_left()
    build_dialog_box()                                                          #畫出對話框



def find_pixel(mouse):
    """
    顯示出滑鼠座標
    """
    global pixel_x, pixel_y
    pixel_x = mouse.x
    pixel_y = mouse.y
    pixel.text = f"({pixel_x},{pixel_y})"


def build_main_body():
    """
    建造主體
    """
    main_body = GOval(300, 300)
    main_body.color = (150, 152, 144)
    main_body.filled = True
    main_body.fill_color = (150, 152, 144)
    window.add(main_body, (window.width - main_body.width) / 2, (window.height - main_body.height) / 2 + 30)

def build_spike_protein_1():
    spike_protein_main = GRect(20, 80)                                                  #棘蛋白的長柱狀
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(50, 50)                                                  #棘蛋白的頭
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main, 401-11, 160-40)
    window.add(spike_protein_head, 401-25, 127-47)

def build_spike_protein_2():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((485, 214))
    spike_protein_main.add_vertex((498, 223))
    spike_protein_main.add_vertex((533, 178))
    spike_protein_main.add_vertex((516, 172))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(45, 45)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 532-spike_protein_head.width/2, 167-spike_protein_head.height/2)


def build_spike_protein_3():
    spike_protein_main = GRect(70, 18)
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(48, 48)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main, 546, 312)
    window.add(spike_protein_head, 632-24, 321-24)


def build_spike_protein_4():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((526, 402))
    spike_protein_main.add_vertex((516, 417))
    spike_protein_main.add_vertex((554, 447))
    spike_protein_main.add_vertex((562, 434))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(40, 40)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 568-spike_protein_head.width/2, 448-spike_protein_head.height/2)


def build_spike_protein_5():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((511, 519))
    spike_protein_main.add_vertex((498, 525))
    spike_protein_main.add_vertex((465, 461))
    spike_protein_main.add_vertex((478, 457))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(48, 48)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 514-spike_protein_head.width/2, 541-spike_protein_head.height/2)


def build_spike_protein_6():
    spike_protein_main = GRect(18, 50)
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(54, 54)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main, 388, 473)
    window.add(spike_protein_head, 388+9-27, 473+45)


def build_spike_protein_7():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((533, 268))
    spike_protein_main.add_vertex((537, 279))
    spike_protein_main.add_vertex((559, 263))
    spike_protein_main.add_vertex((554, 254))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(35, 35)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 568-spike_protein_head.width/2, 253-spike_protein_head.height/2)


def build_spike_protein_8():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((299, 438))
    spike_protein_main.add_vertex((318, 446))
    spike_protein_main.add_vertex((271, 485))
    spike_protein_main.add_vertex((259, 471))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(48, 48)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 247-spike_protein_head.width/2, 492-spike_protein_head.height/2)


def build_spike_protein_9():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((257, 336))
    spike_protein_main.add_vertex((261, 351))
    spike_protein_main.add_vertex((220, 352))
    spike_protein_main.add_vertex((217, 339))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(40, 40)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 208-spike_protein_head.width/2, 345-spike_protein_head.height/2)


def build_spike_protein_10():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((264, 297))
    spike_protein_main.add_vertex((268, 286))
    spike_protein_main.add_vertex((228, 274))
    spike_protein_main.add_vertex((226, 284))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(38, 38)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 218-spike_protein_head.width/2, 278-spike_protein_head.height/2)


def build_spike_protein_11():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((281, 257))
    spike_protein_main.add_vertex((285, 245))
    spike_protein_main.add_vertex((222, 215))
    spike_protein_main.add_vertex((202, 217))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(46, 46)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 215-spike_protein_head.width/2, 217-spike_protein_head.height/2)


def build_spike_protein_12():
    spike_protein_main = GPolygon()
    spike_protein_main.add_vertex((343, 201))
    spike_protein_main.add_vertex((332, 207))
    spike_protein_main.add_vertex((319, 174))
    spike_protein_main.add_vertex((330, 168))
    spike_protein_main.color = (150, 152, 144)
    spike_protein_main.filled = True
    spike_protein_main.fill_color = (150, 152, 144)
    spike_protein_head = GOval(36, 36)
    spike_protein_head.color = (150, 152, 144)
    spike_protein_head.filled = True
    spike_protein_head.fill_color = (150, 152, 144)
    window.add(spike_protein_main)
    window.add(spike_protein_head, 320-spike_protein_head.width/2, 159-spike_protein_head.height/2)


def build_left_eye():
    left_eye_main = GOval(50, 60)                                                       #眼睛
    left_eye_main.filled = True
    pupil_1 = GOval(20,22)
    pupil_1.color = "white"                                                             #瞳孔
    pupil_1.filled = True
    pupil_1.fill_color = "white"
    pupil_2 = GOval(10, 10)
    pupil_2.color = "white"
    pupil_2.filled = True
    pupil_2.fill_color = "white"
    window.add(left_eye_main, 340-25, 293-30)
    window.add(pupil_1, 333-10, 285-11)
    window.add(pupil_2, 349-10, 307-10)


def build_right_eye():
    right_eye_main = GOval(50, 60)
    right_eye_main.filled = True
    pupil_1 = GOval(20, 22)
    pupil_1.color = "white"
    pupil_1.filled = True
    pupil_1.fill_color = "white"
    pupil_2 = GOval(10, 10)
    pupil_2.color = "white"
    pupil_2.filled = True
    pupil_2.fill_color = "white"
    window.add(right_eye_main, 460 - 25, 293 - 30)
    window.add(pupil_1, 333 + 120 - 10, 285 - 11)
    window.add(pupil_2, 349 + 120 - 10, 307 - 10)


def build_smile():
    smile_left = GArc(100, 140, 180, 150)
    window.add(smile_left, 355, 330)


def build_blush_right():
    blush =  GOval(60, 15)
    blush.color = (243, 181, 182)
    blush.filled = True
    blush.fill_color = (243, 181, 182)
    window.add(blush, 496- blush.width/2, 341-blush.height/2)


def build_blush_left():
    blush =  GOval(60, 15)
    blush.color = (243, 181, 182)
    blush.filled = True
    blush.fill_color = (243, 181, 182)
    window.add(blush, 304- blush.width/2, 341-blush.height/2)


def build_dialog_box():
    box_main =  GRect(340, 60)                                                      #對話框主體
    box_main.color = (54, 87, 182)
    box_main.filled = True
    box_main.fill_color = (176, 177, 230)
    box_triangle = GPolygon()                                                       #對話框的延伸線
    box_triangle.add_vertex((484, 80))
    box_triangle.add_vertex((542, 80))
    box_triangle.add_vertex((472, 142))
    box_triangle.color = (54, 87, 182)
    box_triangle.filled = True
    box_triangle.fill_color = (176, 177, 230)
    box_1 = GLine(485, 80, 541, 80)                                                 #避免對話框中間出現線條
    box_1.color = (176, 177, 230)
    box_word = GLabel("I love stanCode! ¯\_(ツ)_/¯")                                #對話框的文字
    box_word.font = "Comic Sans MS-23"
    window.add(box_main, 453, 20)
    window.add(box_triangle)
    window.add(box_1)
    window.add(box_word, 480, 65)







if __name__ == '__main__':
    main()
