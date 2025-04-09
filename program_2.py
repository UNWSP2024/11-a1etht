#Programmer: Alethea Lo
#Date: 4/8/2025
#Title: GUI Program With Personal Info
import tkinter as tk

def show_info():
    info_label.config(text="Alethea Lo\n6693 Court South\nParis, FA 94110")

root = tk.Tk()
root.title("Info Display")
root.geometry("300x200")

info_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
info_label.pack(pady=20)

#Show Button
show_button = tk.Button(root, text="Show Info", command=show_info, font=("Arial", 10), width=15)
show_button.pack(pady=5)

#Quit Button
quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 10), width=15)
quit_button.pack(pady=5)

root.mainloop()