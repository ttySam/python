"""
Autore: Samuel Nobile
Data: 20/03/2026
Titolo: 
        Conversione temperatura: implementare una funzione converti CF che converta una
        temperatura espressa in gradi Fahrenheit in una temperatura espressa in gradi Celsius.

        Usare la seguente formula:
        C = (F - 32) * 5 / 9
        Creare un programma principale che richiami la funzione e ne stampi il risultato visualizzando solo 3 cifre decimali.
"""

##
## Funzioni: def converti_fahrenheit()
##


temperatura = float(input("Inserisci una temperatura in Fahrenheit in formato 0.0: "))

def converti_fahrenheit(temperatura: float) -> str:

    """
    Funzione: converti fahrenheit in celsius
    float temperatura -> temperatura in fahrenheit
    Valore di ritorno:
    str -> restituzione somma e prodotto
    """
    
    celsius = round(((temperatura - 32) * (5 / 9)), 2)

    return str(temperatura) + "°F corrisponde a " + str(celsius) + " °C"

# Sezione di input Dati

# Inizializzazioni variabili
# Elaborazione
print(converti_fahrenheit(temperatura))
# Eventuali sotto processi di Elaborazione
# Sezione di output