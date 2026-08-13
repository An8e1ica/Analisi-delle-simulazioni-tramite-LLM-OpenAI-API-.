import json

informazioni_ai = {
    "tipo_grafo": "DiGraph diretto e pesato",

    "significato_arco":
        "Un arco A -> B indica che A può passare il pacco a B. il grafo rappresenta un gruppo di lavoro che porta il pacco da partenza  destinazione, gli archi pesati rappresentano maggiore o minore propensione  che avvenga il paggio ",

     "significato_peso":
        "Il peso dell'arco rappresenta quanto A preferisce passare "
        "il pacco a B. Il modo in cui viene calcolato dipende dalla "
        "regola della simulazione.",

    "coordinate":
        "x e y rappresentano la posizione spaziale dello staffettista.",
    "distanza": "considerando le coordinate si calcolano le distanze tra nodi e pacchi"
              "in alcune simulazioni influisce sul peso ed è un criterio razionale di passaggio"
                "la distanza è inversamente proporzionale al peso, più l'altro nodo è distanza meno si è propensi a apssargli il pacco",
    "simpatia":"Valore generato casualmente  al peso per distribuire preferenze personali come può esserlo appunto una simpatia"
                "tra gli staffettisti. È direzionale: la simpatia di A verso B può essere diversa dalla simpatia di B verso A."
                "Un alto peso indica propensione a passare, è un criterio irrazionale e soggettivo",
 "pacco_ partenza e pacco_destinazione":"Partenza e Destinazione sono nodi artificiali e non staffettisti. "
                                         "Sono Oggetti generati dalla classe Pacco, "
                    "dotato solo di nome e coordinate come parametri, rappresentano il punto di partenza dei passaggi "
                     "degli staffettisti e "
         "quello finale",
    "titolo di studio": "ci sono vari livelli dal più alto al più basso(laurea magistrale, laurea triennale, superiori, medie),"
                        "i più titolati passano ai meno istruiti per delegare il lavoro di manovalanza"
    "rappresentando una divisione gerarchica o operativa del lavoro" ,

"età": "i più giovani, con età inferiore passano ai più anziani, in questo caso più per rispetto della loro esperienza "      
        "quando i più giovani passano ai più anziani è per rispetto o deferenza"
       "rappresentando una divisione gerarchica o operativa del lavoro",

"anni di servizio" :  "altro peso che indica da quanti anni lo staffettista lavora. Non corrisponde per forza all'età, "
                        " lo staffettista può essere anziano e appena assunto. Come per l'età coloro con meno anni di servizio quando passano "
                            "a chi ha più anni di servizio lo fa per deferenza e fiducia nell'esperienza",
"percorsi":
"Il numero di percorsi è il numero di cammini semplici possibili "
"da Partenza a Destinazione, passando per gli archi pesati.",

"sottogruppi":
"I sottogruppi sono comunità individuate automaticamente nel grafo."
     "cioè insiemi di nodi che risultano più fortemente collegati tra loro "
    "rispetto al resto della rete.",

"metodo per identificare sottogruppi":
"Algoritmo greedy_modularity_communities.",

"numero_archi":
"Numero di passaggi diretti A -> B consentiti dalla rete. "
"Indica il numero di collegamenti diretti presenti nel grafo; "
"non va confuso con il numero dei percorsi possibili.",

"numero_percorsi":
"Numero di sequenze complete possibili da Partenza a Destinazione; "
"non coincide con il numero degli archi.",

"regola e descrizione della regola":
"Ogni regola decide come calcolare i pesi in base a simpatia, distanza, età, "
"titolo di studio e anni di servizio. "
"La descrizione spiega in che modo li combina e privilegia",
"ruoli_emergenti":
    "I ruoli di diffusore, ricevitore, ponte o nodo centrale non sono assegnati in anticipo: "
    "emergono dalla struttura della rete e dalle metriche di centralità.",
"gradi_pesati":
    "Il grado semplice indica quanti collegamenti ha un nodo; "
    "il grado pesato tiene conto anche dell'intensità delle preferenze associate a quei collegamenti.",
}


with open("simulazioni/informazioni_ai.json", "w", encoding="utf-8") as file:
    json.dump( informazioni_ai, file,    ensure_ascii=False,   indent=4 )

print("Creato informazioni_ai.json")