from tkinter import *

homepage = Tk()
homepage.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
homepage.resizable(False,False)
homepage.title("Musayzing") # Title each page has different one
homepage.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage

def log_in_page():
    homepage.destroy() # this deletes the previous page which is homepage

    loginpage = Tk()
    loginpage.geometry("800x500+400+170")
    loginpage.title("Log In")
    loginpage.configure(background='light grey') #light grey pages includes the #loginpage/ #questionspage/ #resultpage
    
    def games_page():
        loginpage.destroy()
        
        gamespage = Tk()
        gamespage.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
        gamespage.title("Games") # Title each page has different one
        gamespage.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage
        
        def play_page():
            gamespage.destroy()

            playpage = Tk()
            playpage.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            playpage.title("Playx") # Title each page has different one
            playpage.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage

        label=Label(gamespage, text="Games", font=('Times_New_Romans', 50))
        label.place(x=280, y=50)
        button4 = Button(gamespage, text="Missing Lyrics",command=play_page, font=('Times_New_Romans', 20))
        button4.place(x=250, y=200, height=40, width=300)
        button5 = Button(gamespage, text="Song Artist", command=play_page, font=('Times_New_Romans', 20))
        button5.place(x=250, y=280, height=40, width=300)
        button6 = Button(gamespage, text="Artist Age", command=play_page, font=('Times_New_Romans', 20))
        button6.place(x=250, y=360, height=40, width=300)
        gamespage.mainloop()


    entry_username = Entry(loginpage)
    entry_username.place(x=250, y=200, height=40, width=300)
    entry_password = Entry(loginpage)
    entry_password.place(x=250, y=250, height=40, width=300)
    label=Label(loginpage, text="Connecting", font=('Times_New_Romans', 50))
    label.place(x=230, y=50)
    button3 = Button(loginpage, command=games_page, text="Log in", font=('Times_New_Roman', 15), height=1, width=20)
    button3.place(x=290, y=320)


    loginpage.mainloop() #this is the boundary for the log in page



label = Label(homepage, text="MUSAYZING", font=('Times_New_Romans', 50))  #Label function and info
label.place(x=200, y=50) # placement of where they are in my page
button1 = Button(homepage , text="Connect with Facebook",command=log_in_page, font=('Times_New_Romans', 15), height=1, width=20)
button1.place(x=290, y=230)
button2 = Button(homepage, text="Connect with Ormiston",command=log_in_page, font=('Times_New_Roman', 15), height=1, width=20)
button2.place(x=290, y=320)




homepage.mainloop() #this is the boundary for the whole program