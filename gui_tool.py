import tkinter as tk
from tkinter import messagebox
from caesar_cipher import caesar_cipher

def process_text():
    mode = mode_var.get()
    shift = int(shift_var.get())
    text = text_input.get("1.0", tk.END).strip()

    result = caesar_cipher(text, shift, mode)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("500x400")

tk.Label(root, text="Enter your text:").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

mode_var = tk.StringVar(value="encode")
tk.Radiobutton(root, text="Encode", variable=mode_var, value="encode").pack()
tk.Radiobutton(root, text="Decode", variable=mode_var, value="decode").pack()

tk.Label(root, text="Shift value (0-25):").pack()
shift_var = tk.StringVar(value="3")
tk.Entry(root, textvariable=shift_var).pack()

tk.Button(root, text="Process", command=process_text).pack(pady=10)

output_box = tk.Text(root, height=5, width=50)
output_box.pack()

root.mainloop()
