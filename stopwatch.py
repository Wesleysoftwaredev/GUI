import tkinter as tk

#variables
running = False
counter = 0

def update_time():
    global counter
    if running:
        counter +=1
        minutes = counter // 6000
        seconds = counter (counter // 100) % 60
        milliseconds = counter % 100
        time_label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")
        root.after(10, update_time)

def start_time():
    global running
    if not running:
        running = True
        update_time()

def stop_time():
    global running
    running = False

def reset_time():
    global counter, running
    running = False
    counter = 0
    time_label.config(text = "00:00:00")

root = tk.Tk()
root.title("Stopwatch")
root.geometry('500x400')
time_label=tk.Label(root, text = "00:00:00", font = ('Ariel', 50), fg = 'black')
time_label.pack(pady = 20)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Start", width=8, command=start_time).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Stop", width=8, command=stop_time).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Reset", width=8, command=reset_time).grid(row=0, column=2, padx=5)

root.mainloop()