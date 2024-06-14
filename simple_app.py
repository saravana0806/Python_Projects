# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:04:46 2024

@author: HP
"""

import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Button Click", "Button was clicked!")

root = tk.Tk()
root.title("Simple Tkinter App")

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)

root.mainloop()

