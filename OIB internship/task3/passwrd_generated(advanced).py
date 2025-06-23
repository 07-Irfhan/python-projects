import tkinter as tk
from tkinter import messagebox
import random

letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
numbers=list('0123456789')
symbols=list('!@#$%^&*()')

def generate_password():
    try:
        l=int(entry_letters.get())
        n=int(entry_numbers.get())
        s=int(entry_symbols.get())
    except ValueError:
        messagebox.showerror("Input Error")
        return
    
    if l<0 or n<0 or s<0:
        messagebox.showerror("Negative values are not allowed")
        return
    password_list=[]
    for _ in range(l):
       password_list.append(random.choice(letters))
    for _ in range(n):
       password_list.append(random.choice(numbers))
    for _ in range(s):
       password_list.append(random.choice(symbols))
     
    random.shuffle(password_list)
    passwords=''.join(password_list)
    result_var.set(passwords)

root=tk.Tk()
root.title("Random Password Generator")

tk.Label(root, text="Number of Letters:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_letters = tk.Entry(root)
entry_letters.grid(row=0, column=1)

tk.Label(root, text="Number of Numbers:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_numbers = tk.Entry(root)
entry_numbers.grid(row=1, column=1)

tk.Label(root, text="Number of Symbols:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_symbols = tk.Entry(root)
entry_symbols.grid(row=2, column=1)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=3, columnspan=2, pady=10)

result_var=tk.StringVar()
result_label=tk.Entry(root,textvariable=result_var,font=("courier",12),width=30,justify='center')
result_label.grid(row=4,columnspan=2,pady=5)

root.mainloop()





