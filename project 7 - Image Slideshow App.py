from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slideshow Viewer")

image_paths = [
    r"C:\Users\l-3\Downloads\assets_task_01k6a657z3fq2rthd3yrsbefxx_1759131223_img_1.webp",
    r"C:\Users\l-3\Downloads\assets_task_01k609e1ndeyj979kmt1dssy0g_1758799052_img_1.webp",
    r"C:\Users\l-3\Downloads\assets_task_01k63bbfjme388ce5k3v10svr1_1758901761_img_0.webp",
    r"C:\Users\l-3\Downloads\assets_task_01k6a65ekwfa9re6zh9etn11pn_1759131237_img_0.webp",
    r"C:\Users\l-3\Downloads\assets_task_01k6993e7wf08b7ne6ar6erx95_1759100743_img_1.webp"
]

image_size =(1000,1000)
images =[Image.open(path). resize(image_size) for path in image_paths]
photo_images =[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    photoimage = next(slideshow) 
    label.config(image=photoimage)
    label.image = photoimage
    root.after(3000, update_image)

def start_slideshow():
    update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)   
play_button.pack()   

root.mainloop()