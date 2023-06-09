import py_cui
root = py_cui.PyCUI(5,5)

def marco(titulo,coor_x,coor_y):
    root.add_label(titulo,coor_x,coor_y)
color='\xb1[7;33m'
endcolor='\xb1[0;0m'
num=(
    color+'1'+endcolor,color+'2'+endcolor,color+'3'+endcolor,color+'4'+endcolor,color+'5'+endcolor
)

marco(num[0],0,0)
marco(num[1],0,1)
marco(num[2],0,2)
marco(num[3],0,3)
marco(num[4],0,4)
a=1
marco(num[0],a,0)
marco(num[1],a,1)
marco(num[2],a,2)
marco(num[3],a,3)
marco(num[4],a,4)

root.start()

