import tkinter as tk
import random as r
import string
from tkinter import messagebox

def generate_password():
    length = int(length_slider.get())
    result = []
    if numbers_enabled.get():
        result += string.digits
    if lowercase_enabled.get():
        result += string.ascii_lowercase
    if uppercase_enabled.get():
        result += string.ascii_uppercase
    if symbols_enabled.get():
        result += string.punctuation

    for i in range(length - len(result)):
        result.append(r.choice(result))
    r.shuffle(result)
    password = ''.join(result)[:length]
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")

root = tk.Tk()
root.iconbitmap('./lock.ico')
root.title("Password Generator")
root.resizable(False, False)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_slider = tk.Scale(root, from_=1, to=100, orient="horizontal", length=200, sliderrelief=tk.FLAT)
length_slider.set(10)
length_slider.grid(row=0, column=1)

label = tk.Label(root, text="Generated Password:")
label.grid(row=1, column=0)

numbers_enabled = tk.BooleanVar(value=True)
symbols_enabled = tk.BooleanVar(value=True)
lowercase_enabled = tk.BooleanVar(value=True)
uppercase_enabled = tk.BooleanVar(value=True)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.grid(row=2, column=1, pady=10)

numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_enabled, onvalue=True, offvalue=False)
numbers_checkbox.grid(row=3, column=0)

symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_enabled, onvalue=True, offvalue=False)
symbols_checkbox.grid(row=3, column=1)

def on_lowercase_enabled():
    if not lowercase_enabled.get():
        uppercase_enabled.set(True)

def on_uppercase_enabled():
    if not uppercase_enabled.get():
        lowercase_enabled.set(True)

lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_enabled, onvalue=True, offvalue=False, command=on_lowercase_enabled)
lowercase_checkbox.grid(row=4, column=0)

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_enabled, onvalue=True, offvalue=False, command=on_uppercase_enabled)
uppercase_checkbox.grid(row=4, column=1)

def decrease_length(event):
 length_slider.set(length_slider.get() - 1)

def increase_length(event):
 length_slider.set(length_slider.get() + 1)

root.bind("<Left>", decrease_length)
root.bind("<Right>", increase_length)
root.bind("<KP_Left>", decrease_length)
root.bind("<KP_Right>", increase_length)

root.mainloop()
