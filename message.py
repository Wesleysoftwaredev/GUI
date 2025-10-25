import tkinter as tk #the library

root = tk.Tk() #main canvas
root.title("button fantasy") #title of the project

root.geometry("400x400") #size of the canvas
button = tk.Button(root, text = "Click Me!", fg = 'purple', bg = 'yellow',font=('Arial',20,'italic bold'))

button.place(relx = 0.5,rely = 0.5,anchor = 'center')

root.mainloop()