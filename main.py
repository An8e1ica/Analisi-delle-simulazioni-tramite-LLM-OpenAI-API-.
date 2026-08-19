import random
from datetime import datetime
import json
from staffettisti import *
import scipy as sp
from analisi import *
import pandas as pd
import regole


nomi = [
    "anna", "ada", "alberto", "antonio", "barbara", "bianca",
    "bernardo", "boris", "carla", "clelia", "cesare", "cosimo",
    "gioia", "germana", "giorgio", "giacomo", "dora", "dina",
    "davide", "duccio", "elena", "elga", "ermanno", "erik",
    "federica", "fulvia", "fabrizio", "ferdy", "gianfranco", "heidi", "laura", "loretta","luca","gioia "
]

simpatie = {}
def crea_gruppo_staffetta(seed, nomi, n):
    random.seed(seed)
    gruppo = {}

    if n <= len(nomi):
        nomi_scelti = random.sample(nomi, n)
    else:
        nomi_scelti = [random.choice(nomi) for _ in range(n)]

    for chiave, nome in enumerate(nomi_scelti):
        gruppo[chiave] = Staffettista(
            nome,
            random.randint(18, 65),
            random.randint(0, 10),
            random.randint(0, 10)
        )

    return gruppo


def main():
    gruppo = crea_gruppo_staffetta(40, nomi, 30)

    for staffettista in gruppo.values():
        if staffettista.nome == "Fabrizio":
            staffettista.presente = False

    pacco_partenza = Pacco("Partenza", 0, 7)
    pacco_destinazione = Pacco("Destinazione", 8, 5)

    criteri=regole.assegna_criteri(gruppo, seed=10)
    #****************************************************************************************
    G = crea_grafo(gruppo, regole.calcola_peso_caso)

    G.add_node(pacco_destinazione)
    G.add_node(pacco_partenza)
    print("numero nodi",G.number_of_nodes())

    for persona in gruppo.values():
        distanza_partenza = persona.calcola_distanza(pacco_partenza)
        distanza_destinazione = persona.calcola_distanza(pacco_destinazione)

        G.add_edge(pacco_partenza,persona, distanza=distanza_partenza)


        G.add_edge( persona,pacco_destinazione, distanza=distanza_destinazione)

    print("numero archi",G.number_of_edges())
    somme = {}



    p,p_meno, p_piu,calcolato = analizza_percorsi_pacco(G, pacco_partenza,pacco_destinazione)


    stampa_percorsi(calcolato, p, p_meno, p_piu)


    df = crea_dataframe(gruppo)
    df = aggiungi_metriche(df, G, gruppo)
    print(df.head())
    print(df.iloc[:, :6])

    stampa_metriche(df)
    grado_ingresso_pesatoo, grado_uscita_pesatoo=gradi_pesati(G)
    stampa_gradi_pesati(grado_ingresso_pesatoo, grado_uscita_pesatoo)
    sottogruppi = trova_sottogruppi(G, gruppo)
    stampa_sottogruppi(sottogruppi, gruppo)



    #disegna_grafico_oggetti(G, "Staffetta")
    s1=crea_simulazione(df,G,p, p_meno,p_piu, gruppo,calcolato)

    with open("simulazioni/simulazione_022.json", "w", encoding="utf-8") as file:

        json.dump(s1, file, indent=4, ensure_ascii=False)
    print("Json fatto")
    with open ("simulazioni/simulazione_022.json", "r", encoding="utf-8") as file:
        dizionario = json.load(file)
        print(dizionario)


if __name__ == "__main__":
    main()