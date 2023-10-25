import tkinter as tk

root = tk.Tk()
root.title("Eigener Test 2")
root.geometry("400x400")
root.focus()
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

fenster1=tk.Label(root)

fenster1.grid()

ButtonTest = tk.Button(root, text="Button 1")
ButtonTest.grid(column=1, row=1, pady= 5, sticky="w")


root.mainloop()