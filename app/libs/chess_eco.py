def map_chess_eco(eco):
    """
    Returning opening name

    :param eco: string
    :type eco: string
    :return: string
    :rtype: string
    """
    eco = str(eco)
    opening_name = ""
    if eco[0] == "A":
        if eco[1:3] == "00":
            opening_name = "Polish (Sokolsky) opening"
        if eco[1:3] == "01":
            opening_name = "Nimzovich-Larsen attack"
        if int(eco[1:3]) in list(range(2,3):
            opening_name = "Bird's opening"
        if int(eco[1:3]) in list(range(4,9):
            opening_name = "Reti opening"
        if int(eco[1:3]) in list(range(10,39):
            opening_name = "English opening"
        if int(eco[1:3]) in list(range(40,41):
            opening_name = "Queen's opening"
    else:
        opening_name = "Horde's opening"
    return opening_name

print(map_chess_eco(eco="A04"))
print(list(range(2,5)))

