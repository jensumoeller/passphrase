# Generator für eine Passphrase variabler Länge auf Basis einer deutschen
# DiceWare Liste, Selektion erfolgt über Random Funktion

import pandas as pd
import os
import sys
import random

# Einlesen der DiceWare.txt Datei in eine Lise
diceware = pd.read_csv("./diceware_de.csv", dtype={'zahl' : int, 'wort' : str})

# Abfragen, wie viele Wörter die Passphrase haben soll
numberOfWords = int(input("\n Anzahl der Wörter für die Passphrase: "))

# Loop für Anzahl der Wörter
phrase = ""
for i in range(numberOfWords):

    # Wort per Zufallsfunktion aus der Spalte 'wort' der Tabelle diceware lesen
    wort = random.choice(diceware.wort)
    # Anhängen des wortes an die Phrase
    phrase = phrase + str(wort) + " "

# Ausgabe des Satzes (der Passphrase)
print('\n', phrase, '\n')

