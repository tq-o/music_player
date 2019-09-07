import tkinter as tk
from tkinter.constants import END, RIGHT
import readfromexel as exc
from tkinter import messagebox
import random


screen = tk.Tk()
screen.title("Song random - by Thai")

# Opening line for Main Screen (Screen 1):
L = tk.Label(screen, text = "Hi there,", font=('BrowalliaUPC', '20'),
    fg = 'gold', bg ='black')
L.pack()
L = tk.Label(screen, text = "How do you like to choose your song?\n", font=('BrowalliaUPC', '15'),
    fg = 'white', bg ='black')
L.pack()

#  Screen 2_1 for choosing by mood:

def screen2_1():
    screen_2_1 = tk.Tk()
    screen_2_1.title("Choosing by mood")

    #Opening in second screen:
    L2_1 = tk.Label(screen_2_1, text = "Please pick your current mood \n _______ \n")
    L2_1.configure(fg='white', bg = 'black', font=('BrowalliaUPC', '15'))
    L2_1.pack()

    # function for getting random song if love is chosen
    def pickSong1():               
        messagebox.showinfo("Now playing", exc.getName(random.choice(exc.loveHelper())))
    
    # function for getting random song if joy is chosen
    def pickSong2():
        messagebox.showinfo("Now playing", exc.getName(random.choice(exc.joyHelper())))
    
    # function for getting random song if anger is chosen
    def pickSong3():
        messagebox.showinfo("Now playing", exc.getName(random.choice(exc.angerHelper())))
    
    # function for getting random song if sad is chosen
    def pickSong4():
        messagebox.showinfo("Now playing", exc.getName(random.choice(exc.sadHelper())))
    
    # function for getting random song if fear is chosen
    def pickSong5():
        messagebox.showinfo("Now playing", exc.getName(random.choice(exc.fearHelper())))
    
    # Love
    Bs2_1 = tk.Button(screen_2_1, text = "Love", command = pickSong1)
    Bs2_1.configure(wid= 9, height = 1, font=('Proxima Nova Rg', '12'))
    Bs2_1.pack()
    # Joy
    Bs2_2 = tk.Button(screen_2_1, text = "Joy", command = pickSong2)
    Bs2_2.configure(wid= 9, height = 1, font=('Proxima Nova Rg', '12'))
    Bs2_2.pack()
    # Anger
    Bs2_3 = tk.Button(screen_2_1, text = "Anger", command = pickSong3)
    Bs2_3.configure(wid= 9, height = 1, font=('Proxima Nova Rg', '12'))
    Bs2_3.pack()
    # Sadness
    Bs2_4 = tk.Button(screen_2_1, text = "Sadness", command = pickSong4)
    Bs2_4.configure(wid= 9, height = 1, font=('Proxima Nova Rg', '12'))
    Bs2_4.pack()
    # Fear
    Bs2_5 = tk.Button(screen_2_1, text = "Fear", command = pickSong5)
    Bs2_5.configure(wid= 9, height = 1, font=('Proxima Nova Rg', '12'))
    Bs2_5.pack()

    # screen2_1 for moods
    screen_2_1.geometry("350x350")
    screen_2_1.configure(background='black')


# Screen 2 for Customs:

def screen2_2():
    screen_2_2 = tk.Tk()
    screen_2_2.title("Manual random song generator")

    L_2 = tk.Label(screen_2_2, text = "Please enter the values in the boxes\n")
    L_2.configure(bg='black', fg='white', font=('BrowalliaUPC', '15'))
    L_2.grid(row=0,column=0, columnspan=30)
    
    #danceability area: 

    L_dan = tk.Label(screen_2_2, text="Danceability")
    L_dan.configure(bg='black', fg='gold', font=('Proxima Nova Rg', '12'))
    L_dan.grid(row=1,column=0)

        #input from value:
    T1_1 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T1_1.grid(row=1, column=1)
    T1_1.insert(END, "0.0")

    tk.Label(screen_2_2, text="to", font=('Proxima Nova Rg', '12'),
            bg='black', fg='white').grid(row=1,column=2)

        #input to value:
    T1_2 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T1_2.grid(row=1, column=3)
    T1_2.insert(END, "1.0")
    
    #energy area:

    L_en=tk.Label(screen_2_2, text="Energy")
    L_en.configure(bg='black', fg='gold', font=('Proxima Nova Rg', '12'))
    L_en.grid(row=2,column=0)

        #input from value:
    T2_1 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T2_1.grid(row=2, column=1)
    T2_1.insert(END, "0.0")

    tk.Label(screen_2_2, text="to", font=('Proxima Nova Rg', '12'),
            bg='black', fg='white').grid(row=2,column=2)

        #input to value:
    T2_2 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T2_2.grid(row=2, column=3)
    T2_2.insert(END, "1.0")


    # acousticness area: 

    L_ac = tk.Label(screen_2_2, text="Acousticness")
    L_ac.configure(bg='black', fg='gold', font=('Proxima Nova Rg', '12'))
    L_ac.grid(row=3,column=0)

        #input from value:
    T3_1 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T3_1.grid(row=3, column=1)
    T3_1.insert(END, "0.0")

    tk.Label(screen_2_2, text="to", font=('Proxima Nova Rg', '12'), 
            bg='black', fg='white').grid(row=3,column=2)

        #input to value:
    T3_2 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T3_2.grid(row=3, column=3)
    T3_2.insert(END, "1.0")

    # tempo area:
    L_temp=tk.Label(screen_2_2, text="Tempo")
    L_temp.configure(bg='black', fg='gold', font=('Proxima Nova Rg', '12'))
    L_temp.grid(row=4,column=0)

        #input from value:
    T4_1 = tk.Entry(screen_2_2, text = "64.0", wid=6, font=('Proxima Nova Rg', '12')) 
    T4_1.grid(row=4, column=1)
    T4_1.insert(END, "64.0")

    tk.Label(screen_2_2, text="to", font=('Proxima Nova Rg', '12'),
            bg='black', fg='white').grid(row=4,column=2)

        #input to value:
    T4_2 = tk.Entry(screen_2_2, wid=6, font=('Proxima Nova Rg', '12')) 
    T4_2.grid(row=4, column=3)
    T4_2.insert(END, "198.0")

    #function for chosing song by passing in values (getName from readfromexel)
    def pickSong2():
                    
        messagebox.showinfo("Now playing", 
                            exc.getName(random.choice(exc.resultList(T1_1.get(),T1_2.get(),
                            T2_1.get(), T2_2.get(), T3_1.get(), T3_2.get(), 
                            T4_1.get(), T4_2.get()))))

    Bs3 = tk.Button(screen_2_2, text = "Generate please", command = pickSong2)
    Bs3.configure(font=('BrowalliaUPC', '12'))
    Bs3.grid(row=5,column=0)

    # screen 2_2 for customs:
    screen_2_2.configure(bg='black')

#Button for Mood:
B1= tk.Button(screen, text = "Mood", wid= 9, height = 1, font=('Proxima Nova Rg', '13'), command = screen2_1)
B1.pack()

#Button for Custom:
B2= tk.Button(screen, text = "Custom", wid= 9, height = 1, font=('Proxima Nova Rg', '13'), command = screen2_2)
B2.pack()

#Main Screen Decoration
L_d = tk.Label(screen, text = "_____________", font=('BrowalliaUPC', '20'),
    fg = 'gold', bg ='black')
L_d.pack()

screen.geometry("350x350")
screen.configure(background='black')
screen.mainloop()