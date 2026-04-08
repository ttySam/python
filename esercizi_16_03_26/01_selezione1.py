
"""Autore: Samuel Nobile
Data: 13/03/2026
Titolo: 
        Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se
        l’importo risulta superiore a 300€ lo sconto è del 10%. 
        Scrivere un programma che richieda
        all'utente l'ammontare della spesa e visualizzi quindi l'importo effettivo da pagare.
"""

# Sezione di input Dati
totale_spesa = float(input("Inserisci il prezzo totale da pagare: "))
# Inizializzazioni variabili
sconto = 0
totale_scontato = 0
# Elaborazione
if totale_spesa > 100:
    sconto = 0.05
elif totale_spesa > 300:
    sconto = 0.1
# Eventuali sotto processi di Elaborazione
totale_scontato = totale_spesa - (totale_spesa * sconto)
# Sezione di output
print(f"Il totale da pagare è {round(totale_scontato, 2)}")