import os
import json
from openai import OpenAI
print("prima import pacchetti")
from comparazione_pacchetti_ai import pacchetti2, carica_pacchetto2
print("dopo import pacchetti")
client = OpenAI()
if os.getenv("OPENAI_API_KEY"):
    print("Chiave trovata")
else:
    print("Chiave NON trovata")


prompt = """
Confronta nel loro insieme tutte le simulazioni e le interpretazioni precedenti.

Individua quali cambiamenti nella struttura della rete sembrano dipendere da:
- composizione del gruppo;
- regola applicata;
- numero di partecipanti;
- presenza o assenza di nodi particolarmente centrali.



Analizza come cambia il modo di lavorare dei gruppi: per esempio policentrismo,
centralizzazione, gerarchia, rigidità, frammentazione, piccole unità autonome,
intermediazione e distribuzione dei flussi di lavoro.

Cerca pattern nelle differenze tra le simulazioni e individua possibili relazioni
tra le regole applicate, le caratteristiche del gruppo e le strutture organizzative
che emergono.

Dai priorità ai confronti che mostrano:
- effetti diversi prodotti da regole diverse sullo stesso gruppo;
- effetti della stessa regola su gruppi di diversa composizione o dimensione;
- cambiamenti nel ruolo strutturale dei nodi al variare della regola;
- relazioni tra densità della rete, centralizzazione, intermediazione,
  formazione di sottogruppi e distribuzione dei flussi.
Confronta in particolare le simulazioni 001 e 022, nelle quali la stessa
regola basata sulla simpatia viene applicata rispettivamente a un gruppo
di 10 e a un gruppo di 30 partecipanti, per individuare eventuali effetti
associati alla dimensione del gruppo.
Distingui i pattern direttamente osservabili nei dati dalle loro possibili
interpretazioni sociologiche e organizzative.
"""
dati_comparazione = {}

for n in range(1, 23):
    dati_comparazione[n] = carica_pacchetto2(pacchetti2[n])

print("inizio analisi")

response = client.responses.create(model="gpt-5.6", input=prompt + "\n\nDATI:\n" + json.dumps(dati_comparazione, ensure_ascii=False))

print(response.usage)

with open("risposte_ai/comparazione_finale.json", "w", encoding="utf-8") as file:
    json.dump({"risposta_ai": response.output_text}, file, ensure_ascii=False, indent=4)

print("SALVATA comparazione finale")
print( response.output_text)