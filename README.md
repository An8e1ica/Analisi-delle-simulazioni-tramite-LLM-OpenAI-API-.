# README

## Obiettivo del progetto
il progetto descrive un gruppo che forma una staffetta, laddove un pacco deve essere portato a destinazione. l'idea è quella di rappresentare 
genericamente un gruppo di lavoro dove il pacco può rappresentare anche una pratica o un servizio, e l'obiettivo è osservare il flusso del lavoro, cambainodo componeneti del gruppo e regole per attribuire preferenze nei passaggi del pacco. 

## Struttura tecnica 
Il progetto è sviluppato in Python e utilizza principalmente NetworkX per la costruzione e l'analisi delle reti, insieme a strutture dati Python e file JSON per la memorizzazione dei risultati.

Il sistema genera gruppi di staffettisti, ciascuno caratterizzato da attributi individuali quali età, coordinate spaziali, titolo di studio, anni di servizio e valori di simpatia verso gli altri partecipanti. Alcune caratteristiche sono generate in modo pseudocasuale mediante seed, così da poter riprodurre gli stessi gruppi in simulazioni differenti.

Ogni simulazione costruisce un grafo diretto e pesato (DiGraph). I nodi rappresentano gli staffettisti, oltre ai nodi artificiali di partenza e destinazione del pacco. Un arco diretto A → B rappresenta la possibilità che A passi il pacco a B; il peso dell'arco esprime invece la maggiore o minore propensione a effettuare quel passaggio.

I pesi vengono determinati attraverso regole di simulazione differenti, basate singolarmente o in combinazione su variabili quali distanza, età, anzianità di servizio, titolo di studio e simpatia personale. Una soglia minima sul peso determina quali relazioni vengono effettivamente inserite nel grafo. In questo modo lo stesso gruppo di individui può generare reti differenti quando cambiano le regole che governano le interazioni.

Per ogni rete vengono successivamente calcolate diverse metriche strutturali e di centralità, tra cui grado entrante e uscente, anche pesato, betweenness e closeness. Vengono inoltre analizzati il numero degli archi, i possibili percorsi tra partenza e destinazione e la loro lunghezza. I sottogruppi della rete vengono individuati attraverso greedy_modularity_communities.

I risultati delle singole simulazioni e delle relative analisi vengono salvati in file JSON, mantenendo separati i dati relativi alla composizione del gruppo, alla simulazione e alle statistiche ottenute. Questa organizzazione permette di riutilizzare gli stessi risultati senza dover eseguire nuovamente le simulazioni.

Una seconda fase del progetto integra un Large Language Model tramite OpenAI API. Per ciascuna simulazione vengono forniti al modello i dati della rete, le metriche calcolate, il significato attribuito alle variabili e un'interpretazione iniziale dell'autrice. Il modello viene utilizzato come livello successivo di interpretazione sociologica e organizzativa e non per produrre le metriche o generare la simulazione.

Le interpretazioni ottenute vengono nuovamente memorizzate in JSON. In una fase finale, i risultati delle diverse simulazioni e le relative interpretazioni vengono forniti congiuntamente al modello per effettuare un confronto trasversale, cercando variazioni associate alla composizione del gruppo, alle regole applicate e alla numerosità dei partecipanti.
## Modello della simulazione
Ogni nodo è un persona dotata di età, anni di servizio, titolo di studio e posizione geografica.   Vi sono tre gruppi diversi e con regole diverse per determinare la propensione a passare il pacco creando una collaborazione, che può essere anche unidirezionale, cioè la preferenza può essere non ricambiata dal collega. 
Il primo gruppo è di 10 persone, il terzo gruppo è di 30 persone e va dalal simulazione 13* a 20°. Il secondo gruppo è sempre di 10 persone ma ho cambiato le loro caratteristiche e corrisponde alla simulazione 2. La 21° simulazione elimina un componente influente er vedere come si riorganizza la rete. 
Le regole per attribuire i pesi agli archi vertono su: distanza tra le persone, il pacco è passato a chi è fisicamente più vicino; età, si passa ai più anziani; anni di servizio: si passa a chi ha maggior anzianità di servizio, titolo di studio: si passa per delegare il lavoro a chi a titolo più basso; simpatia: è un punteggio random che crea una preferenza personale della persona.queste regole sono state combinate in varie maniere dando ora maggior peso a una regola ora all'altra. 
## Interpretazione dei risultati
In ogni simulazione ho commentato i risultati. 
Una regola gerarchica tende a diminuire i percorsi possibili e a creare due poli opposti, costituiti da chi prevalentemente trasmette e chi prevalentemente riceve. 
Con il titolo di studio, ad esempio, i soggetti con qualifiche più elevate tendono a delegare il passaggio a quelli con qualifiche inferiori, producendo una struttura direzionale e relativamente rigida.
Con l'età o gli anni di servizio la direzione si inverte nel significato: sono i soggetti più giovani o meno esperti a rivolgersi a quelli più anziani o con maggiore esperienza, creando una gerarchia basata sulla deferenza e sul riconoscimento dell'esperienza.
Ci sono comunque differenze in quanto, la gerarchia basata sul titolo di studio distingue 4 livelli, quella basata sull'età, praticamente 2: coetaneo o quasi e molto più anziano. 
Introducendo criteri differenti, come la distanza o la simpatia personale, la struttura può invece diventare meno rigidamente polarizzata e aumentano le possibilità di collegamento tra individui. La simpatia, in particolare, mostra come una preferenza personale possa diventare una componente del funzionamento organizzativo quando concorre con le altre regole che determinano i passaggi.

Non emerge tuttavia una struttura che possa essere considerata più efficiente in assoluto. Un numero elevato di archi e percorsi può offrire maggiore flessibilità e alternative, ma può anche generare ridondanza; una rete con pochi collegamenti può invece risultare adeguata a un'attività che richiede una sequenza di passaggi semplice e definita, pur risultando più vulnerabile alla perdita di nodi importanti.

Le simulazioni suggeriscono quindi che regole organizzative, sia esplicite sia implicite, insieme alle preferenze personali, possono contribuire alla formazione di modalità di lavoro differenti. La struttura emergente dipende non soltanto dalle caratteristiche degli individui, ma anche dalle regole secondo cui essi interagiscono.
## Analisi tramite LLM
Dopo una prima analisi delle singole simulazioni, ho utilizzato un Large Language Model (GPT) tramite OpenAI API come ulteriore livello interpretativo.

L'LLM non è stato utilizzato per generare i gruppi, costruire i grafi o calcolare le metriche. Queste operazioni sono state eseguite dal programma in Python. Al modello sono stati invece forniti, attraverso file JSON:

la composizione del gruppo;
la regola utilizzata nella simulazione;
le metriche ottenute dall'analisi della rete;
i sottogruppi individuati;
una descrizione del significato attribuito alle variabili e ai pesi;
il mio commento e la mia interpretazione iniziale dei risultati.

In una prima fase ogni simulazione è stata analizzata separatamente. Il prompt chiedeva al modello di non limitarsi alla descrizione delle metriche, ma di cercare possibili interpretazioni sociologiche e organizzative, distinguendo ciò che era direttamente osservabile nei dati dalle interpretazioni plausibili e dalle ipotesi che avrebbero richiesto ulteriori verifiche.

Le risposte ottenute sono state salvate in ulteriori file JSON.

In una seconda fase sono stati forniti contemporaneamente al modello i risultati delle 21 simulazioni e le rispettive interpretazioni. Lo scopo non era più interpretare il singolo grafo, ma effettuare un confronto trasversale, cercando regolarità e differenze associate alle regole utilizzate, alla composizione e alla numerosità dei gruppi.

L'utilizzo dell'LLM rappresenta quindi una forma di analisi assistita tramite API e prompt engineering, e non un addestramento o fine-tuning del modello.
## Risultati del confronto
Il confronto complessivo ha evidenziato innanzitutto che metriche diverse descrivono aspetti differenti dell'organizzazione della rete e non possono essere ricondotte a un'unica idea di "centralità".

Un individuo che riceve molti passaggi può rappresentare un importante punto di riferimento o di concentrazione del lavoro, senza essere necessariamente un intermediario indispensabile tra parti diverse della rete. Analogamente, un nodo con elevata funzione di ponte può essere strutturalmente importante anche senza essere quello che riceve o distribuisce il maggior numero di passaggi.

È inoltre emerso che l'individuazione di una sola comunità non implica necessariamente una struttura egualitaria. Una rete può essere fortemente gerarchica e allo stesso tempo risultare sufficientemente connessa da essere individuata come un'unica comunità. L'analisi dei sottogruppi deve quindi essere affiancata alle informazioni sulla direzione degli archi e alle altre metriche strutturali.

Un altro risultato interessante riguarda i ruoli emergenti. Lo stesso individuo può assumere una posizione centrale, periferica, di intermediazione, ricezione o diffusione a seconda della regola applicata. Il ruolo osservato nella rete non è quindi necessariamente una proprietà stabile dell'individuo, ma può emergere dall'interazione tra le sue caratteristiche, quelle degli altri partecipanti e le regole che determinano i collegamenti.

Anche l'aumento della numerosità del gruppo non determina automaticamente una maggiore integrazione. Gruppi più numerosi possono produrre reti molto dense, strutture policentriche oppure una forte frammentazione, a seconda dei criteri utilizzati per creare gli archi.

Nel complesso, le simulazioni mostrano soprattutto che la quantità dei collegamenti, considerata isolatamente, non permette di stabilire la qualità del funzionamento di una rete. Molti archi possono significare disponibilità di percorsi alternativi e flessibilità, ma anche ridondanza; pochi archi possono produrre una struttura semplice e funzionale oppure una rete fragile e dipendente da pochi passaggi.
## Conclusioni
La staffetta rappresenta un modello volutamente semplificato di trasferimento di un oggetto tra individui, ma il "pacco" può essere considerato più in generale come un compito, un'informazione, una richiesta, una pratica o una fase di lavorazione che deve attraversare un gruppo.

Le simulazioni suggeriscono che regole organizzative esplicite o implicite e preferenze personali possono concorrere alla formazione di modalità di lavoro differenti.

Regole basate sull'età, sull'anzianità di servizio o sul titolo di studio possono produrre strutture maggiormente gerarchiche e direzionali. Criteri spaziali possono favorire aggregazioni locali, mentre fattori personali come la simpatia possono modificare la distribuzione delle interazioni e concorrere alla formazione della struttura effettiva del gruppo.

La simpatia non rappresenta quindi necessariamente un elemento estraneo all'organizzazione: nel modello diventa una delle possibili leve informali che influenzano la scelta delle interazioni, insieme ai criteri più esplicitamente organizzativi.

Non emerge tuttavia una configurazione che possa essere definita efficiente in assoluto. L'efficienza dipende dal rapporto tra struttura della rete, regole di interazione e funzione che il gruppo deve svolgere. Una rete molto connessa può essere vantaggiosa quando sono necessarie flessibilità e alternative, mentre una struttura più selettiva può risultare adeguata quando il compito richiede una sequenza chiara e poco ambigua di passaggi.

In questo senso, conoscere le regole formali e informali che governano le interazioni può contribuire a rendere più comprensibile e, almeno entro i limiti del modello, più prevedibile la struttura emergente di un gruppo.
## Limiti
Il progetto ha carattere esplorativo e non costituisce un modello empirico del comportamento di gruppi umani reali.

Gli staffettisti sono nodi relativamente semplici, caratterizzati da un numero limitato di attributi. Non possiedono obiettivi individuali complessi, memoria delle interazioni precedenti, capacità di modificare autonomamente le proprie strategie o caratteristiche psicologiche sufficientemente articolate.

Le regole utilizzate sono definite artificialmente e i risultati dipendono necessariamente da tali scelte, dalle soglie utilizzate e dalla composizione dei gruppi simulati. Le simulazioni permettono quindi di osservare cosa accade all'interno del modello costruito, ma non consentono di stabilire relazioni causali generalizzabili alle organizzazioni reali.

Anche i percorsi individuati rappresentano possibilità strutturali di trasferimento, non sequenze di comportamento realmente avvenute. Un numero elevato di percorsi indica quindi che la rete offre molte alternative, ma non dimostra che tali alternative verrebbero effettivamente utilizzate.

I sottogruppi individuati mediante modularità rappresentano zone della rete caratterizzate da una maggiore concentrazione di collegamenti. Non descrivono però da soli la gerarchia, la direzione del lavoro o i rapporti di influenza, che richiedono di essere interpretati insieme alle altre caratteristiche del grafo.

Il modello è inoltre prevalentemente statico: descrive la struttura risultante da determinate regole, ma non studia ancora come reputazione, preferenze, ruoli e relazioni possano modificarsi come conseguenza delle interazioni nel tempo.

Infine, le interpretazioni prodotte dall'LLM 
devono essere considerate ipotesi interpretative assistite, 
non una validazione scientifica dei risultati. Il modello linguistico è stato 
utilizzato per individuare relazioni, confrontare configurazioni e
proporre possibili letture sociologiche dei dati già prodotti dal programma.

## Possibili sviluppi
Un possibile sviluppo consiste nell'introdurre nodi più complessi e dinamici, dotati di un maggior numero di caratteristiche individuali e di comportamenti che possano modificarsi in seguito alle interazioni.

Le relazioni potrebbero evolvere nel tempo: ricevere o completare con successo un compito potrebbe modificare la reputazione di un individuo, precedenti collaborazioni potrebbero aumentare o diminuire la probabilità di interazioni successive e la struttura stessa della rete potrebbe quindi trasformarsi durante la simulazione.

Un numero molto maggiore di simulazioni permetterebbe inoltre di costruire un dataset adatto all'applicazione di tecniche di machine learning, per verificare se, conoscendo le caratteristiche iniziali di un gruppo e le regole di interazione, sia possibile prevedere alcune proprietà della struttura che emergerà.

Un ulteriore sviluppo può riguardare modelli sociali più articolati, nei quali ciascun nodo disponga di caratteristiche individuali, preferenze e possibili comportamenti più complessi. In questo caso l'obiettivo non sarebbe soltanto osservare quale struttura viene prodotta da una determinata regola, ma studiare come una struttura sociale emerga e si trasformi dall'interazione ripetuta tra individui differenti.

Questa ultima parte crea anche un ponte molto naturale con il progetto del gruppo-classe senza mischiare i due: la staffetta rimane il modello semplice in cui riesci ancora a vedere bene regola → rete, mentre l'altro può diventare deliberatamente più complesso.