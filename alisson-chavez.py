Edad = 19
Tiene_licencia = False

if Edad >= 18 :
    print("Puede tramitar un pasaporte")
    if Tiene_licencia == True :
        print ("Puede viajar sin pasaporte")
    else: 
        print ("Necesita pasaporte")
else:
    print ("No puede tramitar un pasaporte")