import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Application")
root.geometry("640x480")
root.minsize(320, 240)

ttk.Label(root, text="Hello").pack(padx=40, pady=40)

root.mainloop()