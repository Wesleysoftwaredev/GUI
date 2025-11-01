import tkinter as tk #the library

root = tk.Tk() #main canvas
root.title("button fantasy") #title of the project

root.geometry("400x400") #size of the canvas

root.configure(bg='darkblue')

button = tk.Button(root, text = "Click Me!", fg = 'purple', bg = 'yellow',font=('Arial',20,'italic bold'))

button.place(relx = 0.5,rely = 0.5,anchor = 'center')

button2 = tk.Button(root,text="Do Not Click!",fg='white',bg='pink',font=('verdana',15,'bold'))

button2.place(relx=0.5,rely=0.7,anchor= 'center')

button3 = tk.Button(root,text="Do Not Click This!",fg='black',bg='green',font=('verdana',15,'bold'))

button3.place(relx=0.5,rely=0.9,anchor= 'center')

button4 = tk.Button(root,text="Maybe you can click this",fg='gold',bg='red',font=('verdana',15,'bold'))

button4.place(relx=0.5,rely=0.3,anchor= 'center')

button5 = tk.Button(root,text="Unclickable",fg='blue',bg='violet',font=('verdana',15,'bold'))

button5.place(relx=0.5,rely=0.1,anchor= 'center')

root.mainloop()