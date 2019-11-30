import tkinter
from tkinter import*
import random
import time
root=Tk()
#canvas = Canvas(root,width=300,height=160)
#image=imageTK.PhotoImage(Image.open("C:\\Users\\92303\\Downloads\\images.jpeg"))
#canvas.create_image(0,0,ANCHOR=NW,image=image)
#canvas.pack()
root.geometry("1600x800+0+0")
root.title("Clustering People using Scrap Data")
Tops=Frame(root,width=1600,height=50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)
#f1=Frame(root,width=800,height=700,bg="powder blue",relief=SUNKEN)
#f1.pack(side=LEFT)
#f2=Frame(root,width=300,height=700,bg="powder blue",relief=SUNKEN)
#f2.pack(side=RIGHT)
#=================================Time==========================
localtime=time.asctime(time.localtime(time.time()))
#=================================Info==========================
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Clustering People using Scrap Data",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#===============================Buttons===========================
def star_program():
    print("start")
start_button = Button(root, text="IMPORT FILE",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue",command=star_program)

cancel_button = Button(root,text="CLUSTER VALUE",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue",command=quit)

center_button = Button(root,text="PROCESS ALGO",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue",command=quit)
start_button.pack(side=TOP)
cancel_button.pack(side=TOP)
center_button.pack(side=TOP)

root.mainloop();
