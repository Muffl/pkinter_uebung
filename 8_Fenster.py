import tkinter as tk


root=tk.Tk()
root.geometry("480x480")

label1=tk.Label(root, text="Label 1", bg="green")
label1.pack(side="top", expand=True, fill="y") #Für side ist top, right, left und bottom möglich

label1=tk.Label(root, text="Label 2", bg="red")
label1.pack(side="top", expand=True, fill="both")

root.mainloop()