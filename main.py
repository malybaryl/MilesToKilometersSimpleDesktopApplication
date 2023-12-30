import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    kilometers_output = mile_input * 1.61
    formatted_output = "{:.2f}".format(kilometers_output)+' km'
    output_string.set(formatted_output)

#window 
window = ttk.Window(themename = 'journal')
window.title("Miles To Kilometers")
window.geometry('400x200')

#title
title_lable = ttk.Label(master = window, text='Miles to kilometers', font='Calibri 24 bold')
title_lable.pack()

# input field
input_frame = ttk.Frame(master = window, )
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable = entry_int)
button = ttk.Button(master=input_frame, text= 'convert', command = convert)
entry.pack(side='left', padx= 10)
button.pack(side='left') # side = "left" (to entry and button be next to each other) #padx - padding x (px)
input_frame.pack(pady = 10) #pady - padding y (px) 

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text='Output',
    font='Calibri 24',
    textvariable = output_string)
output_label.pack()

# run
window.mainloop()