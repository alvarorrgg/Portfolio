from tkinter import *
import Graphs
import math as m
""" 
     SCROLLBAR MOVEMENT FUNCTIONS


"""
def rollWheelYaxis(event):

    direction = 0

    if event.num == 5 or event.delta == -120:

        direction = 20

    if event.num == 4 or event.delta == 120:

        direction = -20

    event.widget.yview_scroll(direction, UNITS)



def downKey(event):

     event.widget.yview_scroll(20, UNITS)



def upKey(event):

     event.widget.yview_scroll(-20, UNITS)



def leftKey(event):

     event.widget.xview_scroll(-20, UNITS)



def rightKey(event):

     event.widget.xview_scroll(20, UNITS)




"""
     MAIN FUNCTION OF FILE,

          REPRESENTS THE GRAPH IN A CANVAS



"""
def show_graph(graph):

     """

          given a graph it will draw the graph and its connections.
     
     """
     """
          In this part we create all about the canvas (scrollbar and config)
     
     """
     #create Root

     root = Tk()



     #createCanvas

     c = Canvas(root, scrollregion=(0,0,3000,3000), height=800, width=1500,background="grey")



     #YaxisScrollbar

     sy = Scrollbar(root, command=c.yview)

     sy.pack(side=RIGHT, fill=Y)

     c.configure(yscrollcommand=sy.set)



     #XAxysScrollBar

     sx=Scrollbar(root,command=c.xview,orient=HORIZONTAL)

     sx.pack(side=BOTTOM, fill=X)

     c.configure(yscrollcommand=sy.set,xscrollcommand=sx.set,yscrollincrement='2',xscrollincrement='2')

     c.pack(side=LEFT)



     """
          Here we will bind the keys correctly to improve the scrollbar movement
     
     """
     
     root.bind('<MouseWheel>', lambda event: rollWheelYaxis(event))
     c.bind('<Down>',downKey)
     c.bind('<Up>',upKey)
     c.bind('<Left>', leftKey)
     c.bind('<Right>', rightKey)
     c.focus_set()





     """

          Drawing the graph vertex
     
     """
     n=Graphs.graph.get_number_vertex(graph)
     
     
     radio=(2000+m.pow(n,1.3))-(1000-m.pow(n,1.3))

     #createOval(x0,y0,x1,y1,color)

     c.create_oval(1000-m.pow(n,1.3),1000-m.pow(n,1.3),2000+m.pow(n,1.3),2000+m.pow(n,1.3))




     long_cf=2*m.pi*radio

     tramo=long_cf/n

     tramo_en_ang=(tramo/long_cf)*360

     x=m.cosh(tramo_en_ang)

     y=m.sinh(tramo_en_ang)

     a=m.sqrt(m.pow(x,2)+m.pow(y,2))

     x=(x/a)*radio

     y=(y/a)*radio

          #create_text()

     c.create_text(20, 30, anchor=W, font="Purisa",text="Num of vertex"+str(tramo_en_ang)+","+str(tramo))

     #This is the main loop for the canvas to work
     root.mainloop()




"""
     if file is main file

"""
if __name__=="__main__":

     g=Graphs.graph()

     g.create_random_graf()

     show_graph(g)
