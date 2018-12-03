from tkinter import *

# Initialisierung eines Gui-Fensters
window = Tk()
# Titel des Fensters
window.title("my own gui")
window.geometry("198x108")


label1 = Label(window,text="Hello")
label1.pack(side="right")

# Exit-Button
button2 = Button(window,text="Exit",command=exit)
button2.pack(side="right")






# Zeigt das Gui-Fenster an
window.mainloop()
