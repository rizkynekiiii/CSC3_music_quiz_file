from tkinter import *

artistage = None
games_page = None
question1 = None

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
        
        def missing_lyrics():
            gamespage.destroy()

            missing = Tk()
            missing.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            missing.title("Play") # Title each page has different one
            missing.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage

            label=Label(missing, text="Missing Lyrics", font=('Times_New_Romans', 50))
            label.place(x=200, y=50)
            button8 = Button(master=missing, text="Play",command=play_missing1, font=('Times_New_Romans', 40))
            button8.place(x=310, y=280,  height=100, width=200)
            missing.mainloop()

        def play_missing1():
            question1 = Tk()
            question1.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            question1.title("Question1") # Title each page has different one
            question1.configure(background='white') # black pages includes the #homepage/ #gamesectionpage/ #playpage

            label=Label(question1, text="Question 1/5", font=('Times_New_Romans', 50))
            label.place(x=230, y=40)
            label=Label(question1, text="You needed somebody, baby, put it on me, I can be that ____, said I can be that body", font=('Times_New_Romans', 14))
            label.place(x=40, y=150)
            button1=Button(question1, text="lady",command=play_missing2, font=('Times_New_Romans', 30))
            button1.place(x=150, y=230, width=200, height=70)
            button2=Button(question1,text="bludy" ,command=play_missing2,font=('Times_New_Romans', 30))
            button2.place(x=460, y=230, width=200, height=70)
            button3=Button(question1,text="body" ,command=play_missing2,font=('Times_New_Romans', 30))
            button3.place(x=150, y=350, width=200, height=70)
            button4=Button(question1,text="gay" ,command=play_missing2,font=('Times_New_Romans', 30))
            button4.place(x=460, y=350, width=200, height=70)
            question1.mainloop()
        def play_missing2():

            question2 = Tk()
            question2.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            question2.title("Question2") # Title each page has different one
            question2.configure(background='white') # black pages includes the #homepage/ #gamesectionpage/ #playpage
            label=Label(question2, text="Question 2/5", font=('Times_New_Romans', 50))
            label.place(x=230, y=40)
            label=Label(question2, text="His love never felt _____, switch sides and I'm beside you ", font=('Times_New_Romans', 14))
            label.place(x=160, y=150)
            button1=Button(question2, text="right",command=play_missing2, font=('Times_New_Romans', 30))
            button1.place(x=150, y=230, width=200, height=70)
            button2=Button(question2,text="good" ,command=play_missing2,font=('Times_New_Romans', 30))
            button2.place(x=460, y=230, width=200, height=70)
            button3=Button(question2,text="ass" ,command=play_missing2,font=('Times_New_Romans', 30))
            button3.place(x=150, y=350, width=200, height=70)
            button4=Button(question2,text="decent" ,command=play_missing2,font=('Times_New_Romans', 30))
            button4.place(x=460, y=350, width=200, height=70)
            question2.mainloop()

        def song_artist():
            gamespage.destroy()
            songartist = Tk()
            songartist.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            songartist.title("Play") # Title each page has different one
            songartist.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage

            label=Label(songartist, text="Song Artist", font=('Times_New_Romans', 50))
            label.place(x=240, y=50)
            button8 = Button(songartist, text="Play",command=play_artist, font=('Times_New_Romans', 40))
            button8.place(x=310, y=280,  height=100, width=200)
            songartist.mainloop()

        def play_artist():

            question1_artist = Tk()
            question1_artist.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            question1_artist.title("Question1") # Title each page has different one
            question1_artist.configure(background='white') # black pages includes the #homepage/ #gamesectionpage/ #playpage
            question1_artist.mainloop()

        def artist_age():
            gamespage.destroy()
            artistage = Tk()
            artistage.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            artistage.title("Play") # Title each page has different one
            artistage.configure(background='black') # black pages includes the #homepage/ #gamesectionpage/ #playpage

            label=Label(artistage, text="Artist Age", font=('Times_New_Romans', 50))
            label.place(x=260, y=50)
            button9 = Button(artistage, text="Play",command=play_age, font=('Times_New_Romans', 40))
            button9.place(x=310, y=280,  height=100, width=200)
            artistage.mainloop()

        def play_age():

            question1_age = Tk()
            question1_age.geometry("800x500+400+170") # This is the fixed layout on how big my pages would be
            question1_age.title("Question1") # Title each page has different one
            question1_age.configure(background='white') # black pages includes the #homepage/ #gamesectionpage/ #playpage
            question1_age.mainloop()



        label=Label(gamespage, text="Games", font=('Times_New_Romans', 50))
        label.place(x=280, y=50)
        button4 = Button(gamespage, text="Missing Lyrics",command=missing_lyrics, font=('Times_New_Romans', 20))
        button4.place(x=250, y=200, height=40, width=300)
        button5 = Button(gamespage, text="Song Artist", command=song_artist, font=('Times_New_Romans', 20))
        button5.place(x=250, y=280, height=40, width=300)
        button6 = Button(gamespage, text="Artist Age", command=artist_age, font=('Times_New_Romans', 20))
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