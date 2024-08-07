from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import pygame
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("1000x600")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("iron-man-snap.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("Iron-man-snap.mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000, 600))
        img = ImageTk.PhotoImage(img)
        lbl.config(image = img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()