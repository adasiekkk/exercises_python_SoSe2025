
def steigung_funktion(x1, y1, x2, y2):
    steigung_liste = [x1, y1, x2, y2]
    if x1-x2 == 0:
        print("Die Steigung ist nicht definiert.")
    else: print((steigung_liste[3]-steigung_liste[1])/(steigung_liste[2]-steigung_liste[0]))
    
    
steigung_funktion(1, 1, 1, 1)
steigung_funktion(1, 2, 3, 4)
steigung_funktion(1, 15, 16, 17)