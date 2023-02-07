# FUNKCIJE ZA POSTAVLJANJE POCETNOG STANJA

# funkcija u kojoj korisnik bira parametre pocetka igre preko konzole
def Izaberi_Pocetno_Stanje(dva_igraca):
    print("BLOCKADE")
    print()
    pogresno_izabran = True
    xiliox = ""

    if(dva_igraca):
        xiliox = "X"
    else:
        while(pogresno_izabran):                            # ceka se unos x ili o sve dok nije pravilno izabrano cime igrac bira da li prvi igra
            print("Izaberite stranu: X ili O")
            xiliox = input()
            if (xiliox == "X" or xiliox == "x" or xiliox == "O" or xiliox == "o"):
                pogresno_izabran = False

    pogresno_izabran = True
    while(pogresno_izabran):
        print("Izaberite velicinu table:")
        print("a) 11x14")
        print("b) 22x28")
        ailib = input()
        if (ailib == "a"):
            m=11
            n=14
            pogresno_izabran = False
        elif (ailib == "b"):
            m=22
            n=28
            pogresno_izabran = False
        else:
            print("Unesite a ili b")
    
    pogresno_izabran = True
    while(pogresno_izabran):
        print("Izaberite broj zidica:")
        print("a) 9 plavih i 9 zelenih po igracu")
        print("b) 18 plavih i 18 zelenih po igracu")
        ailib = input()
        if (ailib == "a"):
            k=9
            pogresno_izabran = False
        elif (ailib == "b"):
            k=18
            pogresno_izabran = False
        else:
            print("Unesite a ili b")

    if (m == 11):
        return Pripremi_Pocetno_Stanje(m,n,[4,4],[8,4],[4,11],[8,11],k,xiliox.upper())
    else:
        return Pripremi_Pocetno_Stanje(m,n,[8,8],[15,8],[8,21],[15,21],k,xiliox.upper())


# funkcija koja prilagodjava unete vrednosti od strane korisnika za dalje koriscenje (koordinate smanjuje za 1, jer pocinju od 0)
def Pripremi_Pocetno_Stanje(m, n, x_prvi_pesak, x_drugi_pesak, ox_prvi_pesak, ox_drugi_pesak, k, izabran):
    x_prvi_pesak[0] -= 1
    x_prvi_pesak[1] -= 1
    x_drugi_pesak[0] -= 1
    x_drugi_pesak[1] -= 1
    ox_prvi_pesak[0] -= 1
    ox_prvi_pesak[1] -= 1
    ox_drugi_pesak[0] -= 1
    ox_drugi_pesak[1] -= 1
    return Pocetno_Stanje(m, n, x_prvi_pesak, x_drugi_pesak, ox_prvi_pesak, ox_drugi_pesak, k, izabran)


# funkcija koja formira strukturu stanja odnosno igre i vraca je na osnovu izabranih pocetnih parametara
def Pocetno_Stanje(m, n, x_prvi_pesak, x_drugi_pesak, ox_prvi_pesak, ox_drugi_pesak, k, izabran):

    igra = dict()
    igra["m"] = m
    igra["n"] = n
    igra["tabla"] = list()

    for i in range(0, m):
        red = list()
        for j in range(0,n):
            polje = dict()
            polje["i"] = i
            polje["j"] = j

            polje["igrac"] = None
            if (i == x_prvi_pesak[0] and j == x_prvi_pesak[1] or i == x_drugi_pesak[0] and j == x_drugi_pesak[1]):
                polje["igrac"] = "X"
            if (i == ox_prvi_pesak[0] and j == ox_prvi_pesak[1] or i == ox_drugi_pesak[0] and j == ox_drugi_pesak[1]):
                polje["igrac"] = "O"

            polje["zidovi"] = dict()
            polje["zidovi"]["levo"] = False
            polje["zidovi"]["gore"] = False
            polje["zidovi"]["desno"] = False
            polje["zidovi"]["dole"] = False

            red.append(polje)
        igra["tabla"].append(red)

    igra["x_pocetno"] = (x_prvi_pesak, x_drugi_pesak)
    igra["x_trenutno"] = [x_prvi_pesak, x_drugi_pesak]
    igra["ox_pocetno"] = (ox_prvi_pesak, ox_drugi_pesak)
    igra["ox_trenutno"] = [ox_prvi_pesak, ox_drugi_pesak]
    igra["k"] = k
    igra["x_zidovi"] = dict()
    igra["x_zidovi"]["plavi"] = k
    igra["x_zidovi"]["zeleni"] = k
    igra["ox_zidovi"] = dict()
    igra["ox_zidovi"]["plavi"] = k
    igra["ox_zidovi"]["zeleni"] = k

    igra["izabran"] = izabran

    return igra