
import tkinter as tk

root = tk.Tk()

root.title("Maze")

root.geometry("500x500")
root.resizable(False, False)

Start = tk.Button(text = "start", width=12, height=2)
Start.place(x=250,y=125, anchor="center")

Continue = tk.Button(text="continue", width=12, height=2)
Continue.place(x=250, y=187.5, anchor="center")

Guide = tk.Button(text = "guide", width=12, height=2)
Guide.place(x=250, y=250, anchor="center")

Shop = tk.Button(text="shop", width=12, height=2)
Shop.place(x=250, y=312.5, anchor="center")

Information = tk.Button(text="information", width=12, height=2)
Information.place(x=250, y=375, anchor="center")

root.mainloop()

