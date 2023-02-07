def Napravi_kopiju_stanja(igra):

    nova_igra = dict()
    nova_igra["m"] = igra["m"]
    nova_igra["n"] = igra["n"]

    nova_igra["tabla"] = list()

    for i in range(0, nova_igra["m"]):
        red = list()
        for j in range(0, nova_igra["n"]):
            polje = dict()
            staro_polje = igra["tabla"][i][j]
            polje["i"] = staro_polje["i"]
            polje["j"] = staro_polje["j"]

            polje["igrac"] = staro_polje["igrac"]
            

            polje["zidovi"] = dict()
            polje["zidovi"]["levo"] = staro_polje["zidovi"]["levo"]
            polje["zidovi"]["gore"] = staro_polje["zidovi"]["gore"]
            polje["zidovi"]["desno"] = staro_polje["zidovi"]["desno"]
            polje["zidovi"]["dole"] = staro_polje["zidovi"]["dole"]

            red.append(polje)
        nova_igra["tabla"].append(red)

    nova_igra["x_pocetno"] = ((igra["x_pocetno"][0][0],igra["x_pocetno"][0][1]),(igra["x_pocetno"][1][0],igra["x_pocetno"][1][1]))
    nova_igra["x_trenutno"] = [[igra["x_trenutno"][0][0],igra["x_trenutno"][0][1]],[igra["x_trenutno"][1][0],igra["x_trenutno"][1][1]]]
    nova_igra["ox_pocetno"] = ((igra["ox_pocetno"][0][0],igra["ox_pocetno"][0][1]),(igra["ox_pocetno"][1][0],igra["ox_pocetno"][1][1]))
    nova_igra["ox_trenutno"] = [[igra["ox_trenutno"][0][0],igra["ox_trenutno"][0][1]],[igra["ox_trenutno"][1][0],igra["ox_trenutno"][1][1]]]
    nova_igra["k"] = igra["k"]
    nova_igra["x_zidovi"] = dict()
    nova_igra["x_zidovi"]["plavi"] = igra["x_zidovi"]["plavi"]
    nova_igra["x_zidovi"]["zeleni"] = igra["x_zidovi"]["zeleni"]
    nova_igra["ox_zidovi"] = dict()
    nova_igra["ox_zidovi"]["plavi"] = igra["ox_zidovi"]["plavi"]
    nova_igra["ox_zidovi"]["zeleni"] = igra["ox_zidovi"]["zeleni"]

    nova_igra["izabran"] = igra["izabran"]

    return nova_igra