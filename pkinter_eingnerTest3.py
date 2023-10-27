import tkinter as tk

text1="Klick mich"

def mein_unterprogramm():
    # Code, der ausgeführt wird, wenn der Button angeklickt wird
    print("Button wurde geklickt!")
   
   

# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Button Beispiel")

# Button erstellen und zum Fenster hinzufügen
button = tk.Button(fenster, text=text1, command=mein_unterprogramm)
button.pack()

# Haupt-Eventloop starten
fenster.mainloop()