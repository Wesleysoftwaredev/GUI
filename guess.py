import tkinter as tk
import random
from tkinter import messagebox

number = random.randint(1,20)

def check_guess():
    guess = entry.get()

    if not guess.isdigit():
        messagebox.showinfo("Invalid input, please enter a valid number")
        return
    
    guess = int(guess)

    if guess == number:
        messagebox.showinfo("result", 'you have done it')
        root.destroy()
    elif guess<number:
        messagebox.showinfo("results", 'number too low')
    else:
        messagebox.showinfo("results", 'number too high')

root = tk.Tk()
root.title("Guess The Number")
root.geometry('350x200')

label_title = tk.Label(root, text='guess the number b/w 1-20',font=('arial', 14))
label_title.grid(row=0,column=0,columnspan=2,pady=10)

label_guess = tk.Label(root, text="Enter your guess:")
label_guess.grid(row=1, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=1,column=0,padx=10,pady=10)

button_guess=tk.Button(root, text="Guess", command=check_guess)
button_guess.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()

