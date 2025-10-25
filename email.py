import tkinter as tk

#login function
def login():
    email = email_entry.get()
    password = pwd_entry.get()

    if '@' in email and len(password)>=8:
        message_var.set('login succesful')
    
    else:
        message_var.set('invalid password')


root = tk.Tk()
root.title("Login form")


tk.Label(root,text = "Email").grid(row = 0, column = 0,padx = 10, pady = 10, sticky = "e")
tk.Label(root,text = "Password").grid(row = 1, column = 0,padx = 10, pady = 10, sticky = "e")
email_entry = tk.Entry(root, width = 30)
pwd_entry = tk.Entry(root, width = 30, show = "*")
email_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
pwd_entry.grid(row = 1, column = 1, padx = 10, pady = 10)

message_var = tk.StringVar() #built in variable class
tk.Label(root, textvariable = message_var, fg="blue").grid(row=3, column=0,columnspan = 2,pady=10)

tk.Button(root, text="Login",command=login).grid(row=2,column=0,columnspan=2,pady=10)

root.mainloop()