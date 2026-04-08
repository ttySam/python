"""
Autore: Samuel Nobile
Data: 20/03/2026
Titolo: 
        Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la
        restituisca espressa solamente in secondi. 
        
        Successivamente creare un programma principale che chieda in input due quantità di tempo 
        e stampi in output quale quantità di tempo è maggiore.

        La funzione deve avere i parametri formali con valori predefiniti
"""

##
## Funzioni: def converti_ore()
##

def converti_ore(ore: int, minuti: int, secondi: int) -> str:

    """
    Funzione: converti_ore 
    int ore -> ore in formato hh
    int minuti -> minuti in formato mm
    int secondi -> secondi in formato ss
    Valore di ritorno:
    str -> restituzione secondi
    """
    secondi_totali= (ore * 3600) + (minuti * 60) + secondi
    return "Il totale è " + str(secondi_totali) + " secondi"

# Sezione di input Dati
while True:
    ore, minuti, secondi = map(int, input("Inserisci un orario in formato 'hh:mm:ss': ").split(":"))
    if ore > 23 or minuti > 59 or secondi > 59:
        print("Inserisci un formato valido")
    else:
        break
# Inizializzazioni variabili
# Elaborazione

print(converti_ore(ore,minuti,secondi))
# Eventuali sotto processi di Elaborazione
# Sezione di output