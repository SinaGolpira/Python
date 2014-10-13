def konto():
    nutzername=["Sina", "Leonard", "Kian", "Ahmad"]
    Passwort=["Stabil", "Stiff"]
    nutzername_input = input("Wie lautet Ihr Nutzername. ")
    passwor_input = input("Wie lautet Ihr Passwort. ")
    if nutzername == nutzername_input and passwort == passwort_input:
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
        zeichen=input("Geben Sie Ihre Rechenmethode ein: ")
        zahlzwei=float(input("Geben Sie Ihre zweite Zahl ein: "))
        print("Ihr Ergebnis ist: ", float(zahleins), zeichen, float(zahlzwei))
             
konto()
while False:
    if konto() is True:
        entscheidung=input("Wollen Sie nun den Taschenrechner (Option: 1) oder Das 1x1 einer bestimmten Zahl (Option: 2)")
    elif konto()is False:
        print("Wiederholen Sie bitte Ihre regestrierung!")
if entscheidung == (1):
    taschenrechner()
elif entscheidung == (2):
    n1x1()
else:
    print("Falsche Option! Wählen Sie zwischen 1 und 2")
