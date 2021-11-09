#!/bin/python
# Geschrieben 10/2020, Henry Korhonen henryk@ethz.ch, basierend auf Matlabskripten von Martin Willeke. Hinweise, Bemerkungen und Vorschläge bitte an henryk@ethz.ch.

import pandas as pd
import numpy as np
from scipy.stats import t
from math import sqrt

xy = pd.read_table('test-mittelwert.txt', names=['x','y'], sep=r'\s+') # Lesen der Daten, erstellen eines Dataframes. Als Separator kommt hier eine unbestimmte Anzahl Leerschläge in Frage. Andernfalls "sep" anpassen.

y = xy['y'] # Relevante Daten aus dem Dataframe extrahieren. Achtung: "names" in pd.read_table gibt der ersten Spalte den Namen x und der zweiten y. Unbedingt sicherstellen, dass die richtigen Daten extrahiert werden!

N = len(y) # Anzahl Datenpunkte ermitteln.
print(f'Anzahl Datenpunkte: {N}')
N

mwert = y.mean() # Mittelwert aus dem Dataframe y bestimmen.

print(f'Mittelwert: {mwert}')

ystd = np.std(y, ddof=1) # Standardabweichung der EINZELMESSUNG. Achtung: Default ist hier ddof=0! (Der Nenner wird so zu N anstatt zum gewünschten N-1)
# ddof muss auf 2 gesetzt werden, für Parameter für eine lin. Reg.  (ystd wäre dann z.B. die Standardabweichung der Steigung oder des Achsenabschnitts aus einer lin. Reg. )

ystd_mean = ystd/sqrt(N) # Standardabweichung des MITTELWERTES

p = 0.95 #
p100 = p*100
intval = t.interval(p,N-1,mwert, ystd_mean)
# t.interval aus der Library scipy.stats (s. dritte Zeile) macht das, was unten steht bereits elegant in einer Zeile.

tinv = t.ppf((1+p)/2,N-1) # Berechnung des Student-T Faktors
halb = ystd_mean*tinv
# Hier wird die Standardabweichung des MITTELWERTES (s. Messfehlerskript) benutzt!


print(f'Das {p100}-% Vertrauensintervall ist: {intval}')


print(f'Anders ausgedrückt: {mwert} +- {halb}\n==================================')
