def cagr_berechnung(AK,EK,t):
    cagr=((EK/abs(AK))**(1/abs(t)))-1
    return(cagr)


cagr=cagr_berechnung(100, 700, 30)

print(120 * (1+cagr)**30)
