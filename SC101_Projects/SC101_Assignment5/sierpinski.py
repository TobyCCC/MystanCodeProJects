"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the layer's order .
	:param length: int, the side length of equilateral triangle.
	:param upper_left_x: x coordinate of triangle.
	:param upper_left_y: y coordinate of triangle.
	:return:
	"""
	# base case
	if order <= 1:
		# base of triangle
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)

		# left side of triangle
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + int(length * 0.866))

		# right side of triangle
		line_3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + int(length * 0.866))

		# draw the triangle on the canvas
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)

	# lower layer
	else:
		# upper left
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)

		# upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)

		# bottom
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * 0.433)


if __name__ == '__main__':
	main()