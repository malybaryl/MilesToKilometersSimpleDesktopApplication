import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# window 
window = ttk.Window(themename='journal')
window.title("Miles To Kilometers")
window.geometry('400x200')

# variables (moved below the window creation)
convert_miles = tk.BooleanVar(value=True)

# functions
def convert():
    mile_input = entry_int.get()
    if convert_miles.get():
        kilometers_output = mile_input * 1.61
        formatted_output = "{:.2f}".format(kilometers_output) + ' km'
    else:
        kilometers_output = mile_input / 1.61
        formatted_output = "{:.2f}".format(kilometers_output) + ' miles'
    output_string.set(formatted_output)

def change():
    convert_miles.set(not convert_miles.get())
    update_title()

def update_title():
    title_string.set('Miles To Kilometers' if convert_miles.get() else 'Kilometers To Miles')

# title
title_string = tk.StringVar()
update_title()  # Setting a starting title
title_label = ttk.Label(master=window,
                        textvariable=title_string,
                        font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame,
                    text='Convert',
                    command=convert)
button_reverse = ttk.Button(master=input_frame, 
                            text='', 
                            command=change)
entry.pack(side='left', 
           padx=10)
button.pack(side='left', 
            padx=10)
button_reverse.pack(side='left')
input_frame.pack(pady=10)

# loading image
image_path = "img/0.png"
img = Image.open(image_path)
img = img.resize((20, 20))
img = ImageTk.PhotoImage(img)
button_reverse.config(image=img, 
                      compound=tk.LEFT)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font='Calibri 24',
    textvariable=output_string)
output_label.pack()

# run
window.mainloop()
