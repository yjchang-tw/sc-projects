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
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * ((width-2*GRAPH_MARGIN_SIZE)/ len(YEARS))
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
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    width = (CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE+i*width,0,GRAPH_MARGIN_SIZE+i*width,CANVAS_HEIGHT)

        canvas.create_text(get_x_coordinate(CANVAS_WIDTH,i)+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,text=YEARS[i],anchor = tkinter.NW)

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
    num = 0
    for name in lookup_names:

        dot = {}
        for year in YEARS:
            years = str(year)
            if str(year) in name_data[name]:
                rank = name_data[name][years]
            else:
                rank = '*'

            index = (year - YEARS[0]) // 10
            coordinate = []
            x = GRAPH_MARGIN_SIZE+index*(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE)/len(YEARS)

            if rank == '*':
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            elif int(rank) > 1000:
                rank = '*'
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            else:
                y = GRAPH_MARGIN_SIZE + ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 999) * (int(rank) - 1)
            coordinate.append(x)
            coordinate.append(y)
            dot[year] = coordinate
            canvas.create_text(x+ TEXT_DX,y,text=name+' '+rank,anchor=tkinter.SW)
        for i in range(len(YEARS)-1):
            dot_lst1 = dot[YEARS[i]]
            dot_lst2 = dot[YEARS[i+1]]
            print('----------')
            print(dot_lst1)
            print(dot_lst2)
            print('----------')
            canvas.create_line(dot_lst1[0],dot_lst1[1],dot_lst2[0],dot_lst2[1],fill=COLORS[num%len(COLORS)],width = LINE_WIDTH)
        num+=1




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
