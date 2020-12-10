def map_chess_eco(eco):
    """
    Returning opening name base on ECO number

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
        if int(eco[1:3]) in list(range(2,3)):
            opening_name = "Bird's opening"
        if int(eco[1:3]) in list(range(4,9)):
            opening_name = "Reti opening"
        if int(eco[1:3]) in list(range(10,39)):
            opening_name = "English opening"
        if int(eco[1:3]) in list(range(40,41)):
            opening_name = "Queen's opening"
        if eco[1:3] == "42":
            opening_name = "Modern defence, Averbakh system"
        if int(eco[1:3]) in list(range(43,44)):
            opening_name = "Old Benoni Defence"
        if int(eco[1:3]) in list(range(45,46)):
            opening_name = "Queen's pawn game"
        if eco[1:3] == "47":
            opening_name = "Queen's Indian defence"
        if int(eco[1:3]) in list(range(48, 49)):
            opening_name = "King's Indian, East Indian defence"
        if eco[1:3] == "50":
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(51, 52)):
            opening_name = "Budapest defence"
        if int(eco[1:3]) in list(range(53, 55)):
            opening_name = "Old Indian defence"
        if eco[1:3] == "56":
            opening_name = "Benoni defence"
        if int(eco[1:3]) in list(range(57, 59)):
            opening_name = "Benko gambit"
        if int(eco[1:3]) in list(range(60, 79)):
            opening_name = "Benoni defence"
        if int(eco[1:3]) in list(range(80, 99)):
            opening_name = "Dutch"
    else:
        opening_name = "Horde's opening"
    return opening_name

print(map_chess_eco(eco="A34"))


