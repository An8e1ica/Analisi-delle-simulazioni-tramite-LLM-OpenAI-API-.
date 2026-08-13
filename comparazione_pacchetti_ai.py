
import json
import os
simulazioni = [
    "simulazioni/simulazione_001.json",
    "simulazioni/simulazione_002.json",
    "simulazioni/simulazione_003.json",
    "simulazioni/simulazione_004.json",
    "simulazioni/simulazione_005.json",
    "simulazioni/simulazione_006.json",
    "simulazioni/simulazione_007.json",
    "simulazioni/simulazione_008.json",
    "simulazioni/simulazione_009.json",
    "simulazioni/simulazione_010.json",
    "simulazioni/simulazione_011.json",
    "simulazioni/simulazione_012.json",
    "simulazioni/simulazione_013.json",
    "simulazioni/simulazione_014.json",
    "simulazioni/simulazione_015.json",
    "simulazioni/simulazione_016.json",
    "simulazioni/simulazione_017.json",
    "simulazioni/simulazione_018.json",
    "simulazioni/simulazione_019.json",
    "simulazioni/simulazione_020.json",
    "simulazioni/simulazione_021.json"
]
risposte=["risposte_ai/risposta001.json",

"risposte_ai/risposta002.json",
"risposte_ai/risposta003.json",
"risposte_ai/risposta004.json",
"risposte_ai/risposta005.json",
"risposte_ai/risposta006.json",
"risposte_ai/risposta007.json",
"risposte_ai/risposta008.json",
"risposte_ai/risposta009.json",
"risposte_ai/risposta010.json",
"risposte_ai/risposta011.json",
"risposte_ai/risposta012.json",
"risposte_ai/risposta013.json",
"risposte_ai/risposta014.json",
"risposte_ai/risposta015.json",
"risposte_ai/risposta016.json",
"risposte_ai/risposta017.json",
"risposte_ai/risposta018.json",
"risposte_ai/risposta019.json",
"risposte_ai/risposta020.json",
"risposte_ai/risposta021.json"
]
gruppi = [
   "statistiche/gruppoA.json",
    "statistiche/gruppoB.json",
    "statistiche/gruppoC.json"]
statistiche = [
    "statistiche/sim001.json",
    "statistiche/sim002.json",
    "statistiche/sim003.json",
    "statistiche/sim004.json",
    "statistiche/sim005.json",
    "statistiche/sim006.json",
    "statistiche/sim007.json",
    "statistiche/sim008.json",
    "statistiche/sim009.json",
    "statistiche/sim010.json",
    "statistiche/sim011.json",
    "statistiche/sim012.json",
    "statistiche/sim013.json",
    "statistiche/sim014.json",
    "statistiche/sim015.json",
    "statistiche/sim016.json",
    "statistiche/sim017.json",
    "statistiche/sim018.json",
    "statistiche/sim019.json",
    "statistiche/sim020.json",
    "statistiche/sim021.json"
]
informazioni="simulazioni/informazioni_ai.json"
pacchetti2={}


def carica_pacchetto2(pacchetto):
    with open(pacchetto["gruppo_base"], "r", encoding="utf-8") as file:
        gruppo = json.load(file)

    with open(pacchetto["simulazione"], "r", encoding="utf-8") as file:
        simulazione = json.load(file)

    with open(pacchetto["statistiche_simulazione"], "r", encoding="utf-8") as file:
        statistiche = json.load(file)

    with open("simulazioni/informazioni_ai.json", "r", encoding="utf-8") as file:
        informazioni = json.load(file)

    with open(pacchetto["risposta_ai"], "r", encoding="utf-8") as file:
        risposta = json.load(file)

    return {
        "informazioni": informazioni,
        "gruppo_base": gruppo,
        "simulazione": simulazione,
        "statistiche_simulazione": statistiche,
        "risposta_ai": risposta
    }
for i in range(21):

    if i == 1:                 # simulazione 002
        gruppo = gruppi[1]

    elif 12 <= i < 20:         # simulazioni 013-020
        gruppo = gruppi[2]

    else:                      # 001, 003-012, 021
        gruppo = gruppi[0]

    pacchetti2[i+1] = {
        "gruppo_base": gruppo,
        "simulazione": simulazioni[i],
        "statistiche_simulazione": statistiche[i],
        "risposta_ai": risposte[i]
    }
#print(pacchetti.keys())
#print(pacchetti)
for numero, pacchetto in pacchetti2.items():
    for tipo, percorso in pacchetto.items():
        if not os.path.exists(percorso):
            print("NON TROVATO:", numero, tipo, percorso)



