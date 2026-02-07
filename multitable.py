import tkinter as tk
from tkinter import ttk, messagebox


def show_table():
    try:
        n = int(num_var.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter an integer for the number.")
        return

    try:
        start = int(start_var.get())
        end = int(end_var.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter integers for start and end.")
        return

    if start > end:
        messagebox.showerror("Invalid range", "Start must be less than or equal to End.")
        return

    lines = [f"{n} x {i} = {n*i}" for i in range(start, end + 1)]
    output_text = "\n".join(lines)

    # Display output
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, output_text)
    output_box.config(state="disabled")


def clear_output():
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.config(state="disabled")

root = tk.Tk()
root.title("Multiplication Table")

num_var = tk.StringVar()
start_var = tk.StringVar()
end_var = tk.StringVar()

frm = ttk.Frame(root, padding=12)
frm.grid(row=0, column=0, sticky="nsew")

ttk.Label(frm, text="Number:").grid(row=0, column=1, sticky="w")
ttk.Entry(frm, textvariable=num_var, width=10).grid(row=0, column=1, sticky="w", padx=6)

ttk.Label(frm, text="Start:").grid(row=1, column=0, sticky="w")
ttk.Entry(frm, textvariable=start_var, width=10).grid(row=1, column=1, sticky="w", padx=6)

ttk.Label(frm, text="End:").grid(row=2, column=0, sticky="w")
ttk.Entry(frm, textvariable=end_var, width=10).grid(row=2, column=1, sticky="w", padx=6)

btns = ttk.Frame(frm)
btns = ttk.Style('red')
btns.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="w")

ttk.Button(btns, text="Show Table", command=show_table).grid(row=0, column=0, padx=(0, 8))
ttk.Button(btns, text="Clear", command=clear_output).grid(row=0, column=1)

output_box = tk.Text(frm, width=30, height=12, state="disabled")
output_box.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky="nsew")

root.mainloop()