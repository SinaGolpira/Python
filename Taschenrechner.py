plus="+"
minus="-"
mal="*"
geteilt="/"
hoch="**"
while 1:
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



    
