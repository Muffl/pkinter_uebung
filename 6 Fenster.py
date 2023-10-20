import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Klickzähler")
root.geometry("400x400")
root.focus()
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)



label = tk.Label(root, text="Ein Klickzähler mit tkinter")
label.grid(column=0, row=4, columnspan=2)

button_label= ttk.Label(root, text="Klickzähler +1:")
button_label.grid(column=0, row=1, sticky="e")

button =ttk.Button(root, text="Hier klicken")
button.grid(column=1, row=1, pady= 5, sticky="w")

button2_label= ttk.Label(root, text="Klickzähler +5:")
button2_label.grid(column=0, row=2, sticky="e")


button2 =ttk.Button(root, text="Hier klicken für +5")
button2.grid(column=1, row=2, pady=5, sticky="w")

root.mainloop()