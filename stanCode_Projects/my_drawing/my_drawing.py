"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=1200,height=600)
    body = GRect(200, 300, x=200, y=150)
    head = GOval(200,200,x=200,y=50)
    eye = GOval(170,120,x=250,y=130)
    left_foot = GRect(80,100,x=200,y=450)
    right_foot = GRect(80,100,x=320,y= 450)
    back = GPolygon()
    back.add_vertex((200,200))
    back.add_vertex((130,220))
    back.add_vertex((130,400))
    back.add_vertex((200,400))
    handle_1 = GRect(40,100,x=500,y=250)
    handle_2 = GRect(80,40,x=420,y=280)
    knife = GPolygon()
    knife.add_vertex((540,280))
    knife.add_vertex((570,260))
    knife.add_vertex((590,275))
    knife.add_vertex((610,265))
    knife.add_vertex((640,315))
    knife.add_vertex((540,315))

    head.filled=True
    body.filled=True
    eye.filled=True
    back.filled=True
    handle_1.filled=True
    left_foot.filled=True
    right_foot.filled=True
    handle_2.filled=True
    knife.filled=True

    head.fill_color='red'
    body.fill_color='red'
    eye.fill_color='skyblue'
    left_foot.fill_color='red'
    right_foot.fill_color='red'
    back.fill_color='red'
    handle_1.fill_color='black'
    handle_2.fill_color='black'
    knife.fill_color='grey'

    head.color='red'
    body.color='red'
    left_foot.color='red'
    right_foot.color='red'

    window.add(body)
    window.add(head)
    window.add(eye)
    window.add(left_foot)
    window.add(right_foot)
    window.add(back)
    window.add(handle_1)
    window.add(handle_2)
    window.add(knife)

    body2 = GRect(200, 300, x=750, y=150)
    head2 = GOval(200, 200, x=750, y=50)
    eye2 = GOval(170, 120, x=730, y=130)
    left_foot2 = GRect(80, 100, x=750, y=450)
    right_foot2 = GRect(80, 100, x=870, y=450)
    back2 = GPolygon()
    back2.add_vertex((950, 200))
    back2.add_vertex((1020, 220))
    back2.add_vertex((1020, 400))
    back2.add_vertex((950, 400))

    knife2 = GPolygon()
    knife2.add_vertex((700, 200))
    knife2.add_vertex((680, 180))
    knife2.add_vertex((650, 200))
    knife2.add_vertex((650, 400))
    knife2.add_vertex((700, 400))

    head2.filled = True
    body2.filled = True
    eye2.filled = True
    back2.filled = True
    left_foot2.filled = True
    right_foot2.filled = True

    knife2.filled = True

    head2.fill_color = 'purple'
    body2.fill_color = 'purple'
    eye2.fill_color = 'skyblue'
    left_foot2.fill_color = 'purple'
    right_foot2.fill_color = 'purple'
    back2.fill_color = 'purple'
    knife2.fill_color = 'brown'

    head2.color = 'purple'
    body2.color = 'purple'
    left_foot2.color = 'purple'
    right_foot2.color = 'purple'
    knife2.color='brown'

    window.add(body2)
    window.add(head2)
    window.add(eye2)
    window.add(left_foot2)
    window.add(right_foot2)
    window.add(back2)

    label  = GLabel('Among Us',x=450,y=500)
    label.font='Courier-50-italic'
    window.add(label)

    window.add(knife2)
if __name__ == '__main__':
    main()
