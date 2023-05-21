# Generator für eine Passphrase variabler Länge auf Basis einer deutschen
# DiceWare Liste, Selektion erfolgt über Random Funktion

import pandas as pd
import os
import sys
import random

# Einlesen der DiceWare.txt Datei in eine Liste
diceware = pd.read_csv("./diceware_en2.csv", dtype={'zahl' : int, 'wort' : str})

# Loop für Abfragewiederholung

while True:

    # Abfragen, wie viele Wörter die Passphrase haben soll
    numberOfWords = int(input(" Anzahl der Wörter für die Passphrase: "))
    
    # Loop für Anzahl der Wörter
    phrase = ""
    for i in range(numberOfWords):
    
        # Wort per Zufallsfunktion aus der Spalte 'wort' der Tabelle diceware lesen
        wort = random.choice(diceware.wort)
        # Anhängen des wortes an die Phrase
        phrase = phrase + str(wort) + " "

    # Ausgabe des Satzes (der Passphrase)
    print('\n', phrase, '\n')

    # Abfrage, ob weitere Passphrase generiert werden soll
    while True:
        jaNein = str(input(" Neue Abfrage (j/n)?"))
        if jaNein in ['j', 'J', 'n', 'N']:
            break
    if jaNein in ['n', 'N']:
        break

