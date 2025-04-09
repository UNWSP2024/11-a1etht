#Programmer: Alethea Lo
#Date: 4/8/2025
#Title: GUI Window
import tkinter as tk

root = tk.Tk()
root.title("Favorite Saying")
root.geometry("400x200")

favorite_saying = ("In the same way, let your light shine before others, "
                   "that they may see your good deeds and glorify "
                   "your Father in heaven. ~ Matthew 5:16")
label = tk.Label(
    root,
    text=favorite_saying,
    wraplength=380,
    font=("Helvetica", 12),
    bg="#f0f0f0",
    fg="#333"
)
label.pack(pady=40, padx=10)

root.mainloop()
