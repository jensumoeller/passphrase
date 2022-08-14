# Generator für eine Passphrase variabler Länge auf Basis einer deutschen
# DiceWare Liste

import pandas as pd
import os
import sys
import random

# Einlesen der DiceWare.txt Datei in eine Lise
diceware = pd.read_csv("./diceware_de.csv", dtype={'zahl' : int, 'wort' : str})
diceware.wort = diceware.wort.astype(str)

# Abfragen, wie viele Wörter die Passphrase haben soll
numberOfWords = int(input("Anzahl der Wörter für die Passphrase: "))

# Loop für Anzahl der Wörter
phrase = ""
for i in range(numberOfWords):

    # Erzeugen 5-stellige Würfelzahl
    wuerfelzahl = 0
    for stelle in range(0,5):
        ziffer = random.randint(1,6)
        wuerfelzahl = wuerfelzahl + ziffer * 10 ** stelle

    # Zur Würfelzahl zugehöriges Wort suchen und an Satz anhängen
    wort = diceware.loc[diceware['zahl'] == wuerfelzahl, 'wort']
    phrase = phrase + str(wort) + " "

# Ausgabe des Satzes (der Passphrase)
print(phrase)

