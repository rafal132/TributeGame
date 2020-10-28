from tkinter import *
from PIL import ImageTk, Image, ImageSequence
import random
import pygame
import ctypes


root = Tk()

user32 = ctypes.windll.user32
screenwith = user32.GetSystemMetrics(0)
screenheight = user32.GetSystemMetrics(1)


p = "papier"
k = "kamień"
n = "nożyce"
comp_score = 0
player_score = 0



root.title("TRIBUTE")
root.resizable(0, 0)
root_width = 504
root_height = 504
middle_x = screenwith/2-root_width/2
middle_y = screenheight/2 - root_height/2

root.geometry('%dx%d+%d+%d' % (root_height, root_width, middle_x, middle_y))


#
# EKRAN STARTOWY GRY:
#
canvas = Canvas(root, bd=-2, bg='black')
canvas.pack(expand=True, fill=BOTH)
canvas.pack_propagate(0)

pygame.mixer.init()
pygame.mixer.music.load('Tenacious D - Tribute.wav')
pygame.mixer.music.play(-1)

quote1 = 'This is the greatest and best \n \'Rock, paper and scissors\' \n game in the world...'
text1 = Label(canvas, pady=120, text=quote1, fg='white', bg='black', bd=0, height=3, font=('arial', 28))
text1.pack()


def start_game():
    canvas.destroy()
    boom = pygame.mixer.Sound('Barrel Exploding.wav')
    boom.play()
    game()

def callback1():
    quote2 = '...tribute.'
    button = Button(canvas, relief=RAISED, width=7, height=1, bd=0, activebackground='black', activeforeground='black',
                    text=quote2, fg='white', bg='black', font=('arial', 28), command=start_game)
    button.pack()


root.after(5000, callback1)


def game():
    def you_lost():
        root.wm_attributes('-disabled', True)
        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')
        win = Toplevel()
        win.wm_attributes('-topmost', True)
        win.overrideredirect(1)
        win.geometry('%dx%d+%d+%d' % (root_height, root_width, middle_x+9, middle_y+29))
        win.wm_title("YOU LOST!")
        win.resizable(0, 0)
        topcanvas = Canvas(win, bd=20, bg='black', relief=RAISED)
        topcanvas.pack(expand=True, fill=BOTH)
        topcanvas.pack_propagate(0)
        gif = [ImageTk.PhotoImage(imge)
               for imge in ImageSequence.Iterator(Image.open("Devilwin.gif"))]
        image = topcanvas.create_image(252, 182, image=gif[0])

        def animate(counter):
            topcanvas.itemconfig(image, image=gif[counter])
            win.after(20, lambda: animate((counter + 1) % len(gif)))

        animate(1)

        def yes_click():
            root.wm_attributes('-disabled', False)
            button1.config(state='normal')
            button2.config(state='normal')
            button3.config(state='normal')
            global comp_score
            global player_score
            emptying()
            jbemptylabel.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
            devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))
            khaboom()
            img1.grid(row=2, column=0, columnspan=3, sticky=N)
            img2.grid(row=2, column=3, columnspan=3, sticky=N)
            comp_score = 0
            player_score = 0
            score_display()
            win.destroy()

        label_lost = Label(topcanvas, height=1, text='YOU LOST!', fg='white', bg='black', font=('arial', 28))
        label_again = Label(topcanvas, height=1, text='Want to play again?', fg='white', bg='black', font=('arial', 28))

        button_yes = Button(topcanvas, text="YES", activeforeground='white', activebackground='black',
                            command=yes_click, width=10, height=1, bg='black', fg='white', bd=10, font=('arial', 16))
        button_no = Button(topcanvas, text="NO", activeforeground='white', activebackground='black',
                           command=root.destroy, width=10, height=1, bg='black', fg='white', bd=10, font=('arial', 16))
        label_lost.grid(row=0, column=0, columnspan=2, sticky=(N, E, W), pady=20, padx=22)
        label_again.grid(row=1, column=0, columnspan=2, sticky=(S, E, W), padx=22)
        button_yes.grid(row=2, column=0)
        button_no.grid(row=2, column=1)
        topcanvas.grid_columnconfigure(0, minsize=252)
        topcanvas.grid_columnconfigure(1, minsize=252)
        topcanvas.grid_rowconfigure(0, minsize=1)
        topcanvas.grid_rowconfigure(1, minsize=250)
        topcanvas.grid_rowconfigure(2, minsize=130)

    def you_won():
        root.wm_attributes('-disabled', True)
        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')
        win = Toplevel()
        win.wm_attributes('-topmost', True)
        win.overrideredirect(1)
        win.geometry('%dx%d+%d+%d' % (root_height, root_width, middle_x+9, middle_y+29))
        win.wm_title("YOU WON!")
        win.resizable(0, 0)
        topcanvas = Canvas(win, bd=20, bg='black', relief=RAISED)
        topcanvas.pack(expand=True, fill=BOTH)
        topcanvas.pack_propagate(0)
        gif = [ImageTk.PhotoImage(imge)
               for imge in ImageSequence.Iterator(Image.open("tributewin2.gif"))]
        image = topcanvas.create_image(252, 182, image=gif[0])

        def animate(counter):
            topcanvas.itemconfig(image, image=gif[counter])
            win.after(20, lambda: animate((counter + 1) % len(gif)))

        animate(1)

        def yes_click():
            root.wm_attributes('-disabled', False)
            button1.config(state='normal')
            button2.config(state='normal')
            button3.config(state='normal')
            global comp_score
            global player_score
            emptying()
            jbemptylabel.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
            devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))
            khaboom()
            img1.grid(row=2, column=0, columnspan=3, sticky=N)
            img2.grid(row=2, column=3, columnspan=3, sticky=N)
            comp_score = 0
            player_score = 0
            score_display()
            win.destroy()

        label_lost = Label(topcanvas, height=1, text='YOU WON!', fg='white', bg='black', font=('arial', 28))
        label_again = Label(topcanvas, height=1, text='Want to play again?', fg='white', bg='black', font=('arial', 28))

        button_yes = Button(topcanvas, text="YES", activeforeground='white', activebackground='black',
                            command=yes_click, width=10, height=1, bg='black', fg='white', bd=10, font=('arial', 16))
        button_no = Button(topcanvas, text="NO", activeforeground='white', activebackground='black',
                           command=root.destroy, width=10, height=1, bg='black', fg='white', bd=10, font=('arial', 16))
        label_lost.grid(row=0, column=0, columnspan=2, sticky=(N, E, W), pady=20, padx=22)
        label_again.grid(row=1, column=0, columnspan=2, sticky=(S, E, W), padx=22)
        button_yes.grid(row=2, column=0)
        button_no.grid(row=2, column=1)
        topcanvas.grid_columnconfigure(0, minsize=252)
        topcanvas.grid_columnconfigure(1, minsize=252)
        topcanvas.grid_rowconfigure(0, minsize=1)
        topcanvas.grid_rowconfigure(1, minsize=250)
        topcanvas.grid_rowconfigure(2, minsize=130)


    canvas = Canvas(root, bd=20, bg='black', relief=RAISED)
    canvas.pack(expand=True, fill=BOTH)
    canvas.pack_propagate(0)
    img = Image.open('road3.jpg')
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(250, 220, image=canvas.image, )

    def set_volume(vol):
        volume = int(vol)/100
        pygame.mixer.music.set_volume(volume)

    option_canvas = Label(canvas, height=5, bd=5, fg='black', relief=RAISED,  bg='black', highlightbackground='black', highlightcolor='black')
    option_canvas.grid(row=4, column=0, columnspan=6, ipadx=139, pady=27, sticky=N)

    volume_slider = Scale(option_canvas, activebackground='black', bg='black', fg='black', length=80, highlightcolor='black', width=10, sliderlength=10, troughcolor='black', bd=0, showvalue=False, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
    volume_slider.pack(side=LEFT)
    volume_slider.set(100)

    def emptying():
        img1.grid_forget()
        img2.grid_forget()
        img3.grid_forget()
        img4.grid_forget()
        img5.grid_forget()
        img6.grid_forget()
        img7.grid_forget()
        img8.grid_forget()
        jbemptylabel.grid_forget()
        devilemptylabel.grid_forget()
        jblabelpaper.grid_forget()
        devillabelpaper.grid_forget()
        jblabelrock.grid_forget()
        jblabelscissors.grid_forget()
        devillabelrock.grid_forget()
        devillabelscissors.grid_forget()


    jbemptylabel = Label(canvas,fg='white',text=' ', font=('arial', 8), height=1, bd=10, bg='black', relief=RAISED)
    jbemptylabel.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
    devilemptylabel = Label(canvas, text=' ', fg='white',font=('arial', 8), height=1, bd=10, bg='black', relief=RAISED)
    devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))

    jblabelpaper = Label(canvas,font=('arial', 8), text="JB picked: PAPER!!!" ,fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #jblabelpaper.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
    devillabelpaper = Label(canvas, font=('arial', 8), text='Devil picked: PAPER!!!',fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #devillabelpaper.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
    jblabelrock = Label(canvas, font=('arial', 8), text="JB picked: ROCK!!!" ,fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #jblabelrock.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
    devillabelrock = Label(canvas, font=('arial', 8), text='Devil picked: ROCK!!!',fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #devillabelrock.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
    jblabelscissors = Label(canvas, font=('arial', 8), text="JB picked: SCISSORS!!!" ,fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #jblabelscissors.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
    devillabelscissors = Label(canvas, font=('arial', 8), text='Devil picked: SCISSORS!!!',fg='white', height=1, bd=10, bg='black', relief=RAISED)
    #devillabelscissors.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))

    CheckVar1 = IntVar()

    def music_stop():
        var = CheckVar1.get()
        if var == 1:
            boom = pygame.mixer.Sound('Barrel Exploding.wav')
            boom.set_volume(0)
            pygame.mixer.music.set_volume(0)
        elif var == 0:
            boom = pygame.mixer.Sound('Barrel Exploding.wav')
            volume_slider.get()
            volume = int(volume_slider.get()) / 100
            boom.set_volume(volume)
            pygame.mixer.music.set_volume(volume)

    def khaboom():
        var = CheckVar1.get()
        if var == 0:
            boom = pygame.mixer.Sound('Barrel Exploding.wav')
            volume_slider.get()
            volume = int(volume_slider.get()) / 100
            boom.set_volume(volume)
            boom.play()

    load1 = Image.open("Pick-of-Destiny.png.jpg")
    render1 = ImageTk.PhotoImage(load1)
    img1 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render1)
    img1.image = render1

    load2 = Image.open("Pick-of-Destiny.png.jpg")
    render2 = ImageTk.PhotoImage(load2)
    img2 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render2)
    img2.image = render2

    img1.grid(row=2, column=0, columnspan=3, sticky=N)
    img2.grid(row=2, column=3, columnspan=3, sticky=N)

    load3 = Image.open("JBscissors.jpg")
    render3 = ImageTk.PhotoImage(load3)
    img3 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render3)
    img3.image = render3

    load4 = Image.open("Devilpapernew.bmp")
    render4 = ImageTk.PhotoImage(load4)
    img4 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render4)
    img4.image = render4

    load5 = Image.open("Devilscissors.bmp")
    render5 = ImageTk.PhotoImage(load5)
    img5 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render5)
    img5.image = render5

    load6 = Image.open("Devilrock.bmp")
    render6 = ImageTk.PhotoImage(load6)
    img6 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render6)
    img6.image = render6

    load7 = Image.open("JBrock.bmp")
    render7 = ImageTk.PhotoImage(load7)
    img7 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render7)
    img7.image = render7

    load8 = Image.open("JBpaper.jpg")
    render8 = ImageTk.PhotoImage(load8)
    img8 = Label(canvas, bd=15, bg='black', relief=RAISED, image=render8)
    img8.image = render8

    canvas.grid_columnconfigure(0, minsize=84)
    canvas.grid_columnconfigure(1, minsize=84)
    canvas.grid_columnconfigure(2, minsize=84)
    canvas.grid_columnconfigure(3, minsize=84)
    canvas.grid_columnconfigure(4, minsize=84)
    canvas.grid_columnconfigure(5, minsize=84)
    canvas.grid_rowconfigure(0, minsize=84)
    canvas.grid_rowconfigure(2, minsize=250)
    canvas.grid_rowconfigure(5, pad=0)

    def score_display():
        comp_score_display = Label(canvas, text=comp_score, bd=10, relief=RAISED, width=1, height=1, fg='red', bg='black', font=('David Libre', 30))
        player_score_display = Label(canvas, text=player_score, bd=10, relief=RAISED, width=1, height=1, fg='blue', bg='black', font=('David Libre', 30))
        comp_score_display.grid(row=0, column=0, columnspan=3, sticky=S)
        player_score_display.grid(row=0, column=3, columnspan=3, sticky=S)

    def paper():
        emptying()
        jblabelpaper.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
        devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))
        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')
        global comp_score
        global player_score
        if comp_score < 3 and player_score < 3:
            img8.grid(row=2, column=3, columnspan=3, sticky=N)
            img1.grid(row=2, column=0, columnspan=3, sticky=N)
            khaboom()

        def callback():
            devilemptylabel.grid_forget()
            global comp_score
            global player_score
            if comp_score < 3 and player_score < 3:
                khaboom()
                global p, k, n
                computer_list = [p, k, n]
                computer = random.choice(computer_list)
                if computer == k:
                    devillabelrock.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                    img6.grid(row=2, column=0, columnspan=3, sticky=N)
                    player_score += 1
                elif computer == n:
                    img5.grid(row=2, column=0, columnspan=3, sticky=N)
                    comp_score += 1
                    devillabelscissors.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                elif computer == p:
                    img4.grid(row=2, column=0, columnspan=3, sticky=N)
                    devillabelpaper.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                score_display()
                button1.config(state='normal')
                button2.config(state='normal')
                button3.config(state='normal')
            if comp_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_lost)
            elif player_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_won)

        root.after(1000, callback)

    def rock():
        emptying()
        jblabelrock.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
        devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))
        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')

        if comp_score < 3 and player_score < 3:
            img7.grid(row=2, column=3, columnspan=3, sticky=N)
            img1.grid(row=2, column=0, columnspan=3, sticky=N)
            khaboom()

        def callback():
            devilemptylabel.grid_forget()
            global comp_score
            global player_score
            global p, k, n
            if comp_score < 3 and player_score < 3:
                khaboom()
                img3.grid(row=2, column=3, columnspan=3, sticky=N)
                computer_list = [p, k, n]
                computer = random.choice(computer_list)
                if computer == n:
                    devillabelscissors.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                    img5.grid(row=2, column=0, columnspan=3, sticky=N)
                    player_score += 1
                elif computer == p:
                    comp_score += 1
                    img4.grid(row=2, column=0, columnspan=3, sticky=N)
                    devillabelpaper.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                elif computer == k:
                    devillabelrock.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                    img6.grid(row=2, column=0, columnspan=3, sticky=N)
                score_display()
                button1.config(state='normal')
                button2.config(state='normal')
                button3.config(state='normal')
            if comp_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_lost)
            elif player_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_won)
        root.after(1000, callback)


    def scissors():
        emptying()
        devilemptylabel.grid(row=1, column=0, columnspan=3, padx=36, sticky=(E, W))
        jblabelscissors.grid(row=1, column=3, columnspan=3, padx=36, sticky=(E, W))
        button1.config(state='disabled')
        button2.config(state='disabled')
        button3.config(state='disabled')

        if comp_score < 3 and player_score < 3:
            img1.grid(row=2, column=0, columnspan=3, sticky=N)
            img3.grid(row=2, column=3, columnspan=3, sticky=N)
            khaboom()

        def callback():
            devilemptylabel.grid_forget()
            global comp_score
            global player_score
            if comp_score < 3 and player_score < 3:
                khaboom()
                global p, k, n
                computer_list = [p, k, n]
                computer = random.choice(computer_list)
                if computer == p:
                    devillabelpaper.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                    player_score += 1
                    img4.grid(row=2, column=0, columnspan=3, sticky=N)
                elif computer == k:
                    devillabelrock.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                    comp_score += 1
                    img6.grid(row=2, column=0, columnspan=3, sticky=N)
                elif computer == n:
                    img5.grid(row=2, column=0, columnspan=3, sticky=N)
                    devillabelscissors.grid(row=1, column=0, columnspan=3,padx=36, sticky=(E, W))
                score_display()
                button1.config(state='normal')
                button2.config(state='normal')
                button3.config(state='normal')
            if comp_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_lost)
            elif player_score == 3:
                button1.config(state=DISABLED)
                button2.config(state=DISABLED)
                button3.config(state=DISABLED)
                root.after(350, you_won)
        root.after(1000, callback)

    button1 = Button(canvas, text="PAPER", activeforeground='white', activebackground='black', command=paper, width=10, height=1, bg='black', fg='white', bd=10,font=('arial', 16))
    button2 = Button(canvas, text="ROCK", activeforeground='white', activebackground='black', command=rock, width=10, height=1, bg='black', fg='white', bd=10,font=('arial', 16))
    button3 = Button(canvas, text="SCISSORS", activeforeground='white', activebackground='black', command=scissors, width=10, height=1, bg='black', fg='white', bd=10, font=('arial', 16))

    score_display()

    button1.grid(row=3, column=0, columnspan=2, sticky=E)
    button2.grid(row=3, column=2, columnspan=2)
    button3.grid(row=3, column=4, columnspan=2, sticky=W)

    stop_music = Checkbutton(option_canvas, padx=5, pady=0, font=('arial', 7), text='Sound on/off', fg='white', selectcolor="black", disabledforeground='black', activebackground='black', activeforeground='white', bg='black',  bd=0, variable=CheckVar1, command=music_stop)
    stop_music.pack(side=LEFT)

root.mainloop()



