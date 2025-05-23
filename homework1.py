import plotly.express as px
from plotly.offline import plot
import pandas as pd

def spar_funktion(AK, SR, i, lz):
    kapital=AK
    sparen=AK
    zinsen=0
    
    gesamt_kapital=[]
    gesamt_zinsen = []
    gesamt_einzahlungen = []
    
    for k in range (1, lz+1):
        zinsen=zinsen + i * kapital
        sparen = sparen + SR
        kapital = kapital * (1+i) + SR
        gesamt_kapital.append(round(kapital,2))
        gesamt_zinsen.append(round(zinsen, 2))
        gesamt_einzahlungen.append(round(sparen,2))
        
    return[gesamt_kapital, gesamt_einzahlungen, gesamt_zinsen]

ergebnisse=