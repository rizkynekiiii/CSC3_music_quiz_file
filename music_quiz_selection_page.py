from tkinter import *

homepage = Tk()
homepage.geometry("800x500+400+170")
homepage.title("Musayzing")
homepage.configure(background='black')

def log_in_page():
    homepage.destroy()

    loginpage = Tk()
    loginpage.geometry("800x500+400+170")
    loginpage.title("Log In")
    loginpage.configure(background='light grey')

label = Label(homepage, text="MUSAYZING", font=('Times_New_Romans', 50)) 
label.place(x=200, y=50)
button1 = Button(homepage , text="Connect with Facebook",command=log_in_page, font=('Times_New_Romans', 15), height=1, width=20)
button1.place(x=290, y=230)
button2 = Button(homepage, text="Connect with Ormiston",command=log_in_page, font=('Times_New_Roman', 15), height=1, width=20)
button2.place(x=290, y=320)




homepage.mainloop()