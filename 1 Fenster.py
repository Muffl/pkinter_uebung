import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Klickzähler")
root.geometry("400x400")
root.focus()
root.columnconfigure(0,weight=1)
#root.rowconfigure(0, weight=1)
#root.rowconfigure(1, weight=10)


label = tk.Label(root, text="Ein Klickzähler mit tkinter")
label.grid()

button =ttk.Button(root, text="Hier klicken")
button.grid()

button2 =ttk.Button(root, text="Hier klicken 2")
button2.grid()

root.mainloop()