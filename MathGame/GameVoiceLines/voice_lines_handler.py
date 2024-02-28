import tkinter as tk
from tkinter import ttk
import json


def load_voice_lines():
    try:
        with open('default_daniel_voice_lines.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"greetings": [], "farewells": []}


def save_voice_lines(voice_lines):
    with open('default_daniel_voice_lines.json', 'w') as file:
        json.dump(voice_lines, file, indent=4)


def add_voice_line():
    category = category_combobox.get()
    new_line = voice_line_entry.get()

    if category and new_line:
        voice_lines = load_voice_lines()
        voice_lines[category].append(new_line)
        save_voice_lines(voice_lines)
        voice_line_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Voice Line Editor")
root.config(bg='lightgrey')

category_label = tk.Label(root, text="Category: ")
category_label.pack(pady=(10, 0))
category_combobox = ttk.Combobox(root, values=list(load_voice_lines().keys()))
category_combobox.pack(pady=30)

category_label.config(bg='blue', fg='black', font=('Arial', 12))
# Styling the category

voice_line_label = tk.Label(root, text="New Voice Line:")
voice_line_label.pack(pady=(10, 0))
voice_line_label.config(bg='black', fg='black', font=('Arial', 12))

voice_line_entry = tk.Entry(root)
voice_line_entry.pack(pady=5)
voice_line_entry.config(fg='black', font=('Arial', 12), bg='white')
# Styling the voice line entry thing


add_line_button = tk.Button(root, text="Add Line", command=add_voice_line)
add_line_button.pack(pady=10)
add_line_button.config(bg='navy', fg='white', font=('Arial', 12), relief=tk.RAISED, bd=5, padx=10, pady=5)

root.mainloop()
