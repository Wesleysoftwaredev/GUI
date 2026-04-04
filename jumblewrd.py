import tkinter as tk
from tkinter import messagebox
import random

words = ['school', 'python', 'basketball', 'zoo', 'excitement', 'petrified', 'patriarchal', 'society', 'burn', 'football']

current_word = ""
jumbled_word = ""
score = 0

def jumble_words(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

def new_word():
    global current_word, jumbled_word

    current_word = random.choice(words)
    jumbled_word = jumble_words(current_word)

    while jumbled_word == current_word:
        jumbled_word = jumble_words(current_word)

    word_label.config(text=jumbled_word)
    entry.delete(0, tk.END)

def check_answer():
    global score

    user_answer = entry.get().strip().lower()

    if user_answer == current_word:
        score += 1
        score_label.config(text="Score: " + str(score))
        messagebox.showinfo("Result", "Correct Answer")
        new_word()
    else:
        score -= 1
        score_label.config(text="Score: " + str(score))
        messagebox.showerror("Result", f"Wrong Answer\nCorrect word was: {current_word}")
        new_word()

root = tk.Tk()
root.title("Jumble Word Game")
root.geometry("400x300")
root.config(bg="lightyellow")

title_label = tk.Label(root, text="Jumble Word Game", font=("Arial", 20, "bold"), bg="lightyellow")
title_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 24, "bold"), bg="lightyellow", fg="blue")
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Arial", 14), command=check_answer)
check_button.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14, "bold"), bg="lightyellow", fg="green")
score_label.pack(pady=10)

new_word()

root.mainloop()