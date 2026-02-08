leiviskat = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
grammat_yhteensa = round(grammat_yhteensa)
kilot = grammat_yhteensa // 1000
grammat = grammat_yhteensa % 1000
print(f"Massa on {kilot} kilogrammaa ja {grammat} grammaa.")

