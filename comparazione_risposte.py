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

Confronta le metriche, il numero di archi e percorsi, la formazione dei sottogruppi
e i cambiamenti nel ruolo strutturale dei partecipanti.

Analizza come cambia il modo di lavorare dei gruppi: per esempio policentrismo,
centralizzazione, gerarchia, rigidità, frammentazione, piccole unità autonome,
intermediazione e distribuzione dei flussi di lavoro.

Cerca soprattutto differenze tra:
- lo stesso gruppo sottoposto a regole diverse;
- gruppi diversi sottoposti a regole uguali o simili;
- simulazioni che modificano il numero o la presenza dei partecipanti.

Non limitarti a riassumere le singole simulazioni: cerca regolarità, differenze
e possibili relazioni tra le caratteristiche della simulazione e la struttura
organizzativa che emerge.

Distingui i risultati osservabili nei dati dalle possibili interpretazioni
sociologiche.
"""
dati_comparazione = {}

for n in range(1, 22):
    dati_comparazione[n] = carica_pacchetto2(pacchetti2[n])

print("inizio analisi")

response = client.responses.create(model="gpt-5.6", input=prompt + "\n\nDATI:\n" + json.dumps(dati_comparazione, ensure_ascii=False))

print(response.usage)

with open("risposte_ai/comparazione_finale.json", "w", encoding="utf-8") as file:
    json.dump({"risposta_ai": response.output_text}, file, ensure_ascii=False, indent=4)

print("SALVATA comparazione finale")
print( response.output_text)