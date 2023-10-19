import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Klickzähler")
root.geometry("400x400")
root.focus()
root.columnconfigure(0,weight=1)



label = tk.Label(root, text="Ein Klickzähler mit tkinter")
label.grid(column=0, row=4 , pady= 10)

button =ttk.Button(root, text="Hier klicken")
button.grid(column=0, row=1, pady= 5)

button2 =ttk.Button(root, text="Hier klicken 2")
button2.grid(column=0, row=2, pady=5)

root.mainloop()