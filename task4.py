import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def login():
    email = email_entry.get().strip()
    password = password_entry.get()

    if not email or "@" not in email:
        error_label.config(text="Invalid email")
        messagebox.showerror("Error", "Invalid Input")
        return

    if not password:
        error_label.config(text="Password required")
        messagebox.showerror("Error", "Password required")
        return

    error_label.config(text="")
    messagebox.showinfo("Success", "Login Successful")

def clear_fields():
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    error_label.config(text="")

root = tk.Tk()
root.title("Email Login")
root.geometry("300x200") 

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()