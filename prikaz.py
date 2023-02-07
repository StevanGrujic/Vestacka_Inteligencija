hex = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"] # G = 10 itd. zbog poravnanja
uspravno_jednako = chr(0x01C1)
duga_crta = chr(8212)

# funkcija za prikaz table
def Prikaz_Stanja(igra):

    print(" ", end = " ")
    for br in range(0, igra["n"]):
        print(hex[br],end=" ")
    print(" ")

    print(" ", end = " ")
    for br in range(0, igra["n"]):
        print("=", end = " ")
    print(" ")

    for vrsta in range(0, igra["m"]):

        print(hex[vrsta] + uspravno_jednako, end = "")
        for br in range(0, igra["n"]):
            polje = igra["tabla"][vrsta][br]
            print(polje["igrac"] if polje["igrac"] != None else " " , end = "")
            if br == igra["n"] - 1:
                print(uspravno_jednako + hex[vrsta])
            else:
                if polje["zidovi"]["desno"] == True:
                    print(uspravno_jednako, end = "")
                else:
                    print("|", end = "")
        print(" ",end=" ")

        for br in range(0, igra["n"]):
            polje = igra["tabla"][vrsta][br]
            if vrsta != igra["m"] - 1:
                if polje["zidovi"]["dole"] == True:
                    print("=", end = " ")
                else:
                    print(duga_crta, end = " ")
            else:
                print("=",end=" ")
        print()

    print(" ", end = " ")
    for br in range(0, igra["n"]):
        print(hex[br], end = " ")
    print(" ")