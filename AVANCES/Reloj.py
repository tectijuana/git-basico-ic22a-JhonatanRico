rom tkinter import *
import time

root = Tk()
root.title("Clock")
width = 300
height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="light blue")


Top = Frame(root, width=400, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=400)
Mid.pack(side=TOP, expand=1)
 
 

lbl_title = Label(Top, text="Python: Simple Digital Clock", width=200, font=("arial", 10))
lbl_title.pack(fill=X)
 
clock = Label(Mid, font=('times', 20 , 'bold'), fg="green", bg="light blue")
clock.pack()


def tick():
    setTime = time.strftime('%I: %M: %S %p')
    clock.config(text=setTime )
    clock.after(200, tick)


 
if __name__ == '__main__':
    tick()
    root.mainloop()