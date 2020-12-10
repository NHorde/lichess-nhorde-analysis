def map_chess_eco(eco):
    """
    Returning opening name base on ECO number

    :param eco: string
    :type eco: string
    :return: string
    :rtype: string
    """
    eco = str(eco)
    opening_name = "Horde's opening"
    if eco[0] == "A":
        if eco[1:3] == "00":
            opening_name = "Polish (Sokolsky) opening"
        if eco[1:3] == "01":
            opening_name = "Nimzovich-Larsen attack"
        if int(eco[1:3]) in list(range(2,4)):
            opening_name = "Bird's opening"
        if int(eco[1:3]) in list(range(4,10)):
            opening_name = "Reti opening"
        if int(eco[1:3]) in list(range(10,40)):
            opening_name = "English opening"
        if int(eco[1:3]) in list(range(40,42)):
            opening_name = "Queen's opening"
        if eco[1:3] == "42":
            opening_name = "Modern defence, Averbakh system"
        if int(eco[1:3]) in list(range(43,45)):
            opening_name = "Old Benoni Defence"
        if int(eco[1:3]) in list(range(45,47)):
            opening_name = "Queen's pawn game"
        if eco[1:3] == "47":
            opening_name = "Queen's Indian defence"
        if int(eco[1:3]) in list(range(48, 50)):
            opening_name = "King's Indian, East Indian defence"
        if eco[1:3] == "50":
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(51, 53)):
            opening_name = "Budapest defence"
        if int(eco[1:3]) in list(range(53, 56)):
            opening_name = "Old Indian defence"
        if eco[1:3] == "56":
            opening_name = "Benoni defence"
        if int(eco[1:3]) in list(range(57, 60)):
            opening_name = "Benko gambit"
        if int(eco[1:3]) in list(range(60, 80)):
            opening_name = "Benoni defence"
        if int(eco[1:3]) in list(range(80, 100)):
            opening_name = "Dutch"
    elif eco[0] == "B":
        if int(eco[1:3]) in list(range(0, 1)):
            opening_name = "King's pawn opening"
        if int(eco[1:3]) in list(range(1, 2)):
            opening_name = "Scandinavian (centre counter) defence"
        if int(eco[1:3]) in list(range(2, 6)):
            opening_name = "Alekhine's defence"
        if int(eco[1:3]) in list(range(6, 7)):
            opening_name = "Robatsch (modern) defence"
        if int(eco[1:3]) in list(range(7, 10)):
            opening_name = "Pirc defence"
        if int(eco[1:3]) in list(range(10, 20)):
            opening_name = "Caro-Kahn defence"
        if int(eco[1:3]) in list(range(20, 100)):
            opening_name = "Sicilian defence"
    elif eco[0] == "C":
        if int(eco[1:3]) in list(range(0, 20)):
            opening_name = "French defence"
        if int(eco[1:3]) in list(range(20, 21)):
            opening_name = "King's pawn game"
        if int(eco[1:3]) in list(range(21, 23)):
            opening_name = "Centre game"
        if int(eco[1:3]) in list(range(23, 25)):
            opening_name = "Bishop's opening"
        if int(eco[1:3]) in list(range(25, 30)):
            opening_name = "Vienna game"
        if int(eco[1:3]) in list(range(30, 40)):
            opening_name = "King's gambit"
        if int(eco[1:3]) in list(range(40, 41)):
            opening_name = "King's knight opening"
        if int(eco[1:3]) in list(range(41, 42)):
            opening_name = "Philidor's defence"
        if int(eco[1:3]) in list(range(42, 44)):
            opening_name = "Petrov's defence"
        if int(eco[1:3]) in list(range(44, 45)):
            opening_name = "King's pawn game"
        if int(eco[1:3]) in list(range(45, 46)):
            opening_name = "Scotch game"
        if int(eco[1:3]) in list(range(46, 47)):
            opening_name = "Three knights game"
        if int(eco[1:3]) in list(range(47, 50)):
            opening_name = "Four knights, Scotch variation"
        if int(eco[1:3]) in list(range(50, 51)):
            opening_name = "King's pawn game"
        if int(eco[1:3]) in list(range(51, 53)):
            opening_name = "Evans gambit"
        if int(eco[1:3]) in list(range(53, 55)):
            opening_name = "Giuoco Piano"
        if int(eco[1:3]) in list(range(55, 60)):
            opening_name = "Two knights defence"
        if int(eco[1:3]) in list(range(60, 100)):
            opening_name = "Ruy Lopez (Spanish opening)"
    elif eco[0] == "D":
        if int(eco[1:3]) in list(range(0, 1)):
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(1, 2)):
            opening_name = "Richter-Veresov attack"
        if int(eco[1:3]) in list(range(2, 3)):
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(3, 4)):
            opening_name = "Torre attack (Tartakower variation)"
        if int(eco[1:3]) in list(range(4, 6)):
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(6, 7)):
            opening_name = "Queen's gambit"
        if int(eco[1:3]) in list(range(7, 10)):
            opening_name = "Queen's Gambit Declined, Chigorin defence"
        if int(eco[1:3]) in list(range(10, 16)):
            opening_name = "Queen's Gambit Declined Slav defence"
        if int(eco[1:3]) in list(range(16, 17)):
            opening_name = "Queen's Gambit Slav accepted, Alapin variation"
        if int(eco[1:3]) in list(range(17, 20)):
            opening_name = "Queen's Gambit Declined Slav, Czech defence"
        if int(eco[1:3]) in list(range(20, 30)):
            opening_name = "Queen's gambit accepted"
        if int(eco[1:3]) in list(range(30, 43)):
            opening_name = "Queen's gambit declined"
        if int(eco[1:3]) in list(range(43, 50)):
            opening_name = "EQueen's Gambit Declined semi-Slav"
        if int(eco[1:3]) in list(range(50, 70)):
            opening_name = "Queen's Gambit Declined, 4.Bg5"
        if int(eco[1:3]) in list(range(70, 80)):
            opening_name = "Neo-Gruenfeld defence"
        if int(eco[1:3]) in list(range(80, 100)):
            opening_name = "Gruenfeld defence"
    elif eco[0] == "E":
        if int(eco[1:3]) in list(range(0, 1)):
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(1, 10)):
            opening_name = "Catalan, closed"
        if int(eco[1:3]) in list(range(10, 11)):
            opening_name = "Queen's pawn game"
        if int(eco[1:3]) in list(range(11, 12)):
            opening_name = "Bogo-Indian defence"
        if int(eco[1:3]) in list(range(12, 20)):
            opening_name = "Queen's Indian defence"
        if int(eco[1:3]) in list(range(20, 60)):
            opening_name = "Nimzo-Indian defence"
        if int(eco[1:3]) in list(range(60, 100)):
            opening_name = "King's Indian defence"
    return opening_name

def check_eco_missing():
    for letter in ["A", "B", "C", "D", "E"]:
        for i in range(0,100):
            if map_chess_eco(eco=f"{letter}{format(i, '02d')}") == "Horde's opening":
                print(f"Missing eco: {letter}{format(i, '02d')}")

# check_eco_missing()