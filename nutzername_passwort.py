name = "Leonard"
name2 = "Sina"
passwort = "Stabil"
while 1:
    input_name = input("Nutzername? ")
    input_passwort = input("Passwort? ")

    if input_name == name and input_passwort == passwort:
        print("Herzlich Willkommen")
    elif input_name == name2 and input_passwort == passwort:
        print("Herzlich Willkommen")
    elif input_name == name and input_passwort != passwort:
        print("Ihr Passwort ist Falsch")
    elif input_name == name2 and input_passwort != passwort:
        print("Ihr Passwort ist Falsch")
    elif input_passwort == passwort and input_name != name and input_name != name2:
        print("Ihr Nutzername ist falsch")
    elif input_name != name and input_name != name2 and input_passwort!=passwort:
        print("Du bist ein Spast merk dir deine Kontodaten!!!")
    
    input()
    
