import tkinter as tk
from datetime import datetime
from tkinter import font as tkFont  

def start_timer():
    global start_time
    start_time = datetime.now()
    label.config(text="Timer started. Use your phone.", bg='lightgreen')
    start_button.config(state=tk.DISABLED, bg='black')
    stop_button.config(state=tk.NORMAL, bg='red')

def stop_timer():
    if 'start_time' in globals():
        end_time = datetime.now()
        duration = end_time - start_time
        duration_seconds = int(duration.total_seconds())
        hours, remainder = divmod(duration_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{hours}h {minutes}m {seconds}s"
        label.config(text=f"Total usage: {time_string}", bg='lightblue')
        start_button.config(state=tk.NORMAL, bg='green')
        stop_button.config(state=tk.DISABLED, bg='black')

root = tk.Tk()
root.title("Cellphone Usage Timer")

globalFont = tkFont.Font(family="Arial", size=14, weight="bold")

root.option_add("*Font", globalFont)

root.config(bg='purple')

label = tk.Label(root, text="Press 'Start' to begin timing.", bg='lightblue')
label.pack(padx=100, pady=100)

start_button = tk.Button(root, text="Start", command=start_timer, bg='green')
start_button.pack(side=tk.LEFT, padx=30, pady=30)

stop_button = tk.Button(root, text="Stop", command=stop_timer, bg='red')
stop_button.pack(side=tk.RIGHT, padx=30, pady=30)
stop_button.config(state=tk.DISABLED, bg='black') 

root.mainloop()