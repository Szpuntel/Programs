from tkinter import *
import os
base_folder = os.path.dirname(__file__)
cuboid_path = os.path.join(base_folder, 'cuboid.png')

window = Tk()
window.geometry()
window.config(background="black")

x = IntVar()
photo_cuboid = PhotoImage(file=cuboid_path)

def submit():
    entry.delete(0, END)
    l = entry_1.get()
    w = entry_2.get()
    h = entry_3.get()
    wynik = int(l)*int(w)*int(h)
    entry.insert(0,str(wynik))

label_1 = Label(window, fg="white", bg="black",font=('Arial', 10, 'bold'), text="Podaj l prostopadłościanu: ")
label_2 = Label(window, fg="white", bg="black",font=('Arial', 10, 'bold'), text="Podaj w prostopadłościanu: ", pady=5)
label_3 = Label(window, fg="white", bg="black",font=('Arial', 10, 'bold'), text="Podaj h prostopadłościanu: ")
photo_cuboid_label = Label(window,bd = 0, image=photo_cuboid)


entry_1 = Entry(window, bg="#141313", fg="white")
entry_2 = Entry(window,bg="#141313", fg="white")
entry_3 = Entry(window, bg="#141313", fg="white")

button = Button(window,text="Policz",         
                           command=submit,
                           font=('Arial',15),
                           fg="red", bg="black",
                           pady=1)

label_1.pack()
entry_1.pack()
label_2.pack() 
entry_2.pack()
label_3.pack()
entry_3.pack()
photo_cuboid_label.pack()
button.pack(side="left")
entry = Entry(window, font=('Arial',20,'bold'), width=10, fg="white", bg="#141313")
entry.pack(side="left")






window.mainloop()