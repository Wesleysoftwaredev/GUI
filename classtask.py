import tkinter as tk
class WorkoutBuddy:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Buddy")
        self.root.geometry("300x180")
        self.running = False
        self.seconds = 0
        self.mode = "Work"
        self.mode_label = tk.Label(root, text=f"Current Mode: {self.mode}", font=("Arial", 12))
        self.mode_label.pack(pady=10)
        self.time_label = tk.Label(root, text="Time: 00:00", font=("Arial", 12))
        self.time_label.pack(pady=10)
        self.start_button = tk.Button(root, text="Start Workout", command=self.start_workout)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_workout)
        self.stop_button.pack(pady=5)
    def start_workout(self):
        if not self.running:
            self.running = True
            self.update_timer()
    def stop_workout(self):
        self.running = False
    def update_timer(self):
        if self.running:
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.time_label.config(text=f"Time: {minutes:02}:{seconds:02}")
            self.seconds += 1
            self.root.after(1000, self.update_timer)
root = tk.Tk()
app = WorkoutBuddy(root)
root.mainloop()