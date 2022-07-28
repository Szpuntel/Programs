from tkinter import *
from tkinter import ttk
import random
import itertools

window = Tk()
number = 1
notebook = ttk.Notebook(window)

tab0 = Frame(notebook, bg='#048a6f')
tab1 = Frame(notebook, bg='#048a6f')
tab2 = Frame(notebook, bg='#048a6f')

notebook.add(tab0, text="Strona główna")
notebook.add(tab1, text="Rejestracja")
notebook.add(tab2, text="Przelewy")
notebook.pack()

window.config(bg='#048a6f')

class Bank:

    balance = 100
    client_list = []
    newid = itertools.count().__next__

    def __init__(self,firstname,lastname,age,email,pesel,password):
        self.id = Bank.newid()
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.pesel = pesel
        self.password = password
        self.balance
        Bank.client_list.append(str(self.id) + ". " +self.firstname + " " + self.lastname)



    def add_balance(self,amount):
        self.balance += amount
        print("You have added: ", amount ," to your account")
        print("Your current balance:", self.balance)


    def transfer_money():
        amount = kwota.get()
        from_who = przelew1.get()
        to_who = przelew2.get()
        from_who = f'client_{from_who}'
        to_who = f'client_{to_who}'
        Bank.transfer_money2(from_who, to_who, amount)

    def transfer_money2(cli1,cli2,amo):
        cli1.balance -= amo
        cli2.balance += amo
        print(cli1.balance, cli2.balance)
        
    def check_balance(self):
        print("Your current balance:", self.balance)

def refresh_list():
    global number
    listbox.delete(0,END)
    for client in Bank.client_list:
        listbox.insert(number,client)
        number += 1
    listbox.pack()


def register():
    client_number = random.randint(000000,999999)
    client_new ="Client_",client_number
    imie = eimie.get()
    nazwisko = enazwisko.get()
    wiek = ewiek.get()
    email = eemail.get()
    pesel = epesel.get()
    haslo = ehaslo.get()

    if ehaslo.get() == ehaslo2.get():
        client_new = Bank(f"{imie}",f"{nazwisko}",f"{wiek}",f"{email}",f"{pesel}",f"{haslo}")
        if client_new.balance == 100:
            print("Witaj ",client_new.firstname)
            print("Rejestracja powiodła sie :) Możesz juz korzystac z swojego zasranego konta !")

        else:
            print("Sorry mordo coś poszło nie tak spróbuj ponownie pozniej")
    else:
        print("Hasła nie są takie same")


opis= '''Mamy unikalną kulturę organizacyjną,
a wyróżniają nas ludzie!Tworzymy aplikacje
 webowe, mobilne i narzędzia technologiczne,
z których skorzystało już ponad 5,5 mln 
naszych klientów.Cenimy poczucie stabilności
 i bezpieczeństwa, możliwości rozwoju
oraz... swój czas – w pracy i po pracy.
Wiemy, że wokół świata IT krążą plotki, mity,
domysły.Ale jak jest naprawdę?
Sprawdź, co o tym i innych powszechnych
opiniach myślimy w mBanku '''

text_box = Text(
    tab0,
    bg='#048a6f',
    height=12,
    width=45
)

listbox = Listbox(tab2)
listbox2 = Listbox(tab2)

button_confirm = Button(tab2, text="Wybierz", command=Bank.transfer_money)
button_refresh = Button(tab2,text="Odśwież Klientów", command=refresh_list)
button_register = Button(tab1,text="Rejstracja", command=register, font=('Arial',16,'bold'),bg='gray')

lkwota = Label(tab2, text="Ile przelać?")
przelew_z = Label(tab2,text="Przelew z:")
przelew_na = Label(tab2,text="Przelew na:")
powitanie = Label(tab0,text='Witaj w banku HajsSieZgadza', font=('Arial',16,'bold'),bg='#048a6f' )
pimie = Label(tab1,text="Imię: ")
pnazwisko = Label(tab1,text="Nazwisko: ")
pemail = Label(tab1,text="E-mail: ")
pwiek = Label(tab1,text="Wiek: ")
ppesel = Label(tab1,text="Pesel: ")
phaslo= Label(tab1,text="Hasło: ")
phaslo2 = Label(tab1,text="Powtórz hasło: ")

kwota = Entry(tab2)
przelew1 = Entry(tab2)
przelew2 = Entry(tab2)
eimie = Entry(tab1)
enazwisko = Entry(tab1)
eemail = Entry(tab1)
ewiek = Entry(tab1)
epesel = Entry(tab1)
ehaslo = Entry(tab1)
ehaslo2= Entry(tab1)


# tab0 - Powitanie
powitanie.pack()
text_box.pack(expand=True)
text_box.insert('end', opis)
text_box.config(state='disabled')

# tab 1 - Rejestracja
pimie.grid(column=0,row=0)
eimie.grid(column=1,row=0)
pnazwisko.grid(column=0,row=1)
enazwisko.grid(column=1,row=1)
pwiek.grid(column=0,row=2)
ewiek.grid(column=1,row=2)
pemail.grid(column=0,row=3)
eemail.grid(column=1,row=3)
ppesel.grid(column=0,row=4)
epesel.grid(column=1,row=4)
phaslo.grid(column=0,row=5)
ehaslo.grid(column=1,row=5)
phaslo2.grid(column=0,row=6)
ehaslo2.grid(column=1,row=6)
button_register.grid(column=1,row=7)

# tab 2 - Przelewy
przelew_z.place(x=60,y=0)
przelew_na.place(x=52,y=20)
lkwota.place(x=55,y=38)
przelew1.pack()
przelew2.pack()
kwota.pack()
button_confirm.pack()
button_refresh.pack()



# for value  in Bank.client_list:
#     print (value)





client_1 = Bank("Rafał","Mamoa","szpuntel@gmail.com","26",'9604593955',"okon")
client_2 = Bank("Endriu","Iglesias","enrikoiglo@gmail.com","33",'8674635557',"espaniol")

print(type(client_1))



window.mainloop()