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
label.grid(pady=20)

button =ttk.Button(root, text="Hier klicken")
button.grid(sticky="w", padx=10)

button2 =ttk.Button(root, text="Hier klicken 2")
button2.grid(sticky="we", padx=10, pady=10)

button3 =ttk.Button(root, text="Hier klicken 3")
button3.grid(padx=10, pady=10)

root.mainloop()