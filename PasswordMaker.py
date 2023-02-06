import tkinter as tk
from tkinter import messagebox
import random as r
import string

passwords = []

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
    passwords.append(password)
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
root.geometry("340x190")

length_label = tk.Label(root, text="Password Length:")
length_label.place(x=12, y=27)

length_slider = tk.Scale(root, from_=1, to=100, orient="horizontal", length=200, sliderrelief=tk.FLAT)
length_slider.set(10)
length_slider.place(x=122, y=10)

label = tk.Label(root, text="Generated Password:")
label.place(x=12, y=60)

numbers_enabled = tk.BooleanVar(value=True)
symbols_enabled = tk.BooleanVar(value=True)
lowercase_enabled = tk.BooleanVar(value=True)
uppercase_enabled = tk.BooleanVar(value=True)

password_entry = tk.Entry(root, width=30)
password_entry.place(x=132, y=60)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.place(x=45, y=90)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.place(x=185, y=90)

numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_enabled, onvalue=True, offvalue=False)
numbers_checkbox.place(x=35, y=125)

symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=symbols_enabled, onvalue=True, offvalue=False)
symbols_checkbox.place(x=175, y=125)

def on_lowercase_enabled():
    if not lowercase_enabled.get():
        uppercase_enabled.set(True)

def on_uppercase_enabled():
    if not uppercase_enabled.get():
        lowercase_enabled.set(True)

lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_enabled, onvalue=True, offvalue=False, command=on_lowercase_enabled)
lowercase_checkbox.place(x=35, y=150)

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_enabled, onvalue=True, offvalue=False, command=on_uppercase_enabled)
uppercase_checkbox.place(x=175, y=150)

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Password History")
    history_window.geometry("300x300")

    history_listbox = tk.Listbox(history_window)
    history_listbox.pack()

    for password in passwords:
        history_listbox.insert(tk.END, password)
    close_button = tk.Button(history_window, text="Close", command=history_window.destroy)
    close_button.pack()
history_button = tk.Button(root, text="History", command=show_history)
history_button.place(x=0, y=0)

def decrease_length(event):
 length_slider.set(length_slider.get() - 1)

def increase_length(event):
 length_slider.set(length_slider.get() + 1)

root.bind("<Left>", decrease_length)
root.bind("<Right>", increase_length)
root.bind("<KP_Left>", decrease_length)
root.bind("<KP_Right>", increase_length)

root.mainloop()
