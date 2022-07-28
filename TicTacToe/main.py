
from tkinter import *
import math

window = Tk()
nvar = IntVar()
whos_turn = 0


icon = PhotoImage(file='./icon.png')
iconx = PhotoImage(file='./iconx.png')
icono = PhotoImage(file='./icono.png')

game_table = []
for i in range(1, 11):
    game_table.append("None")

def restart():
    window.destroy()

def check_clicked_button():
    global game_table
    if game_table[1] == "X":
        global icon 
        icon = PhotoImage(file='./iconx.png')

def where_to_put(place,value):
    if value == "x":
        button = Checkbutton(window,image=iconx)
    if value == "o":
        button = Checkbutton(window,image=icono)

    row = math.ceil(place/3) - 1
    col = (place - 1) % 3
    button.grid(column=col, row=row)

    print(row, col)

def put_o(place):
    where_to_put(place,"o")
        
def put_x(place):
    where_to_put(place,"x")


def check_winner(mark):
    #Left from right
    for y in range(3):
        markers = 0
        for x in range(3):
            if game_table[(x + y*3 + 1)] == mark:
                markers = markers + 1
                
        if markers == 3:
            return True
            
    #Up to down
    for x in range(3):
        markers = 0
        for y in range(3):
            if game_table[(x + y*3 + 1)] == mark:
                markers = markers + 1
                
        if markers == 3:
            return True
            
            
    #Diagonal
    if game_table[5] == mark:
        if game_table[1] == mark and game_table[9] == mark:
            return True
        
        if game_table[3] == mark and game_table[7] == mark:
            return True
    
    #If no combination has been found, return false
    return False

    

def place_value():
    global whos_turn
    place = nvar.get()
    print(place)
    if whos_turn % 2 == 0:
        print("Player O turn")
        game_table[place] = "X"
        put_x(place)
    else:
        print("Player X turn")
        game_table[place] = "O"
        put_o(place)        

    whos_turn += 1

    if whos_turn >= 5:
        if check_winner("X") == True:
            label_x_winner.grid(column=1, row=3)
            restartbutton.grid(column=1,row=4)
        
        if check_winner("O") == True:
            label_o_winner.grid(column=1, row=3)
            restartbutton.grid(column=1,row=4)
            
    if whos_turn == 9:
        label.grid(column=1, row=3)
        restartbutton.grid(column=1,row=4)


label = Label(window, text="Draw", font=('Arial', 15),fg="red")
label_x_winner = Label(window, text="X Won!", font=('Arial', 15),fg="red")
label_o_winner = Label(window, text="O Won!", font=('Arial', 15),fg="red")

restartbutton = Button(window,text="EXIT", font=('Arial',15),command=restart)

for x in range(3):
    for y in range(3):
        print(x, y, x + y*3 + 1)
        button = Checkbutton(window, command = place_value, variable=nvar, onvalue=x + y*3 + 1, image=icon)
        button.grid(column=x, row=y)


window.mainloop()