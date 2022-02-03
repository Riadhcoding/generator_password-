from tkinter import *
import string
from random import randint,choice
import webbrowser

def open():
    webbrowser.open_new('https://www.youtube.com/c/riadhcoding')


def password():
    password_min = 12
    password_max = 12
    all_password = string.ascii_letters + string.punctuation +string.digits
    generator_password = ''.join(choice(all_password)
    for x in range(randint(password_min,password_max)))
    display.delete(0,END)
    display.insert(0,generator_password)

window = Tk()
window.title('Password Generator')
window.geometry('480x480')
window.iconbitmap('icon_password.ico')
window.config(bg='#b5007c')
big_title = Label(window,text='Password Generator',font=('roboto',30),bg='#b5007c',fg='white')
big_title.pack()
width = 250
height = 250
image = PhotoImage(file='image.jpg').zoom(10).subsample(15)
canvas = Canvas(window,width=width,height=height,bg='#b5007c',bd=0,highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.pack()
display = Entry(window,font=('roboto',30),bg='white',fg='black')
display.pack()
button = Button(window,font=('roboto',25),border=0,text='Generator',bg='red',fg='white',command=password)
button.pack(expand=YES)
menu_bar = Menu(window)
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',command=password)
file_menu.add_command(label='Youtube',command=open)
file_menu.add_command(label='Exit',command=window.quit)
menu_bar.add_cascade(label='File',menu=file_menu,font=(15))
window.config(menu=menu_bar)




window.mainloop()