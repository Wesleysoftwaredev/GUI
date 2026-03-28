import tkinter as tk
import random

words = ["python", "football", "shuffle", "keyboard", "practice"]
word = random.choice(words)
jumbled = "".join(random.sample(word, len(word)))

def check():
    if entry.get().lower() == word:
       result.config(text="Correct!", fg="green")
    else:
       result.config(text="Try Again!", fg="red")

root = tk.Tk()