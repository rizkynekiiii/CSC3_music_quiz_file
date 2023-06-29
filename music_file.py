import tkinter as tk
from tkinter import *
from tkinter import font

root=Tk()

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")

#This shows the Labels on what page is what
label1=Label(page1 ,text="MUSAYZING", font=('Times_New_Romans', 25))
label1.pack(pady=20)

label2=Label(page2 ,text="CONNECTING", font=('Times_New_Romans', 25))
label2.pack(pady=20)

label3=Label(page3 ,text="GAMES", font=('Times_New_Romans', 25))
label3.pack(pady=20)

#Buttons 
button1 = Button(page1, text="Connect with Facebook", command=lambda: page2.tkraise(), font=('Times_New_Romans', 25))
button1.pack()
button2 = Button(page1, text="Connect with Ormiston", command=lambda: page2.tkraise(), font=('Times_New_Romans', 25))
button2.pack()
button3 = Button(page2, text="Log in", command=lambda: page3.tkraise(), font=('Times_New_Romans', 25))
button3.pack()
page1.tkraise()
root.minsize(height=500, width=900)
root.title("Musayzing")
root.configure(background='white')
root.mainloop()
