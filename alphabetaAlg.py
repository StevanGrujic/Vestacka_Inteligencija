from potez import Postavi_Prvi_Validan_Zid, Vrati_Moguca_Nova_Stanja, Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove
from kraj import Da_Li_Je_Kraj
from proverePoteza import Proveriti_Potez_Pesaka
from stanje import Napravi_kopiju_stanja


def max_value(stanje, dubina, alpha, beta):
    if dubina == 0 or Da_Li_Je_Kraj(stanje)[0]:
        return [stanje, proceni_stanje_slozena(stanje)]                        #proceni_stanje_malo_slozenija(stanje)]
    else:
        i = 0
        for s in Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove(stanje,"X"):        
            v = min_value(Napravi_kopiju_stanja(s), dubina - 1, Kopija_Alpha_Beta(alpha), Kopija_Alpha_Beta(beta))
            if i == 0:
                alpha[0] = s
                rezerva = v[1]
                i += 1
            if v[1] >= alpha[1]:
                alpha[1] = v[1]
                alpha[0] = s
                rezerva = v[1]
            if alpha[1] > beta[1]:
                return alpha
    return [alpha[0],rezerva]

def min_value(stanje, dubina, alpha, beta):
    if dubina == 0 or Da_Li_Je_Kraj(stanje)[0]:
        return [stanje, proceni_stanje_slozena(stanje)]                            #proceni_stanje_malo_slozenija(stanje)]
    else:
        i = 0
        for s in Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove(stanje,"O"):
            v = max_value(Napravi_kopiju_stanja(s), dubina - 1, Kopija_Alpha_Beta(alpha), Kopija_Alpha_Beta(beta))
            if i == 0:
                beta[0] = s
                rezerva = v[1]
                i += 1
            if v[1] <= beta[1]:
                beta[1] = v[1]
                beta[0] = s
                rezerva = v[1]
            if beta[1] < alpha[1]:
                return beta
    return [beta[0],rezerva]

from potez import Postavi_Prvi_Validan_Zid

def alphabeta(igra, dubina, na_potezu, alpha = (None, -10), beta = (None, 10)):
    stanje = Napravi_kopiju_stanja(igra)
    alpha = [stanje, -10]
    beta = [stanje, 10]
    # stanje["x_zidovi"] = {"plavi" : 0, "zeleni" : 0}
    # stanje["ox_zidovi"] = {"plavi" : 0, "zeleni" : 0}
    if na_potezu == "X":
        v = max_value(stanje, dubina, Kopija_Alpha_Beta(alpha), Kopija_Alpha_Beta(beta))
        # v[0]["x_zidovi"] = {"plavi" : igra["x_zidovi"]["plavi"], "zeleni" : igra["x_zidovi"]["zeleni"]}
        # v[0]["ox_zidovi"] = {"plavi" : igra["ox_zidovi"]["plavi"], "zeleni" : igra["x_zidovi"]["zeleni"]}
        # return Postavi_Prvi_Validan_Zid(v[0],"X")
        
# OVDE MORA AKO JE VREDNOST MANJA ILI JEDNAKA 0 HEURISTIKA DA BI IGRAO NA POBEDU
        vprim = list()
        vprim.append(None)
        if v[1] <= 0 or v[1] == 10:     # jer kad je u prednosti i pobedjuje u 3. potezu uzme da pobedi u 3. potezu a ne u prvom
            vprim = igraj_na_pobedu_x(Napravi_kopiju_stanja(stanje))
            if v[1] == 10 and vprim[1] != 10:
                vprim[0] = v[0]
        else:
            vprim[0] = v[0]

        return vprim[0]
    else:
        v = min_value(stanje, dubina, Kopija_Alpha_Beta(alpha), Kopija_Alpha_Beta(beta))
        # v[0]["x_zidovi"] = {"plavi" : igra["x_zidovi"]["plavi"], "zeleni" : igra["x_zidovi"]["zeleni"]}
        # v[0]["ox_zidovi"] = {"plavi" : igra["ox_zidovi"]["plavi"], "zeleni" : igra["x_zidovi"]["zeleni"]}
        # return Postavi_Prvi_Validan_Zid(v[0],"O")
        vprim = list()
        vprim.append(None)
        if v[1] >= 0 or v[1] == -10:
            vprim = igraj_na_pobedu_ox(Napravi_kopiju_stanja(stanje))
            if v[1] == -10 and vprim[1] != -10:
                vprim[0] = v[0]
        else:
            vprim[0] = v[0]

        return vprim[0]

def proceni_stanje_prosto(stanje):
    if Da_Li_Je_Kraj(stanje)[1] == "X":
        return 10
    if Da_Li_Je_Kraj(stanje)[1] == "O":
        return -10
    return 0

def proceni_stanje_malo_slozenija(stanje):
    if Da_Li_Je_Kraj(stanje)[1] == "X":
        return 10
    if Da_Li_Je_Kraj(stanje)[1] == "O":
        return -10
    x_trenutno_0_i = stanje["x_trenutno"][0][0]
    x_trenutno_0_j = stanje["x_trenutno"][0][1]
    x_trenutno_1_i = stanje["x_trenutno"][1][0]
    x_trenutno_1_j = stanje["x_trenutno"][1][1]
    x_pocetno_0_i = stanje["x_pocetno"][0][0]
    x_pocetno_0_j = stanje["x_pocetno"][0][1]
    x_pocetno_1_i = stanje["x_pocetno"][1][0]
    x_pocetno_1_j = stanje["x_pocetno"][1][1]
    ox_trenutno_0_i = stanje["ox_trenutno"][0][0]
    ox_trenutno_0_j = stanje["ox_trenutno"][0][1]
    ox_trenutno_1_i = stanje["ox_trenutno"][1][0]
    ox_trenutno_1_j = stanje["ox_trenutno"][1][1]
    ox_pocetno_0_i = stanje["ox_pocetno"][0][0]
    ox_pocetno_0_j = stanje["ox_pocetno"][0][1]
    ox_pocetno_1_i = stanje["ox_pocetno"][1][0]
    ox_pocetno_1_j = stanje["ox_pocetno"][1][1]
    x_vrednost = min(abs_razlika(x_trenutno_0_i,x_trenutno_0_j,ox_pocetno_0_i,ox_pocetno_0_j), abs_razlika(x_trenutno_0_i,x_trenutno_0_j,ox_pocetno_1_i,ox_pocetno_1_j),
        abs_razlika(x_trenutno_1_i,x_trenutno_1_j,ox_pocetno_0_i,ox_pocetno_0_j), abs_razlika(x_trenutno_1_i,x_trenutno_1_j,ox_pocetno_1_i,ox_pocetno_1_j))
    ox_vrednost = min(abs_razlika(ox_trenutno_0_i,ox_trenutno_0_j,x_pocetno_0_i,x_pocetno_0_j), abs_razlika(ox_trenutno_0_i,ox_trenutno_0_j,x_pocetno_1_i,x_pocetno_1_j),
        abs_razlika(ox_trenutno_1_i,ox_trenutno_1_j,x_pocetno_0_i,x_pocetno_0_j), abs_razlika(ox_trenutno_1_i,ox_trenutno_1_j,x_pocetno_1_i,x_pocetno_1_j))
    max = stanje["m"] + stanje["n"]
    heuristika = (1-float(x_vrednost)/max)*10+(1-float(ox_vrednost)/max)*(-10)

    return heuristika



def abs_razlika(red0,kolona0,red1,kolona1):
    return abs(kolona1 - kolona0) + abs(red1 - red0)


def Kopija_Alpha_Beta(lista):
    novo = list()
    novo.append(Napravi_kopiju_stanja(lista[0]))
    novo.append(lista[1])
    return novo



def igraj_na_pobedu_x(stanje):
    v = list()
    v.append(stanje)
    v.append(-11)
    for s in Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove(stanje,"X"):
        ocena = proceni_stanje_slozena(s)             #proceni_stanje_malo_slozenija_na_pobedu_x(s)
        if v[1] <= ocena:
            v[0] = s
            v[1] = ocena

    return v

def igraj_na_pobedu_ox(stanje):
    v = list()
    v.append(stanje)
    v.append(11)
    for s in Vrati_Moguca_Nova_Stanja_Sa_Heuristikom_Za_Zidove(stanje,"O"):
        ocena = proceni_stanje_slozena(s)                            #proceni_stanje_malo_slozenija_na_pobedu_ox(s)
        if v[1] >= ocena:
            v[0] = s
            v[1] = ocena

    return v

def proceni_stanje_malo_slozenija_na_pobedu_x(stanje):
    if Da_Li_Je_Kraj(stanje)[1] == "X":
        return 10
    x_trenutno_0_i = stanje["x_trenutno"][0][0]
    x_trenutno_0_j = stanje["x_trenutno"][0][1]
    x_trenutno_1_i = stanje["x_trenutno"][1][0]
    x_trenutno_1_j = stanje["x_trenutno"][1][1]
    ox_pocetno_0_i = stanje["ox_pocetno"][0][0]
    ox_pocetno_0_j = stanje["ox_pocetno"][0][1]
    ox_pocetno_1_i = stanje["ox_pocetno"][1][0]
    ox_pocetno_1_j = stanje["ox_pocetno"][1][1]
    x_vrednost = min(abs_razlika(x_trenutno_0_i,x_trenutno_0_j,ox_pocetno_0_i,ox_pocetno_0_j), abs_razlika(x_trenutno_0_i,x_trenutno_0_j,ox_pocetno_1_i,ox_pocetno_1_j),
        abs_razlika(x_trenutno_1_i,x_trenutno_1_j,ox_pocetno_0_i,ox_pocetno_0_j), abs_razlika(x_trenutno_1_i,x_trenutno_1_j,ox_pocetno_1_i,ox_pocetno_1_j))
    max = stanje["m"] + stanje["n"]
    heuristika = (1-float(x_vrednost)/max)*10
    return heuristika

def proceni_stanje_malo_slozenija_na_pobedu_ox(stanje):
    if Da_Li_Je_Kraj(stanje)[1] == "O":
        return 10
    ox_trenutno_0_i = stanje["ox_trenutno"][0][0]
    ox_trenutno_0_j = stanje["ox_trenutno"][0][1]
    ox_trenutno_1_i = stanje["ox_trenutno"][1][0]
    ox_trenutno_1_j = stanje["ox_trenutno"][1][1]
    x_pocetno_0_i = stanje["x_pocetno"][0][0]
    x_pocetno_0_j = stanje["x_pocetno"][0][1]
    x_pocetno_1_i = stanje["x_pocetno"][1][0]
    x_pocetno_1_j = stanje["x_pocetno"][1][1]
    ox_vrednost = min(abs_razlika(ox_trenutno_0_i,ox_trenutno_0_j,x_pocetno_0_i,x_pocetno_0_j), abs_razlika(ox_trenutno_0_i,ox_trenutno_0_j,x_pocetno_1_i,x_pocetno_1_j),
        abs_razlika(ox_trenutno_1_i,ox_trenutno_1_j,x_pocetno_0_i,x_pocetno_0_j), abs_razlika(ox_trenutno_1_i,ox_trenutno_1_j,x_pocetno_1_i,x_pocetno_1_j))
    max = stanje["m"] + stanje["n"]
    heuristika = (1-float(ox_vrednost)/max)*(-10)
    return heuristika



def proceni_stanje_slozena(igra):

    tabla = igra["tabla"]
    m = igra["m"]
    n = igra["n"]
    x_vrednost = Pronadji_Put_Duzina(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n, igra, "X")
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10

    ox_vrednost = Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n, igra, "O")
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10

    max = m*n
    heuristika = (1-float(x_vrednost)/max)*10+(1-float(ox_vrednost)/max)*(-10)
    return heuristika


def proceni_stanje_slozena_na_pobedu_x(igra):

    tabla = igra["tabla"]
    m = igra["m"]
    n = igra["n"]
    x_vrednost = Pronadji_Put_Duzina(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n, igra, "X")
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][0][0]][igra["ox_pocetno"][0][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][0][0]][igra["x_trenutno"][0][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10
    x_vrednost = min(x_vrednost, Pronadji_Put_Duzina(tabla[igra["x_trenutno"][1][0]][igra["x_trenutno"][1][1]], tabla[igra["ox_pocetno"][1][0]][igra["ox_pocetno"][1][1]], tabla, m, n, igra, "X"))
    if x_vrednost == 0:
        return 10

    max = m*n
    heuristika = (1-float(x_vrednost)/max)*10
    return heuristika


def proceni_stanje_slozena_na_pobedu_ox(igra):

    tabla = igra["tabla"]
    m = igra["m"]
    n = igra["n"]

    ox_vrednost = Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n, igra, "O")
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][0][0]][igra["x_pocetno"][0][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][0][0]][igra["ox_trenutno"][0][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10
    ox_vrednost = min(ox_vrednost, Pronadji_Put_Duzina(tabla[igra["ox_trenutno"][1][0]][igra["ox_trenutno"][1][1]], tabla[igra["x_pocetno"][1][0]][igra["x_pocetno"][1][1]], tabla, m, n, igra, "O"))
    if ox_vrednost == 0:
        return -10

    max = m*n
    heuristika = (1-float(ox_vrednost)/max)*(-10)
    return heuristika



# a star algoritam za heuristiku
def Pronadji_Put_Duzina(start, cilj, tabla, m, n, igra, na_potezu):
    start = [start["i"], start["j"]]
    cilj = [cilj["i"], cilj["j"]]
    found_cilj = False        
    open_set = list()  
    open_set.append(start)
    closed_set = list() 
    g = {}                            
    g[hashable_ime_polje(start)] = 0          

    while len(open_set) > 0 and (not found_cilj): 
        node = None 
        for next_node in open_set: 
            if node is None or g[hashable_ime_polje(next_node)] + he(next_node,cilj) < g[hashable_ime_polje(node)] + he(node,cilj): 
                node = next_node 
           
        if node == cilj: 
            found_cilj = True 
            break

        for potomak in potomci_moguca_polja(node, tabla, m, n, igra, na_potezu): 
            if potomak not in open_set and potomak not in closed_set: 
                open_set.append(potomak) 
                g[hashable_ime_polje(potomak)] = g[hashable_ime_polje(node)] + 1

        open_set.remove(node) 
        if node not in closed_set:
            closed_set.append(node)

    
    if found_cilj: 
        return g[hashable_ime_polje(node)]
    else:
        return False


def he(node, cilj):          # heuristika za racunanje rastojanja, racuna koliko polja treba da se pomeri horizontalno plus vertikalno do cilja
    return abs(node[1] - cilj[1]) + abs(node[0] - cilj[0])

def potomci_moguca_polja(node, tabla, m, n, igra, na_potezu):          

    lista = list()


    i = node[0]
    j = node[1]
    polja = [[i-2,j],[i-1,j],[i+1,j],[i+2,j],[i,j-2],[i,j-1],[i,j+1],[i,j+2],[i+1,j+1],[i-1,j+1],[i+1,j-1],[i-1,j-1]]
    for polje in polja:
        if Proveriti_Potez_Pesaka(igra, [na_potezu, -1], polje, node):
            lista.append(polje)

    return lista

def hashable_ime_polje(polje):                                 
    return str(polje[0]) + str(polje[1])