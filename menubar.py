import tkinter as tk
root = tk.Tk()

root.title('simple menubar')
root.geometry('400x300')

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff = 0)

def new_file():
    new_window = tk.Toplevel(root)
    new_window.title('new file')
    new_window.geometry('200x100')
    tk.Label(new_window, text = 'this is the new window').pack(pady=20)

file_menu.add_command(label = 'new file',command=new_file)
file_menu.add_separator()
file_menu.add_command(label = 'exit',command = root.destroy)

menubar.add_cascade(label = 'file',menu = file_menu)
root.config(menu = menubar)
 
button1 = tk.Button(root, text = "Click me", fg = 'pink', bg = 'blue', font=('Arial', 15))
button1.place(relx = 0.5, rely = 0.5, anchor='center')

button2 = tk.Button(root, text = "Dont click me", fg = 'purple', bg = 'red', font=('Arial', 15))
button2.place(relx = 0.5, rely = 0.7, anchor='center')

button3 = tk.Button(root, text = "Never click me", fg = 'yellow', bg = 'green', font=('Arial', 15))
button3.place(relx = 0.5, rely = 0.9, anchor='center')

root.mainloop()
 