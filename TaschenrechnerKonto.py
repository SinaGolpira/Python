nutzername= ["Sina", "Kian", "Leonard"]
passwort="Stiff"
def passwortListe():
    input_nutzername = input("Nutzername: ")
    input_passwort = input("Passwort: ")
    if input_nutzername in nutzername and input_passwort == passwort:
        return True
    else:
        return False 

def taschenrechner():
    zahleins=input("Schreiben Sie bitte ihre erste Zahl: ")
    methode=input("Schreiben Sie bitte ihre Rechenmethode: ")
    zahlzwei=input("Schrieben Sie bitte ihre zweite Zahl: ")
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
    input()
while True:
    if passwortListe():
        taschenrechner()
    else:
        print("Bitte wiederholen Sie ihren Log-in")
    
