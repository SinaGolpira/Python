def konto():
    nutzername=["Sina", "Leonard", "Kian", "Ahmad"]
    passwort=["Stabil", "Stiff"]
    nutzername_input = input("Wie lautet Ihr Nutzername. ")
    passwort_input = input("Wie lautet Ihr Passwort. ")
    if nutzername_input in nutzername and passwort_input in passwort:
        return True
    else:
        return False

def n1x1():
	zahl = int(input("Welches 1x1 wollen Sie? "))
	#for i in range (1, 11):
def taschenrechner():
        print("Zu Ihrer Information: ")
        print("Plus = +")
        print("Minus = -")
        print("Mal = *")
        print("Geteilt = /")
        print("Hoch = **")
        zahleins=float(input("Geben Sie Ihre erste Zahl ein: "))
        methode=input("Geben Sie Ihre Rechenmethode ein: ")
        zahlzwei=float(input("Geben Sie Ihre zweite Zahl ein: "))
        if methode=="+":
            print("Ihr Ergebnis ist: ", float(zahleins)+float(zahlzwei))
        elif methode=="-":
            print("Ihr Ergebnis ist: ", float(zahleins)-float(zahlzwei))
        elif methode=="*":
            print("Ihr Ergebnis ist: ", float(zahleins)*float(zahlzwei))    
        elif methode=="/":
            print("Ihr Ergebnis ist: ", float(zahleins)/float(zahlzwei))    
        elif methode=="**":
            print("Ihr Ergebnis ist: ", float(zahleins)**float(zahlzwei))   
        else:
            print ("Syntax Fehler")

while konto() == False:
    print("Wiederholen Sie bitte Ihre regestrierung!")

entscheidung=input("Wollen Sie nun den Taschenrechner (Option: 1) oder Das 1x1 einer bestimmten Zahl (Option: 2)")

if entscheidung == "1":
    taschenrechner()
elif entscheidung == "2":
    n1x1()
else:
    print("Falsche Option! Wählen Sie zwischen 1 und 2")
