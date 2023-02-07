# OSNOVNA IGRA

# prikaz strukture igre
igraS = {
    "m" : 11, # redovi
    "n" : 14,   # kolone
    "tabla" : [],   # sadrzi polja
    "x_pocetno" : (),   # pocetne koordinate X figura
    "ox_pocetno" : (),  # pocetne koordinate O figura
    "x_trenutno" : [],  # trenutne koordinate X figura
    "ox_trenutno" : [], # trenutne koordinate O figura
    "k" : 9,            # broj plavih zidova, odnosno, zelenih zidova jednog igraca (jedan igrac ima onda 18 zidova, ukupno 36 zidova)
    "x_zidovi" : {"plavi": 9, "zeleni" : 9},        # preostali zidovi
    "ox_zidovi" : {"plavi": 9, "zeleni" : 9},       # preostali zidovi
    "izabran" : "X"
}

# prikaz strukture jednog polja
poljeS = {
    "i" : 0,
    "j" : 0,
    "igrac" : None,  # X O None 
    "zidovi" : {
        "levo" : False,
        "gore" : False,
        "desno" : False,
        "dole" : False
    }
}



from prikaz import *


# funkcija koja proverava da li je neko pobedio, da li je kraj igre
from kraj import *



from pocetnoStanje import *
from potez import *


# funkcija za odigravanje igre izmedju dva coveka
def Partija_Dva_Igraca():

    igra = Izaberi_Pocetno_Stanje(True)
    Prikaz_Stanja(igra)

    kraj = False
    pobednik = None

    while(not kraj):

        print()
        print("Na potezu: X")
        print()
        
        validan_potez = False

        if (igra["x_zidovi"]["plavi"] == 0 and igra["x_zidovi"]["zeleni"] == 0):
            bez_zida = True
        else:
            bez_zida = False

        while(not validan_potez):
            figura = Odabir_Figure()
            print()
            potez = Unos_Poteza(bez_zida)
            nova_igra = Odigraj_Potez(igra,["X",figura],[potez["vrsta"],potez["kolona"]],[potez["boja"],potez["vrsta_zid"],potez["kolona_zid"]])
            if (nova_igra != "Nevalidan potez"):
                validan_potez = True
                igra = nova_igra
            else:
                print("Nevalidan potez - Unesite nove vrednosti")
        Prikaz_Stanja(igra)

        kraj = Da_Li_Je_Kraj(igra)
        pobednik = kraj[1]
        kraj = kraj[0]
        if (kraj):
            break

        print()
        print("Na potezu: O")
        print()
        
        validan_potez = False

        if (igra["ox_zidovi"]["plavi"] == 0 and igra["ox_zidovi"]["zeleni"] == 0):
            bez_zida = True
        else:
            bez_zida = False

        while(not validan_potez):
            figura = Odabir_Figure()
            print()
            potez = Unos_Poteza(bez_zida)
            nova_igra = Odigraj_Potez(igra,["O",figura],[potez["vrsta"],potez["kolona"]],[potez["boja"],potez["vrsta_zid"],potez["kolona_zid"]])
            if (nova_igra != "Nevalidan potez"):
                validan_potez = True
                igra = nova_igra
            else:
                print("Nevalidan potez - Unesite nove vrednosti")
        Prikaz_Stanja(igra)

        kraj = Da_Li_Je_Kraj(igra)
        pobednik = kraj[1]
        kraj = kraj[0]

    print("Pobednik je: " + pobednik)

from alphabetaAlg import alphabeta, proceni_stanje_slozena

def Partija_Igrac_Kompjuter(dubina):

    igra = Izaberi_Pocetno_Stanje(False)
    Prikaz_Stanja(igra)

    kraj = False
    pobednik = None

    while(not kraj):

        if igra["izabran"] == "X":

            print()
            print("Na potezu: X")
            print()
            
            validan_potez = False

            if (igra["x_zidovi"]["plavi"] == 0 and igra["x_zidovi"]["zeleni"] == 0):
                bez_zida = True
            else:
                bez_zida = False

            while(not validan_potez):
                figura = Odabir_Figure()
                print()
                potez = Unos_Poteza(bez_zida)
                nova_igra = Odigraj_Potez(igra,["X",figura],[potez["vrsta"],potez["kolona"]],[potez["boja"],potez["vrsta_zid"],potez["kolona_zid"]])
                if (nova_igra != "Nevalidan potez"):
                    validan_potez = True
                    igra = nova_igra
                else:
                    print("Nevalidan potez - Unesite nove vrednosti")
            Prikaz_Stanja(igra)

            kraj = Da_Li_Je_Kraj(igra)
            pobednik = kraj[1]
            kraj = kraj[0]
            if (kraj):
                break

            igra = alphabeta(igra, dubina, "O")
            Prikaz_Stanja(igra)

            kraj = Da_Li_Je_Kraj(igra)
            pobednik = kraj[1]
            kraj = kraj[0]

        else:

            igra = alphabeta(igra, dubina, "X")
            Prikaz_Stanja(igra)

            kraj = Da_Li_Je_Kraj(igra)
            pobednik = kraj[1]
            kraj = kraj[0]
            if (kraj):
                break

            print()
            print("Na potezu: O")
            print()
            
            validan_potez = False

            if (igra["ox_zidovi"]["plavi"] == 0 and igra["ox_zidovi"]["zeleni"] == 0):
                bez_zida = True
            else:
                bez_zida = False

            while(not validan_potez):
                figura = Odabir_Figure()
                print()
                potez = Unos_Poteza(bez_zida)
                nova_igra = Odigraj_Potez(igra,["O",figura],[potez["vrsta"],potez["kolona"]],[potez["boja"],potez["vrsta_zid"],potez["kolona_zid"]])
                if (nova_igra != "Nevalidan potez"):
                    validan_potez = True
                    igra = nova_igra
                else:
                    print("Nevalidan potez - Unesite nove vrednosti")
            Prikaz_Stanja(igra)

            kraj = Da_Li_Je_Kraj(igra)
            pobednik = kraj[1]
            kraj = kraj[0]

    print("Pobednik je: " + pobednik)


print("Izaberite tip igre:")
print("a) Dva igraca")
print("b) Jedan igrac")
ailib = input()
if (ailib == "a"):
    Partija_Dva_Igraca()    
elif (ailib == "b"):
    Partija_Igrac_Kompjuter(3)          
else:
    print("Unesite a ili b")





# igra = Izaberi_Pocetno_Stanje(False)
# Prikaz_Stanja(igra)
# igra = Odigraj_Potez(igra,["X",1],[4,6],["Z",1,1])
#  #igra = Odigraj_Potez(igra,["X",1],[8,10],["Z",4,4])
# if (igra != "Nevalidan potez"):
#     Prikaz_Stanja(igra)
# else:
#     print(igra)
# igra = Odigraj_Potez(igra,["X",1],[4,8],["P",5,5])
# if (igra != "Nevalidan potez"):
#     Prikaz_Stanja(igra)
# else:
#     print(igra)
# igra = Odigraj_Potez(igra,["X",1],[4,10],["Z",2,6])
# if (igra != "Nevalidan potez"):
#     Prikaz_Stanja(igra)
# else:
#     print(igra)

# print(proceni_stanje_slozena(igra))

# igra["x_zidovi"] = {"plavi" : 0, "zeleni" : 0}
# igra["ox_zidovi"] = {"plavi" : 0, "zeleni" : 0}

# stanje = alphabeta(igra, 3, "X")
# Prikaz_Stanja(stanje)


#Partija_Dva_Igraca()
#igra = Odigraj_Potez(igra,["X",1],[6,6],["P",2,11])
#if (igra != "Nevalidan potez"):
    #Prikaz_Stanja(igra)
#else:
    #print(igra)

# igra["x_zidovi"] = {"plavi" : 0, "zeleni" : 0}
# igra["ox_zidovi"] = {"plavi" : 0, "zeleni" : 0}

# lista = Vrati_Moguca_Nova_Stanja(igra,"X")
# xlista = lista


# igra = Pripremi_Pocetno_Stanje(11,14,[4,4],[8,4],[4,11],[8,11],9)
# #igra["tabla"][3][3]["igrac"] = "O"
# #print(Da_Li_Je_Kraj(igra))
# Prikaz_Stanja(igra)
# nova_igra = Odigraj_Potez(igra, ["X", 2], [8,6], ["Z",4,4])
# if nova_igra == "Nevalidan potez":
#     print("Nevalidan potez")
# else:
#     Prikaz_Stanja(nova_igra)

# nova_igra = Odigraj_Potez(nova_igra, ["X", 2], [8,8], ["P",2,2])
# if nova_igra == "Nevalidan potez":
#     print("Nevalidan potez")
# else:
#     Prikaz_Stanja(nova_igra)

# nova_igra["tabla"][nova_igra["x_trenutno"][1][0]][nova_igra["x_trenutno"][1][1]]["igrac"] = None
# nova_igra["x_trenutno"][1][1] = 9
# nova_igra["tabla"][nova_igra["x_trenutno"][1][0]][nova_igra["x_trenutno"][1][1]]["igrac"] = "X"

# nova_igra = Odigraj_Potez(nova_igra, ["X", 2], [8,11], ["P",4,4])
# if nova_igra == "Nevalidan potez":
#     print("Nevalidan potez")
# else:
#     Prikaz_Stanja(nova_igra)
#     print(Da_Li_Je_Kraj(nova_igra))


