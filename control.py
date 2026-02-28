import tkinter as tk

root = tk.Tk()
root.title("Control Panel")
root.geometry('400x300')

top_frame = tk.Frame(root)
top_frame.pack(pady=40)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, pady=40)

start_button = tk.Button(top_frame, text="Start", fg="green", width=10)
start_button.pack(side=tk.LEFT, padx=15)

stop_button = tk.Button(top_frame, text="Stop", fg="red", width=10)
stop_button.pack(side=tk.LEFT, padx=15)

settings_button = tk.Button(bottom_frame, text="Settings", width=10)
settings_button.pack(side=tk.LEFT, padx=15)

exit_button = tk.Button(bottom_frame, text="Exit", fg="red", width=10, command=root.destroy)
exit_button.pack(side=tk.LEFT, padx=15)

root.mainloop()