import math
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime
from regole import calcola_peso_caso
from staffettisti import *
#grafo con staffettisti e due pacchi. elimino archi con peso inferiore a 2
def crea_grafo(gruppo, regola):
    G = nx.DiGraph()
    persone = [persona for persona in gruppo.values()
        if persona.presente]

    G.add_nodes_from(persone)
    for persona1 in persone:
        for persona2 in persone:

            if persona1 == persona2:
                continue

            peso = regola(persona1, persona2)

            distanza = persona1.calcola_distanza(persona2)

            if peso > 2:
                G.add_edge(persona1, persona2, peso=peso, distanza =distanza)



    return G

def crea_dataframe(gruppo):
    righe = []

    for chiave, persona in gruppo.items():
        riga = vars(persona).copy()
        riga["id"] = chiave
        righe.append(riga)

    return pd.DataFrame(righe).set_index("id")

def disegna_grafico_oggetti(G, titolo):
    pos = {
        nodo: nodo.posizione
        for nodo in G.nodes()
    }

    labels = {
        nodo: nodo.nome
        for nodo in G.nodes()
    }

    etichette_pesi = {
        (nodo1, nodo2): round(dati["peso"], 2)
        for nodo1, nodo2, dati in G.edges(data=True)
        if "peso" in dati
    }

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        ax=ax,
        labels=labels,
        with_labels=True,
        node_size=1800,
        font_size=9,
        arrows=True
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        ax=ax,
        edge_labels=etichette_pesi,
        font_size=8,
        rotate=False
    )

    ax.set_title(titolo)
    ax.axis("off")
    fig.tight_layout()
    plt.show()
#G = nx.DiGraph()


def aggiungi_metriche(df, G, gruppo):
    in_degree = dict(G.in_degree())
    out_degree = dict(G.out_degree())
    in_degree_pesato = dict(G.in_degree(weight="peso"))
    out_degree_pesato = dict(G.out_degree(weight="peso"))

    centralita_entrata = nx.in_degree_centrality(G)
    centralita_uscita = nx.out_degree_centrality(G)
    betweenness = nx.betweenness_centrality(G, weight="peso")
    closeness = nx.closeness_centrality(G)

    try:
        eigen = nx.eigenvector_centrality(
            G,
            weight="peso",
            max_iter=1000,
            tol=1e-5
        )

    except nx.PowerIterationFailedConvergence:
        print(
            "\nEigenvector centrality non calcolabile: "
            "l'algoritmo non ha raggiunto la convergenza."
        )
        eigen = {}
    try:
        pagerank = nx.pagerank(
            G,
            weight="peso",
            max_iter=1000
        )

    except nx.PowerIterationFailedConvergence:
        print("\nPageRank non calcolabile.")
        pagerank = {}


    for chiave, persona in gruppo.items():
        df.loc[chiave, "in_degree"] = in_degree.get(persona, 0)
        df.loc[chiave, "out_degree"] = out_degree.get(persona, 0)
        df.loc[chiave, "in_degree_pesato"] = in_degree_pesato.get(persona, 0)
        df.loc[chiave, "out_degree_pesato"] = out_degree_pesato.get(persona, 0)
        df.loc[chiave, "centralita_entrata"] = centralita_entrata.get(persona, 0)
        df.loc[chiave, "centralita_uscita"] = centralita_uscita.get(persona, 0)
        df.loc[chiave, "betweenness"] = betweenness.get(persona, 0)
        df.loc[chiave, "eigen"] = eigen.get(persona, 0)
        df.loc[chiave, "closeness"] = closeness.get(persona, 0)
        df.loc[chiave, "pagerank"] = pagerank.get(persona, 0)

    return df

# Somma dei pesi degli archi entranti
def stampa_metriche(df):
    metriche = [
        "in_degree",
        "out_degree",
        "grado_ingresso_pesato",
        "grado_uscita_pesato",
        "centralita_entrata",
        "centralita_uscita",
        "betweenness",
        "closeness",
        "eigen",
        "pagerank"
    ]

    print("\n*********** SINTESI METRICHE ***********\n")

    for metrica in metriche:

        if metrica not in df.columns:
            continue

        indice_max = df[metrica].idxmax()
        indice_min = df[metrica].idxmin()

        print(f"{metrica}:")
        print(
            "  massimo:",
            df.loc[indice_max, "nome"],
            round(df.loc[indice_max, metrica], 3)
        )
        print(
            "  minimo :",
            df.loc[indice_min, "nome"],
            round(df.loc[indice_min, metrica], 3)
        )
        print()

def gradi_pesati(G):
    grado_ingresso_pesato = dict(G.in_degree(weight="peso")    )
    grado_ingresso_pesatoo = sorted(
        grado_ingresso_pesato.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Somma dei pesi degli archi uscenti
    grado_uscita_pesato = dict(G.out_degree(weight="peso"))
    grado_uscita_pesatoo = sorted(
        grado_uscita_pesato.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return grado_ingresso_pesatoo, grado_uscita_pesatoo
def distanza_media(nodo, gruppo):
    distanza_totale = 0
    numero_distanze = 0

    for altro_nodo in gruppo.values():

        if altro_nodo != nodo:
            distanza = nodo.calcola_distanza(altro_nodo)
            distanza_totale = distanza_totale + distanza
            numero_distanze = numero_distanze + 1

    if numero_distanze == 0:
        return 0

    distanza_media = distanza_totale / numero_distanze

    return distanza_media
def distanza_media_archi(G):
    distanza_totale = 0
    numero_archi = 0

    for nodo1, nodo2 in G.edges():
        distanza_totale = distanza_totale + nodo1.calcola_distanza(nodo2)
        numero_archi = numero_archi + 1

    if numero_archi == 0:
        return 0
    media_archi=distanza_totale / numero_archi
    return media_archi

def stampa_gradi_pesati(grado_ingresso_pesatoo, grado_uscita_pesatoo):
    print("\nGRADO DI INGRESSO PESATO")
    for persona, valore in grado_ingresso_pesatoo:
        print(persona.nome, round(valore, 2))

    print("\nGRADO DI USCITA PESATO")
    for persona, valore in grado_uscita_pesatoo:
        print(persona.nome,  round(valore, 2))
#pos= nx.spring_layout(G, seed=42, k=3,iterations=100)

#print("\n*************************************CAMMINI**********************************************\n")
def analizza_percorsi_pacco(G, pacco_partenza, pacco_destinazione):
    if G.number_of_edges()>45:
        percorsi = []
        percorso_meno_passaggi = None
        percorso_piu_passaggi = None

        calcolato=False
        return (
            percorsi,
            percorso_meno_passaggi,
            percorso_piu_passaggi,
            calcolato
        )
    if not nx.has_path(G, pacco_partenza, pacco_destinazione):
        print("Il pacco non può raggiungere la destinazione.")
        return []

    percorsi = list(
        nx.all_simple_paths(
            G,
            source=pacco_partenza,
            target=pacco_destinazione
        )
    )
    percorso_meno_passaggi = min(percorsi, key=len)
    percorso_piu_passaggi = max(percorsi, key=len)
    calcolato=True

    return percorsi, percorso_meno_passaggi, percorso_piu_passaggi,calcolato
def stampa_percorsi(calcolato,percorsi, percorso_meno_passaggi, percorso_piu_passaggi, modalita="sintesi"):
    if not calcolato:
        print("Percorsi non calcolati: numero di archi troppo elevato.")
        return
    if not percorsi:
        print("Nessun percorso da stampare.")
        return
    print("Numero di percorsi possibili:", len(percorsi))
    if not percorsi:
        print("Nessun percorso da stampare.")
        return

    print("Numero di percorsi:", len(percorsi))

    if modalita == "tutti":

        for numero, percorso in enumerate(percorsi, start=1):

            print(f"\nPercorso {numero}")

            for nodo in percorso:
                print(nodo.nome, end=" -> ")

            print("Fine")
            print("Passaggi:", len(percorso) - 1)

    print("\nPercorso con meno passaggi:")

    for nodo in percorso_meno_passaggi:
        print(nodo.nome, end=" -> ")

    print("Fine")
    print("Passaggi:", len(percorso_meno_passaggi) - 1)

    print("\nPercorso con più passaggi:")

    for nodo in percorso_piu_passaggi:
        print(nodo.nome, end=" -> ")

    print("Fine")
    print("Passaggi:", len(percorso_piu_passaggi) - 1)
#percorso_piu_breve = nx.shortest_path(
   # G,
    #source=pacco_partenza,
    #target=pacco_destinazione,
    #weight="distanza")

#distanza_piu_breve = nx.shortest_path_length(
    #G,    source=pacco_partenza,    target=pacco_destinazione,    weight="distanza")

def trova_sottogruppi(G, gruppo):
    GU = nx.Graph()

    # Associa ogni oggetto alla sua chiave numerica
    oggetto_id = {}

    for chiave, persona in gruppo.items():
        oggetto_id[persona] = chiave
        GU.add_node(chiave, nome=persona.nome)

    persone = list(gruppo.values())

    for i in range(len(persone)):
        for j in range(i + 1, len(persone)):
            persona1 = persone[i]
            persona2 = persone[j]

            peso_1_2 = 0
            peso_2_1 = 0

            if G.has_edge(persona1, persona2):
                peso_1_2 = G[persona1][persona2].get("peso", 0)

            if G.has_edge(persona2, persona1):
                peso_2_1 = G[persona2][persona1].get("peso", 0)

            peso_totale = peso_1_2 + peso_2_1

            if peso_totale > 0:
                GU.add_edge(
                    oggetto_id[persona1],
                    oggetto_id[persona2],
                    peso=peso_totale
                )

    comunita = nx.community.greedy_modularity_communities(GU, weight="peso")

    return comunita

def stampa_sottogruppi(sottogruppi, gruppo):
    print("\n******** SOTTOGRUPPI ********")

    for numero, sottogruppo in enumerate(sottogruppi, start=1):
        print("\nGruppo", numero)

        for chiave in sottogruppo:
            print(gruppo[chiave].nome)

def scrivi_e_leggi(nome_file, messaggio):
    print(messaggio)
    print(f"Apri il file: testi/{nome_file}")
    input("Premi INVIO quando hai finito...")
    with open(f"testi/{nome_file}", "r", encoding="utf-8") as file:
        testo = file.read()

    with open(f"testi/{nome_file}", "w", encoding="utf-8") as file:
        file.write("")

    return testo
def crea_simulazione(df, G,  percorsi, percorso_meno_passaggi, percorso_piu_passaggi,gruppo, calcolato):
    nome_regola = input("Nome della regola: ")
    descrizione = input(" descivi la regola e simulazione:  ")
    commento=scrivi_e_leggi("commenti.txt","Scrivi il commento in commento.txt e premi INVIO...")
    interpretazione=scrivi_e_leggi("interpretazioni.txt","Scrivi l'interpretazione in interpretazione.txt e premi INVIO...")


    sottogruppi = trova_sottogruppi(G, gruppo)

    sottogruppi_json = []

    for sottogruppo in sottogruppi:
        nomi = []

        for chiave in sottogruppo:
            nomi.append(gruppo[chiave].nome)

        sottogruppi_json.append(nomi)


    simulazione = {
        "regola": {
            "nome": nome_regola,
            "descrizione": descrizione
        },

        "staffettisti": df.to_dict(orient="records"),

        "percorsi": {
    "numero_totale": len(percorsi) if calcolato else None,

    "percorso_meno_passaggi":
        [nodo.nome for nodo in percorso_meno_passaggi] if calcolato else None,

    "numero_passaggi_minimo":
        len(percorso_meno_passaggi) - 1 if calcolato else None,

    "percorso_piu_passaggi":
        [nodo.nome for nodo in percorso_piu_passaggi] if calcolato else None,

    "numero_passaggi_massimo":
        len(percorso_piu_passaggi) - 1 if calcolato else None
},

        "sottogruppi": sottogruppi_json,

        "metriche_globali": {
            "distanza_media_archi": distanza_media_archi(G),
            "numero_nodi": G.number_of_nodes(),
            "numero_archi": G.number_of_edges()
        },


        "commento": commento,
        "interpretazione":interpretazione
    }

    return simulazione