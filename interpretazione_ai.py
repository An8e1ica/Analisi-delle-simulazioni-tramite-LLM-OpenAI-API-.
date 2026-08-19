import os
import json
from openai import OpenAI
from pacchetti_ai import pacchetti, carica_pacchetto

client = OpenAI()
if os.getenv("OPENAI_API_KEY"):
    print("Chiave trovata")
else:
    print("Chiave NON trovata")


prompt = """
Analizza la simulazione non limitandoti a descrivere le metriche del grafo.

Usa:
- le informazioni sul significato sociale attribuito alle variabili e ai pesi;
- la regola specifica della simulazione;
- le metriche di rete;
- i sottogruppi individuati;
- il commento e l'interpretazione dell'autrice.

Cerca di formulare una possibile interpretazione sociologica e organizzativa
del gruppo simulato.

Nell'interpretazione sociologica distingui i diversi ruoli che possono
emergere dalla struttura della rete.

Per esempio, valuta se i dati suggeriscono:
- un ruolo operativo o di coordinamento, legato alla quantità e intensità
  dei collegamenti;
- un ruolo di ponte o intermediazione, legato alla posizione tra parti
  diverse della rete;
- un ruolo di riferimento, quando un nodo tende a ricevere molti passaggi;
- un ruolo di diffusione o delega, quando tende a distribuirli verso molti altri;
- forme di centralità organizzativa quando più indicatori convergono.

Puoi formulare interpretazioni sociologiche ulteriori quando sono
ragionevolmente sostenute dalla struttura osservata, spiegando da quali
elementi del grafo derivano.

Il commento e l'interpretazione dell'autrice servono come guida al tipo
di ragionamento desiderato, ma non devono essere semplicemente confermati:
correggili quando i dati li contraddicono e sviluppa interpretazioni ulteriori.

Distingui chiaramente:
1. ciò che è direttamente osservabile nei dati;
2. l'interpretazione sociologica plausibile;
3. le ipotesi che richiederebbero ulteriori simulazioni o dati per essere verificate.
"""
for n in range(1, 23):
    dati_ai = carica_pacchetto(pacchetti[n])
    response = client.responses.create(model="gpt-5.6",  input=prompt + "\n\nDATI:\n" + json.dumps( dati_ai, ensure_ascii=False)
)
    print("inizio analisi")
    #print(response.output_text)
    #print("\nUSO:")
    #print(response.usage)
    with open(
        f"risposte_ai/risposta{n:03d}.json",
        "w",
        encoding="utf-8") as file:

        json.dump({"simulazione": n,"risposta_ai": response.output_text },  file,  ensure_ascii=False, indent=4)

    print(f"SALVATA simulazione {n}")