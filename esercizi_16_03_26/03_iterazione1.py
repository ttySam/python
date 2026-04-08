"""
Autore: Samuel Nobile
Data: 13/03/2026
Titolo: 
        Leggere una successione di numeri interi passati dall’utente, fermandosi al primo numero
        che rende la successione non crescente e restituendo quanti numeri formano la
        successione inserita.

        Esempio:
        INPUT: 2 5 28 10 OUTPUT: 3
        INPUT: 2 -2 OUTPUT: 1
"""

# Sezione di input Dati
numeri = map(int,input("Inserisci dei numeri separati da spazio ").split())
# Inizializzazioni variabili
contatore = 0
somma = 0
# Elaborazione
for num in numeri:
    if (somma + num) > somma:
        somma+=num
        contatore+=1
    else:
        break
# Eventuali sotto processi di Elaborazione
# Sezione di output
print("Ci sono ", contatore, "numeri in sequenza")
