import tkinter as tk
from PIL import ImageGrab
import pyperclip

hex_color = "#FFFFFF"

def pick_color(event=None):
    global hex_color
    root.withdraw()
    
    screen = ImageGrab.grab()
    
    root.deiconify()
    
    root.update()
    x, y = root.winfo_pointerx(), root.winfo_pointery()
    rgb_color = screen.getpixel((x, y))
    
    hex_color = '#%02x%02x%02x' % rgb_color
    color_label.config(text=f"Color: {hex_color}", bg="#FFFFFF")
    show_color.config(bg=hex_color)

def copy_color():
    global hex_color
    pyperclip.copy(hex_color)

root = tk.Tk()
root.title("Color Box - By Myzer")
root.geometry("300x400")

instruction_label = tk.Label(root, text="Press Enter to pick a color", font=("Arial", 14))
instruction_label.pack(pady=20)

color_label = tk.Label(root, text="Color: #FFFFFF", bg="#FFFFFF", font=("Arial", 14))
color_label.pack(pady=20)

show_color = tk.Label(root, text="______", bg="#FFFFFF", font=("Arial", 16))
show_color.pack(pady=10)

bouton_copy = tk.Button(root, text="Copy Color", font=("Arial", 14), command=copy_color)
bouton_copy.pack(pady=10)

root.bind('<Return>', pick_color)

root.mainloop()
