"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + (width-2*GRAPH_MARGIN_SIZE)*year_index/len(YEARS)
    return x_coordinate



def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)

        # draw vertical lines
        canvas.create_line(x_coordinate, GRAPH_MARGIN_SIZE, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)

        # Show year labels
        canvas.create_text(x_coordinate + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        if name in name_data:
            for j in range(len(YEARS)-1):
                # draw the line between every two years
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), find_y_position(name_data[name], j),
                                   get_x_coordinate(CANVAS_WIDTH, j + 1), find_y_position(name_data[name], j+1), width=LINE_WIDTH, fill=COLORS[i])

                # create name/rank labels
                if str(YEARS[j]) in name_data[name]:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, find_y_position(name_data[name], j),
                                       text=f'{name} {name_data[name][str(YEARS[j])]}', anchor=tkinter.SW, fill=COLORS[i])
                else:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX, find_y_position(name_data[name], j),
                                       text=f'{name} *', anchor=tkinter.SW, fill=COLORS[i])

            # create name/rank labels for the last datum (2010)
            if str(YEARS[j+1]) in name_data[name]:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX, find_y_position(name_data[name], j+1),
                                   text=f'{name} {name_data[name][str(YEARS[j+1])]}', anchor=tkinter.SW, fill=COLORS[i])
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1) + TEXT_DX, find_y_position(name_data[name], j+1),
                                   text=f'{name} *', anchor=tkinter.SW, fill=COLORS[i])


def find_y_position(data, year_index):
    """
    Given a dict of rank and a specific year, return the y coordinate of the datum associate with the specific year.
    Input:
        data: dict, the rank in every year of a specific baby name.
        year: int, the index of a specific year we assigned.
    Returns:
        y: int, the y coordinate of the datum.
    """
    year = YEARS[year_index]        # transform year_index into year
    if str(year) in data:
        rank = int(data[str(year)])
        y = GRAPH_MARGIN_SIZE + rank / 1000 * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2)

    # if the baby name rank over 1000 in that year, place the datum on the bottom of the canvas
    else:
        y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    return y



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
