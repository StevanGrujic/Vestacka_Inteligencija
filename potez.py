from proverePoteza import *
# FUNKCIJE ZA ODIGRAVANJE POTEZA

# funkcija koja priprema sve potrebne parametre za potez, proverava da li je validan i izvrsava potez
def Odigraj_Potez(igra, figura, odabrano_polje, zid):   # [X 2] [6 3] [Z 4 9]
    figura[1] -= 1
    odabrano_polje[0] -= 1
    odabrano_polje[1] -= 1
    zid[1] -= 1
    zid[2] -= 1
    if (zid[0] == 0):
        if Proveriti_Potez_Pesaka(igra,figura, odabrano_polje):
            return Potez(igra, figura, odabrano_polje, zid)
    else:
        if Proveriti_Potez_Pesaka(igra,figura, odabrano_polje) and Proveriti_Potez_Zid(igra, figura, zid):      # provere da li je potez validan pre izvrsavanja poteza
            return Potez(igra, figura, odabrano_polje, zid)
    return "Nevalidan potez"

from stanje import *

# funkcija koja menja stanje igre na osnovu prosledjenih parametara
def Potez(igra, figura, odabrano_polje, zid):
    novo_stanje_igre = Napravi_kopiju_stanja(igra)
    xoxfigura = None
    if figura[0] == "X":
        xoxfigura = "x_trenutno"
        xoxzid = "x_zidovi"
    else:
        xoxfigura = "ox_trenutno"
        xoxzid = "ox_zidovi"
    koordinate_polja_odabrane_figure = novo_stanje_igre[xoxfigura][figura[1]]
    novo_stanje_igre["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["igrac"] = None
    koordinate_polja_odabrane_figure[0] = odabrano_polje[0]
    koordinate_polja_odabrane_figure[1] = odabrano_polje[1]
    novo_stanje_igre["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["igrac"] = figura[0]        # postavljanje figure na odabrano mesto

    if novo_stanje_igre[xoxzid]["plavi"] == 0 and novo_stanje_igre[xoxzid]["zeleni"] == 0:
        return novo_stanje_igre
    
    if zid[0] == "P":       # plavi horizontalno, zeleni vertikalno
        novo_stanje_igre[xoxzid]["plavi"] -= 1
        novo_stanje_igre["tabla"][zid[1]][zid[2]]["zidovi"]["dole"] = True
        novo_stanje_igre["tabla"][zid[1]][zid[2]+1]["zidovi"]["dole"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]]["zidovi"]["gore"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]+1]["zidovi"]["gore"] = True
    else:                                                                                                                           # postavljanje zida na odabrano mesto
        novo_stanje_igre[xoxzid]["zeleni"] -= 1
        novo_stanje_igre["tabla"][zid[1]][zid[2]]["zidovi"]["desno"] = True
        novo_stanje_igre["tabla"][zid[1]][zid[2]+1]["zidovi"]["levo"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]]["zidovi"]["desno"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]+1]["zidovi"]["levo"] = True

    if (4*novo_stanje_igre["k"] - (novo_stanje_igre["x_zidovi"]["plavi"] + novo_stanje_igre["x_zidovi"]["zeleni"] + novo_stanje_igre["ox_zidovi"]["plavi"] + novo_stanje_igre["ox_zidovi"]["zeleni"]) > 3):
        if (Proveriti_Put(novo_stanje_igre) == False):
            return "Nevalidan potez"

    return novo_stanje_igre


def Postavi_Prvi_Validan_Zid(igra, figura):
    novo_stanje_igre = Napravi_kopiju_stanja(igra)
    m = igra["m"]
    n = igra["n"]
    if figura == "X":
        xoxzid = "x_zidovi"
    else:
        xoxzid = "ox_zidovi"
    if novo_stanje_igre[xoxzid]["plavi"] == 0 and novo_stanje_igre[xoxzid]["zeleni"] == 0:
        return novo_stanje_igre
    for red in range(0,m):
        for kolona in range(0,n):
            rezultat = Postavi_Zid(novo_stanje_igre, figura, ["P",red,kolona])
            if rezultat != "Nevalidan potez":
                return rezultat  
            rezultat = Postavi_Zid(novo_stanje_igre, figura, ["Z",red,kolona])
            if rezultat != "Nevalidan potez":
                return rezultat

def Vrati_Prvi_Validan_Zid(igra, figura):
    novo_stanje_igre = Napravi_kopiju_stanja(igra)
    m = igra["m"]
    n = igra["n"]
    if figura == "X":
        xoxzid = "x_zidovi"
    else:
        xoxzid = "ox_zidovi"
    if novo_stanje_igre[xoxzid]["plavi"] == 0 and novo_stanje_igre[xoxzid]["zeleni"] == 0:
        return novo_stanje_igre
    for red in range(0,m):
        for kolona in range(0,n):
            rezultat = Postavi_Zid(novo_stanje_igre, figura, ["P",red,kolona])
            if rezultat != "Nevalidan potez":
                return ["P",red,kolona] 
            rezultat = Postavi_Zid(novo_stanje_igre, figura, ["Z",red,kolona])
            if rezultat != "Nevalidan potez":
                return ["Z",red,kolona]


def Postavi_Zid(igra, figura, zid):

    if Proveriti_Potez_Zid(igra, figura, zid) == False:
        return "Nevalidan potez"

    novo_stanje_igre = Napravi_kopiju_stanja(igra)
    if figura == "X":
        xoxzid = "x_zidovi"
    else:
        xoxzid = "ox_zidovi"
    if zid[0] == "P":       # plavi horizontalno, zeleni vertikalno
        novo_stanje_igre[xoxzid]["plavi"] -= 1
        novo_stanje_igre["tabla"][zid[1]][zid[2]]["zidovi"]["dole"] = True
        novo_stanje_igre["tabla"][zid[1]][zid[2]+1]["zidovi"]["dole"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]]["zidovi"]["gore"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]+1]["zidovi"]["gore"] = True
    else:                                                                                                                           # postavljanje zida na odabrano mesto
        novo_stanje_igre[xoxzid]["zeleni"] -= 1
        novo_stanje_igre["tabla"][zid[1]][zid[2]]["zidovi"]["desno"] = True
        novo_stanje_igre["tabla"][zid[1]][zid[2]+1]["zidovi"]["levo"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]]["zidovi"]["desno"] = True
        novo_stanje_igre["tabla"][zid[1]+1][zid[2]+1]["zidovi"]["levo"] = True

    if (Proveriti_Put(novo_stanje_igre) == False):
       return "Nevalidan potez"

    return novo_stanje_igre


# funkcija koja vraca sva moguca nova stanja
def Vrati_Moguca_Nova_Stanja(igra, na_potezu):
    lista_mogucih_stanja = list()
    m = igra["m"]
    n = igra["n"]
    if na_potezu == "X":
        xoxfigura = "x_trenutno"
        xoxzid = "x_zidovi"
    else:
        xoxfigura = "ox_trenutno"
        xoxzid = "ox_zidovi"
        
    for redni_broj_figure in range(0,2):

        i = igra[xoxfigura][redni_broj_figure][0]
        j = igra[xoxfigura][redni_broj_figure][1]
        polja = [[i-2,j],[i-1,j],[i+1,j],[i+2,j],[i,j-2],[i,j-1],[i,j+1],[i,j+2],[i+1,j+1],[i-1,j+1],[i+1,j-1],[i-1,j-1]]
        if igra[xoxzid]["plavi"] == 0 and igra[xoxzid]["zeleni"] == 0:
            for odabrano_polje in polja:
                if Proveriti_Potez_Pesaka(igra,[na_potezu,redni_broj_figure], odabrano_polje):
                    rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, [0,0,0])
                    if rezultat != "Nevalidan potez":
                        lista_mogucih_stanja.append(rezultat)
        else:
            for odabrano_polje in polja:
                for red in range(0,m):
                    for kolona in range(0,n):
                        if Proveriti_Potez_Pesaka(igra,[na_potezu,redni_broj_figure], odabrano_polje) and Proveriti_Potez_Zid(igra, [na_potezu,redni_broj_figure], ["P",red,kolona]):      
                            rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, ["P",red,kolona])
                            if rezultat != "Nevalidan potez":
                                lista_mogucih_stanja.append(rezultat)
                        if Proveriti_Potez_Pesaka(igra,[na_potezu,redni_broj_figure], odabrano_polje) and Proveriti_Potez_Zid(igra, [na_potezu,redni_broj_figure], ["Z",red,kolona]):      
                            rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, ["Z",red,kolona])
                            if rezultat != "Nevalidan potez":
                                lista_mogucih_stanja.append(rezultat)

    return lista_mogucih_stanja


# funkcija koja vraca sva moguca nova stanja
def Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove(igra, na_potezu):

    lista_mogucih_stanja = list()
    m = igra["m"]
    n = igra["n"]
    if na_potezu == "X":
        xoxfigura = "x_trenutno"
        xoxzid = "x_zidovi"
        protivnik = "ox_trenutno"
    else:
        xoxfigura = "ox_trenutno"
        xoxzid = "ox_zidovi"
        protivnik = "x_trenutno"

    for redni_broj_figure in range(0,2):

        i = igra[xoxfigura][redni_broj_figure][0]
        j = igra[xoxfigura][redni_broj_figure][1]
        polja = [[i-2,j],[i-1,j],[i+1,j],[i+2,j],[i,j-2],[i,j-1],[i,j+1],[i,j+2],[i+1,j+1],[i-1,j+1],[i+1,j-1],[i-1,j-1]]
        if igra[xoxzid]["plavi"] == 0 and igra[xoxzid]["zeleni"] == 0:
            for odabrano_polje in polja:
                if Proveriti_Potez_Pesaka(igra,[na_potezu,redni_broj_figure], odabrano_polje):
                    rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, [0,0,0])
                    if rezultat != "Nevalidan potez":
                        lista_mogucih_stanja.append(rezultat)
        else:
            for odabrano_polje in polja:
                heuristika_zid = Heuristika_Zida(igra,na_potezu,odabrano_polje,i,j,protivnik, xoxzid, xoxfigura)
                if Proveriti_Potez_Pesaka(igra,[na_potezu,redni_broj_figure], odabrano_polje):
                    if Proveriti_Potez_Zid(igra, [na_potezu,redni_broj_figure], heuristika_zid):      
                            rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, heuristika_zid)
                            if rezultat != "Nevalidan potez":
                                lista_mogucih_stanja.append(rezultat)
                            else:
                                rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, Vrati_Prvi_Validan_Zid(igra,na_potezu))   # ako heuristika nije validna, onda vraca prvu mogucu opciju za zid
                                if rezultat != "Nevalidan potez":
                                    lista_mogucih_stanja.append(rezultat)
                    else:
                        rezultat = Potez(igra, [na_potezu,redni_broj_figure], odabrano_polje, Vrati_Prvi_Validan_Zid(igra,na_potezu))   # ako heuristika nije validna, onda vraca prvu mogucu opciju za zid
                        if rezultat != "Nevalidan potez":
                            lista_mogucih_stanja.append(rezultat)
                    
    return lista_mogucih_stanja


def Heuristika_Zida(igra, na_potezu, odabrano_polje, i, j, protivnik, xoxzid, xoxfigura):

    if na_potezu == "X":
        xoxpoc = "x_pocetno"
    else:
        xoxpoc = "ox_pocetno"
    if igra[xoxzid]["plavi"] + igra[xoxzid]["zeleni"] > 2*igra["k"] - 6:
        x_pocetno_0_i = igra[xoxpoc][0][0]
        x_pocetno_0_j = igra[xoxpoc][0][1]
        x_pocetno_1_i = igra[xoxpoc][1][0]
        x_pocetno_1_j = igra[xoxpoc][1][1]
        if na_potezu == 'X':
            lista = [['Z',x_pocetno_0_i,x_pocetno_0_j],['Z',x_pocetno_1_i,x_pocetno_1_j],['P',x_pocetno_0_i-1,x_pocetno_0_j-1],['P',x_pocetno_1_i-1,x_pocetno_1_j-1],
            ['P',x_pocetno_0_i,x_pocetno_0_j-1],['P',x_pocetno_1_i,x_pocetno_1_j-1]]
        else:
            lista = [['Z',x_pocetno_0_i,x_pocetno_0_j-1],['Z',x_pocetno_1_i,x_pocetno_1_j-1],['P',x_pocetno_0_i-1,x_pocetno_0_j],['P',x_pocetno_1_i-1,x_pocetno_1_j],
            ['P',x_pocetno_0_i,x_pocetno_0_j],['P',x_pocetno_1_i,x_pocetno_1_j]]
        for potezZid in lista:
            if Proveriti_Potez_Zid(igra, [na_potezu,None], potezZid) != False:
                return potezZid

    # if na_potezu == "X":
    #     lista = [['Z',igra[protivnik][0][0],igra[protivnik][0][1]-1],['Z',igra[protivnik][1][0],igra[protivnik][1][1]-1]]
    # else:
    #     lista = [['Z',igra[protivnik][0][0],igra[protivnik][0][1]],['Z',igra[protivnik][1][0],igra[protivnik][1][1]]]
    # for potezZid in lista:
    #     if Proveriti_Potez_Zid(igra, [na_potezu,None], potezZid) != False:
    #         return potezZid

    if odabrano_polje[1] > j:
        red = i
        kolona = j
        boja = "Z"
    elif odabrano_polje[1] < j:
        red = odabrano_polje[0]
        kolona = odabrano_polje[1]
        boja = "Z"
    elif odabrano_polje[0] > i:
        red = i
        kolona = j
        boja = "P"
    else:
        red = odabrano_polje[0]
        kolona = odabrano_polje[1]
        boja = "P"

    return [boja, red, kolona]

def Unos_Poteza(bez_zida):
    print("Odaberite red novog polja figure")
    vrsta = Odabir_Vrste()
    print("Odaberite kolonu novog polja figure")
    kolona = Odabir_Kolone()
    if (bez_zida == True):
        return {"vrsta":vrsta,"kolona":kolona,"boja":0,"vrsta_zid":0,"kolona_zid":0}
    boja = Odabir_Boje_Zida()
    print("Odaberite red novog polja zidica")
    vrsta_zid = Odabir_Vrste()
    print("Odaberite kolonu novog polja zidica")
    kolona_zid = Odabir_Kolone()
    return {"vrsta":vrsta,"kolona":kolona,"boja":boja,"vrsta_zid":vrsta_zid,"kolona_zid":kolona_zid}

def Odabir_Figure():
    figura = 0
    while(figura == 0):
        print("Odaberite figuru 1 ili 2")
        figura = input()
        if (figura != "1" and figura != "2"):
            figura = 0
        figura = int(figura)
    return figura

from prikaz import hex

def Odabir_Vrste():   
    vrsta = 0
    while(vrsta == 0):
        vrsta = input()
        if (vrsta in hex):
            vrsta = hex.index(vrsta) + 1
        else:
            vrsta = 0
            print("Nepostojeci red")
    return vrsta

def Odabir_Kolone():
    kolona = 0
    while(kolona == 0):
        kolona = input()
        if (kolona in hex):
            kolona = hex.index(kolona) + 1
        else:
            kolona = 0
            print("Nepostojeca kolona")
    return kolona

def Odabir_Boje_Zida():
    print("Odaberite tip zida P - plavi ili Z - zeleni")
    boja = 0
    while(boja == 0):
        boja = input()
        if boja != 'P' and boja != "Z" and boja != "p" and boja != "z":
            boja = 0
        else:
            boja = boja.upper()        
    return boja