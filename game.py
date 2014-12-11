from tkinter import *
import random
import itertools
import time
import turtle
import time
from sys import exit
from random import randint
tk = Tk()
tk.title("Bollar")
tk.resizable(1,1)
tk.wm_attributes("-topmost", 1)
canvas = list()


class App:
    def write_slogan(self):
            print ("Here are the rules:")
            print ("In one turn remove as many balls as you want from one row")
            print ("After your turn click on GO!")
            print ("The one who has to pick up the last ball loses")
            print ("By the way I'm on Easy level")
            print ("Best of Luck!")       
    def callgo(self,event,rows):
        y=[rows.retlen(0),rows.retlen(1),rows.retlen(2)]
        k=max(y[0],y[1],y[2])
        i=0
        d=0
        a.removing = list()
        for p in list(itertools.permutations([1,2,0])):
            if(y[p[0]]==0 and y[p[1]] == 0 and y[p[2]]==1):
                print("YOU  WIN!");
                sys.exit()
        for p in list(itertools.permutations([1,2,0])):
            if(y[p[0]]==0 and y[p[1]] == 0 and y[p[2]]!=1):
                 d=y[p[2]]-1
                 while i<d:
                     rows.remove(p[2])
                     i=i+1
                 print("YOU  LOSE!")
                 return
                 
             
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==0 and y[p[1]]==1:
                d=y[p[2]]
                while d>=0:
                    rows.remove(p[2])
                    d = d-1
                print("YOU  LOSE!")
                #flash = Splash(tk)
                sys.exit();
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==1 and y[p[2]]==1 and y[p[1]]==1:
                rows.remove(p[1])
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==0 and y[p[2]]==y[p[1]]:
                d=y[p[2]]
                if y[p[2]]==1:
                    rows.remove(p[2])
                    print("YOU  LOSE!")
                    #flash = Splash(tk)
                    sys.exit();
                while d>=0:
                    rows.remove(p[2])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]!=0 and y[p[2]]==y[p[1]]:
                d=y[p[0]]
                while d>=0:     
                        rows.remove(p[0])
                        d=d-1
                return
                
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==0 and y[p[2]] != y[p[1]]:
                d=max(y[p[1]],y[p[2]])-min(y[p[1]],y[p[2]])
                if y[p[1]]>y[p[2]]: 
                    while d>0:     
                        rows.remove(p[1])
                        d=d-1
                    return 
                else: 
                    while d>0:                                 
                        rows.remove(p[2])
                        d=d-1
                    return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]>1 and y[p[2]]%2==0 and y[p[1]]==y[p[2]]+1:
                d=y[p[0]]
                while d>1:
                    rows.remove(p[0])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==1 and y[p[2]]%2==0 and y[p[1]]>y[p[2]]+1:
                d=y[p[1]]
                while d>=(y[p[2]]+1):
                    rows.remove(p[1])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==1 and y[p[2]]%2==1 and y[p[1]]>y[p[2]]:
                d=y[p[1]]
                while d>=(y[p[2]]-1):
                    rows.remove(p[1])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==1 and y[p[2]]%2==0 and y[p[1]]==y[p[2]]-1:
               
                while d>=2:
                    rows.remove(p[2])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==1 and y[p[2]]%2==0 and y[p[1]]!=0:
                d=y[p[1]]
                while d>=(y[p[2]]+1):
                    rows.remove(p[1])
                    d=d-1
                return
        
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]>2 and y[p[2]]%4==0 and y[p[1]]==y[p[2]]+2:
                d=y[p[0]]-2
                while d>2:
                    rows.remove(p[0])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==2 and y[p[2]]>4 and y[p[1]]==6:
                d=y[p[2]]
                while d>4:
                    rows.remove(p[2])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==2 and y[p[2]]==4 and y[p[1]]>6:
                d=y[p[1]]
                while d>6:
                    rows.remove(p[1])
                    d=d-1
                return
        
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==5 and y[p[2]]==7 and y[p[1]]>2:
                d=y[p[1]]
                while d>2:
                    rows.remove(p[1])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]>5 and y[p[2]]==7 and y[p[1]]==2:
                d=y[p[0]]
                while d>=5:
                    rows.remove(p[0])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==5 and y[p[2]]>7 and y[p[1]]==2:
                d=y[p[2]]
                while d>=7:
                    rows.remove(p[2])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]>3 and y[p[2]]==5 and y[p[1]]==6:
                d=y[p[0]]              
                while d>3:
                    rows.remove(p[1])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==3 and y[p[2]]>5 and y[p[1]]==6:
                d=y[p[2]]              
                while d>5:
                    rows.remove(p[2])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==3 and y[p[2]]==5 and y[p[1]]>6:
                d=y[p[1]]              
                while d>6:
                    rows.remove(p[1])
                    d=d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]] == 1 and y[p[1]]==1:
                d=y[p[2]]
                while d>1:
                    rows.remove(p[2])
                    d = d-1
                return
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]] == 0 and y[p[1]]==0:
                d=y[p[2]]
                while d>1:
                    rows.remove(p[2])
                    d = d-1
                print("YOU  LOSE!")
                flash = Splash(tk)
                return
        for p in list(itertools.permutations([1,2,0])):
            #[1,3,5]->[1,3,2],[1,5,6]->[1,5,4]
            t = randint(1,8)
            if y[p[0]]==1 and y[p[1]]%2 == 1 and y[p[2]] == y[p[1]] + t:
                while t>=0:
                    y[p[2]].remove()
                    t=t-1
                return
        for p in list(itertools.permutations([1,2,0])):
            d=k
            if y[p[0]]==k:
                rows.remove(p[0])
                return
            if y[p[1]]==k:
                rows.remove(p[1])
                return
            if y[p[2]]==k:
                rows.remove(p[2])
                return
             
        for p in list(itertools.permutations([1,2,0])):
            if y[p[0]]==k:
                q=[rows.retlen(p[1]),rows.retlen(p[2])]
                h=max(q)
                w=min(q)
                if w>=k-h:
                     
                     if q[0]==h:
                         d=q[1]
                         while d>(k-h):
                             rows.remove(p[2])
                             d=d-1
                         return
                     else:
                         d=q[0]
                         while d>(k-h):
                             rows.remove(p[1])
                             d=d-1
                         return
                elif w<(k-h):
                     d=k-(h-w)
                     while i<=d:
                          rows.remove(p[0])
                          i=i+1
                     return
        
                    
                    
                
        
    def __init__(self, master):
        frame = master
        self.slogan = Button(frame,
                         text="Rules",fg="green",
                         command=self.write_slogan)
        self.slogan.pack(side=LEFT)
        self.button1=Button(frame,text="Go!")
        self.button1.pack(side=RIGHT)
        self.button1.bind("<Button-1>",lambda event, arg=a: self.callgo(event,arg))

class Ball:
    def __init__(self, canvas, color,posx,posy,row):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, posx, posy)
        self.row = row
    def getId(self):
        return self.id
 

class Row:
    removing = list()
    rowsd = list()
    def __init__(self, number):
        for ill in range(number):
            self.A = list()
            canvas.append(Canvas(tk, width=200, height=100,bg="blue"))
            for jll in range(randint(2,8)):
                self.ball=Ball(canvas[ill],'red',20*jll,20+(5*(ill-1)), ill+1)
                self.A.append(self.ball)
            self.rowsd.append(self.A)
            canvas[ill].bind("<Button-1>",lambda event, arg=ill: self._remove(event,arg))
            canvas[ill].pack()
            tk.update()
            
    def _remove(self, event,rownum):
        try:
            if len(self.removing)== 0 or rownum == self.removing[0]:
                canvas[rownum].delete(self.rowsd[rownum].pop().getId())
                self.removing.append(rownum)
                tk.update()
        except:
             pass
    def remove(self, rownum):
        try:
            canvas[rownum].delete(self.rowsd[rownum].pop().getId())
            tk.update()
        except:
             pass
    def retlen(self,rownum):
        return len(self.rowsd[rownum])
            
     
 
    
     
a = Row(3)
tk.update_idletasks()
app=App(tk)
tk.update()



    

