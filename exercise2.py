
def teilbar_funktion(x,y):
    if y==0:
        print("Es ist nicht möglich durch 0 zu teilen")
    elif x==y:
        print("X und Z sind gleich")
    else:
        if x%y==0:
            print("X ist durch Y teilbar")
        else:
            print("X ist durch Y nicht teilbar")
            
            
teilbar_funktion(5, 3)
teilbar_funktion(6, 3)
teilbar_funktion(3, 3)
teilbar_funktion(5, 0)