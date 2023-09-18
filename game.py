from tkinter import *
import random

root=Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title('Stone-Paper-Scissors')
root.config(bg ='#424242')
Label(root, text = 'Stone Paper Scissors' , font='arial 20 bold', bg = 'seashell2').pack()
user_take = StringVar()
Label(root, text = 'Choose any one: stone, paper or scissors' , font='arial 15 bold', bg = 'whitesmoke').place(x = 52,y=70)

def Opponent():
    comp_pick = random.randint(1,3)
    if comp_pick == 1:
        comp_pick = 'stone'
    elif comp_pick ==2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'
    return comp_pick

Result = StringVar()
Userpoint=0; Comppoint=0;
UP=IntVar(); CP=IntVar()

def Stone():
    user_take='stone'
    global Userpoint; global Comppoint
    comp_pick=Opponent()
    if user_take == comp_pick:
        Result.set('tie,you both select same')
    elif comp_pick == 'paper':
        Result.set('you loose,computer selects paper')
        Comppoint+=1
        CP.set(Comppoint)
    elif comp_pick == 'scissors':
        Result.set('you win,computer selects scissors')
        Userpoint+=1
        UP.set(Userpoint)

def Paper():
    user_take='paper'
    comp_pick=Opponent()
    global Userpoint; global Comppoint
    if user_take == comp_pick:
        Result.set('tie,you both select same')
    elif comp_pick == 'scissors':
        Result.set('you loose,computer selects scissors')
        Comppoint+=1
        CP.set(Comppoint)
    elif comp_pick == 'stone':
        Result.set('you win,computer selects stone')
        Userpoint+=1
        UP.set(Userpoint)

def Scissors():
    user_take='scissors'
    comp_pick=Opponent()
    global Userpoint; global Comppoint
    if user_take == comp_pick:
        Result.set('tie,you both select same')
    elif comp_pick == 'stone':
        Result.set('you loose,computer selects stone')
        Comppoint+=1
        CP.set(Comppoint)
    elif comp_pick == 'paper':
        Result.set('you win,computer selects paper')
        Userpoint+=1
        UP.set(Userpoint)

def Reset():
    Result.set("") 
    UP.set(0)
    CP.set(0)
    user_take.set("")
    global Userpoint; global Comppoint
    Userpoint=0; Comppoint=0

def Exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='whitesmoke',width = 50,).place(x=70, y = 250)
Button(root, font = 'arial 15 bold', text = 'STONE'  ,padx =5,bg ='lightsteelblue1' ,command = Stone).place(x=70,y=160)
Button(root, font = 'arial 15 bold', text = 'PAPER'  ,padx =5,bg ='lightsteelblue1' ,command = Paper).place(x=189,y=160)
Button(root, font = 'arial 15 bold', text = 'SCISSORS'  ,padx =5,bg ='lightsteelblue1' ,command = Scissors).place(x=305,y=160)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='lightsteelblue1' ,command = Reset).place(x=150,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='lightsteelblue1' ,command = Exit).place(x=280,y=310)
Label(root, text = 'Your Points: ' , font='arial 10 bold', bg = '#424242', fg='white').place(x=120,y=380)
Label(root, textvariable= UP, font='arial 10 bold', bg='#424242', fg='white').place(x=200,y=380)
Label(root, text = 'Computer Points: ' , font='arial 10 bold', bg = '#424242', fg='white').place(x=250,y=380)
Label(root, textvariable= CP, font='arial 10 bold', bg='#424242', fg='white').place(x=363,y=380)

root.mainloop()