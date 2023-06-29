from tkinter import *

root = Tk()

root.minsize(height=500, width=900)
root.title("Musayzing")
root.configure(background='white')

label = Label(root, text="MUSAYZING", font=('Times_New_Romans', 25)) 
label.place()
button1 = Button(root , text="Connect with Facebook", font=('Times_New_Romans', 15))
button1.place(x=450, y=250, anchor=CENTER)
button2 = Button(root, text="Connect with Ormiston", font=('Times_New_Roman', 15))
button2.pack(anchor= CENTER)




root.mainloop()