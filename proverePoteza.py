# FUNKCIJE ZA PROVERU VALIDNOSTI POTEZA

# funkcija koja ispituje sve sto je potrebno na osnovu izabranog pomeranja figure da odredi da li je validno
def Proveriti_Potez_Pesaka(igra, figura, odabrano_polje, koor_polja_odab = None):

    if figura[0] == "X":
        xoxfigura = "x_trenutno"
        ciljno = "ox_pocetno"
    else:
        xoxfigura = "ox_trenutno"
        ciljno = "x_pocetno"
    if koor_polja_odab == None:
        koordinate_polja_odabrane_figure = igra[xoxfigura][figura[1]]
    else:
        koordinate_polja_odabrane_figure = koor_polja_odab

    if odabrano_polje[0] < 0 or odabrano_polje[0] >= igra["m"]:         # provera da li su vrednosti odabranog polja u granicama table
        return False
    if odabrano_polje[1] < 0 or odabrano_polje[1] >= igra["n"]:
        return False

    if not(odabrano_polje[0] == igra[ciljno][0][0] and odabrano_polje[1] == igra[ciljno][0][1] or odabrano_polje[0] == igra[ciljno][1][0] and odabrano_polje[1] == igra[ciljno][1][1]):
        if (igra["tabla"][odabrano_polje[0]][odabrano_polje[1]]["igrac"] != None):
            return False

    delta_red = odabrano_polje[0] - koordinate_polja_odabrane_figure[0]
    delta_kolona = odabrano_polje[1] - koordinate_polja_odabrane_figure[1]
    pom = delta_kolona * delta_red

    if delta_red == 0:                                                                                                          # slucajevi svih mogucih kretanja
        if delta_kolona == 1 or delta_kolona == -1:
            if odabrano_polje[0] == igra[ciljno][0][0] and odabrano_polje[1] == igra[ciljno][0][1] or odabrano_polje[0] == igra[ciljno][1][0] and odabrano_polje[1] == igra[ciljno][1][1]:
                return Proveriti_prepreku_zid_horizontalno(igra,koordinate_polja_odabrane_figure,odabrano_polje,delta_kolona)
            if igra["tabla"][odabrano_polje[0]][koordinate_polja_odabrane_figure[1]+delta_kolona]["igrac"] == None:
                return False
            return Proveriti_prepreku_zid_horizontalno(igra,koordinate_polja_odabrane_figure,odabrano_polje,delta_kolona)           # horizontalne provere
        if delta_kolona != 2 and delta_kolona != -2:
            return False
        return Proveriti_prepreku_zid_horizontalno(igra,koordinate_polja_odabrane_figure,odabrano_polje,delta_kolona)
    elif delta_kolona == 0:
        if delta_red == 1 or delta_red == -1:
            if odabrano_polje[0] == igra[ciljno][0][0] and odabrano_polje[1] == igra[ciljno][0][1] or odabrano_polje[0] == igra[ciljno][1][0] and odabrano_polje[1] == igra[ciljno][1][1]:
                return Proveriti_prepreku_zid_vertikalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_red)
            if igra["tabla"][koordinate_polja_odabrane_figure[0]+delta_red][odabrano_polje[1]]["igrac"] == None:
                return False
            return Proveriti_prepreku_zid_vertikalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_red)             # vertikalne provere
        if delta_red != 2 and delta_red != -2:
            return False
        return Proveriti_prepreku_zid_vertikalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_red)
    elif pom != -1 and pom != 1:
        return False
    else:
        return Proveriti_prepreku_zid_dijagonalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_kolona, delta_red)  # dijagonalna provera


# funkcija koja proverava da li postoji zid/zidovi izmedju pocetnog i konacnog polja za kretanje horizontalno
def Proveriti_prepreku_zid_horizontalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_kolona):
    if delta_kolona > 0:
        if igra["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["desno"] == True:
            return False
        if igra["tabla"][odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["levo"] == True:
            return False
    else:
        if igra["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["levo"] == True:
            return False
        if igra["tabla"][odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["desno"] == True:
            return False
    return True

# funkcija koja proverava da li postoji zid/zidovi izmedju pocetnog i konacnog polja za kretanje vertikalno
def Proveriti_prepreku_zid_vertikalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_red):
    if delta_red > 0:
        if igra["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["dole"] == True:
            return False
        if igra["tabla"][odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["gore"] == True:
            return False
    else:
        if igra["tabla"][koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["gore"] == True:
            return False
        if igra["tabla"][odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["dole"] == True:
            return False
    return True

# funkcija koja proverava da li postoji prepreka za dijagonalno kretanje (kretanje je moguce ukoliko bi razlozeno na jedan pokret vertikalno i jedan horizontalno bilo moguce)
# primer: gore-desno, moze li se proci desno pa gore za po jedno polje ili gore pa desno
def Proveriti_prepreku_zid_dijagonalno(igra, koordinate_polja_odabrane_figure, odabrano_polje, delta_kolona, delta_red):
    tabla = igra["tabla"]
    if delta_red > 0 and delta_kolona > 0:
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["desno"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["gore"] == False:
            return True
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["dole"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["levo"] == False:
            return True
        return False
    if delta_red < 0 and delta_kolona > 0:
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["desno"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["dole"] == False:
            return True
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["gore"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["levo"] == False:
            return True
        return False
    if delta_red < 0 and delta_kolona < 0:
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["levo"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["dole"] == False:
            return True
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["gore"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["desno"] == False:
            return True
        return False
    if delta_red > 0 and delta_kolona < 0:
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["levo"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["gore"] == False:
            return True
        if tabla[koordinate_polja_odabrane_figure[0]][koordinate_polja_odabrane_figure[1]]["zidovi"]["dole"] == False and tabla[odabrano_polje[0]][odabrano_polje[1]]["zidovi"]["desno"] == False:
            return True
        return False

# funkcija koja proverava da li mesto za zid nije vec zauzeto ili prekinuto drugim zidom
def Proveriti_Potez_Zid(igra, figura, zid):

    if figura[0] == "X":
        xoxfigura = "x_zidovi"
    else:
        xoxfigura = "ox_zidovi"

    if zid[1] < 0 or zid[1] >= igra["m"] - 1:         # provera da li su vrednosti odabranog polja za zid u granicama table
        return False
    if zid[2] < 0 or zid[2] >= igra["n"] - 1:
        return False

    tabla = igra["tabla"]
    if zid[0] == "P":
        if igra[xoxfigura]["plavi"] == 0:
            return False
        if tabla[zid[1]][zid[2]]["zidovi"]["dole"] == True or tabla[zid[1]][zid[2]+1]["zidovi"]["dole"] == True:
            return False
        if tabla[zid[1]][zid[2]]["zidovi"]["desno"] == True and tabla[zid[1]+1][zid[2]]["zidovi"]["desno"] == True:
            return False
    else:
        if igra[xoxfigura]["zeleni"] == 0:
            return False
        if tabla[zid[1]][zid[2]]["zidovi"]["desno"] == True or tabla[zid[1]+1][zid[2]]["zidovi"]["desno"] == True:
            return False
        if tabla[zid[1]][zid[2]]["zidovi"]["dole"] == True and tabla[zid[1]][zid[2]+1]["zidovi"]["dole"] == True:
            return False
    return True


# funkcija koja proverava da li se zatvara put do bilo kog pocetnog polja
def Proveriti_Put(igra):
    tabla = igra["tabla"]
    m = igra["m"]
    n = igra["n"]
    u = Pronadji_Put(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n)
    if u == False:
        return False
    u = u and Pronadji_Put(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n)
    return u

# a star algoritam
def Pronadji_Put(start, cilj, tabla, m, n):
    found_cilj = False        
    open_set = list()  
    open_set.append(start)
    closed_set = list() 
    g = {}                   
    #prev_nodes = {}          
    g[hashable_ime(start)] = 0          
    #prev_nodes[hashable_ime(start)] = None

    while len(open_set) > 0 and (not found_cilj): 
        node = None 
        for next_node in open_set: 
            if node is None or g[hashable_ime(next_node)] + h(next_node,cilj) < g[hashable_ime(node)] + h(node,cilj): 
                node = next_node 
           
        if node == cilj: 
            found_cilj = True 
            break

        for potomak in potomci(node, tabla, m, n): 
            if potomak not in open_set and potomak not in closed_set: 
                open_set.append(potomak) 
                #prev_nodes[hashable_ime(potomak)] = node 
                g[hashable_ime(potomak)] = g[hashable_ime(node)] + 1

        open_set.remove(node) 
        if node not in closed_set:
            closed_set.append(node)

    
    if found_cilj: 
        return True
    else:
        return False


def h(node, cilj):          # heuristika za racunanje rastojanja, racuna koliko polja treba da se pomeri horizontalno plus vertikalno do cilja
    return abs(node["j"] - cilj["j"]) + abs(node["i"] - cilj["i"])

def potomci(node, tabla, m, n):          

    lista = list()

    if (node["j"] - 1 >= 0 and node["zidovi"]["levo"] == False):
        levo = tabla[node["i"]][node["j"] - 1]
        lista.append(levo)

    if (node["j"] + 1 < n and node["zidovi"]["desno"] == False):
        desno = tabla[node["i"]][node["j"] + 1]
        lista.append(desno)
    
    if (node["i"] - 1 >= 0 and node["zidovi"]["gore"] == False):
        gore = tabla[node["i"] - 1][node["j"]]
        lista.append(gore)

    if (node["i"] + 1 < m and node["zidovi"]["dole"] == False):
        dole = tabla[node["i"] + 1][node["j"]]
        lista.append(dole)

    return lista

def hashable_ime(polje):                                 # polje je dictionary, a dictionary nije hashable, ova funkcija pravi jedinstven string
    return str(polje["i"]) + str(polje["j"])