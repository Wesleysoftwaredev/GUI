import tkinter as tk
root = tk.Tk()

root.title('simple menubar')
root.geometry('400x300')

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff = 0)
file_menu.add_command(label = 'new file')
file_menu.add_separator()
file_menu.add_command(label = 'exit',command = root.destroy)

menubar.add_cascade(label = 'file',menu = file_menu)

root.config(menu = menubar)
root.mainloop()
 