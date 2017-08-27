try:
    score = input("Enter score: ")
    fsc = float(score)
    if fsc > 1 or fsc < 0:
        print("Bad score")
    elif fsc >= 0.9:
        print('A')
    elif fsc >= 0.8:
        print("B")
    elif fsc >= 0.7:
        print("C")
    elif fsc >= 0.6:
        print("D")
    elif fsc > 0:
        print('F')
except:
    print("Bad score")