import tkinter as tk
import calendar

root = tk.Tk()
root.title('calendar App')
root.geometry('500x400')
root.config(bg = 'lightblue')

year_label = tk.Label(root,text = 'year:')
year_label.grid(row=0,column=0,padx=5,pady=5)

year_entry = tk.Entry(root)
year_entry.grid(row=0,column=1,padx=5,pady=5)

month_label = tk.Label(root,text = 'month:')
month_label.grid(row=1,column=0,padx=5,pady=5)

month_entry = tk.Entry(root)
month_entry.grid(row=1,column=1,padx=5,pady=5)

cal_display = tk.Label(root,font = ('courier new',14),justify='left')
cal_display.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())


        if month <1 or month>12:
            cal_display.config(text='invalid month choose b/w 1-12')
            return
    
        cal_text = calendar.month(year,month)
        cal_display.config(text=cal_text)

    except ValueError:
        cal_display.config(text = 'please enter numeric values only')

show_button = tk.Button(root,text='show calendar',fg='white',bg='black',command= show_calendar)
show_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

root.mainloop()