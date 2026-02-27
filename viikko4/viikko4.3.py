pienin = None
suurin = None
while True:
    syote = input("Anna luku (Enter lopettaa): ")
    if syote == "":
        break
    luku = float(syote)
    if pienin is None:
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
print("Pienin luku:" , pienin)
print("Suurin luku:" , suurin)















