def Da_Li_Je_Kraj(igra):

    tabla = igra["tabla"]

    polozaj_prvo_polje_x = igra["x_pocetno"][0]
    prvo_polje_x = tabla[polozaj_prvo_polje_x[0]][polozaj_prvo_polje_x[1]]
    polozaj_drugo_polje_x = igra["x_pocetno"][1]
    drugo_polje_x = tabla[polozaj_drugo_polje_x[0]][polozaj_drugo_polje_x[1]]

    polozaj_prvo_polje_ox = igra["ox_pocetno"][0]
    prvo_polje_ox = tabla[polozaj_prvo_polje_ox[0]][polozaj_prvo_polje_ox[1]]
    polozaj_drugo_polje_ox = igra["ox_pocetno"][1]
    drugo_polje_ox = tabla[polozaj_drugo_polje_ox[0]][polozaj_drugo_polje_ox[1]]

    if prvo_polje_x["igrac"] == "O" or drugo_polje_x["igrac"] == "O": 
        return (True, "O")
    elif prvo_polje_ox["igrac"] == "X" or drugo_polje_ox["igrac"] == "X":
        return (True, "X")
    else:
        return (False, None)
