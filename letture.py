import json
from pprint import pprint
from pacchetti_ai import pacchetti
from comparazione_pacchetti_ai import pacchetti2, carica_pacchetto2
nome_file = ("simulazioni/simulazione_001.json")
nf=("risposte_ai/risposta003.json")


with open(nf, "r", encoding="utf-8") as file:
    risposta1 = json.load(file)

print("risposta",risposta1)
with open(nome_file, "r", encoding="utf-8") as file:
    simulazione = json.load(file)


print("\n===== CHIAVI PRINCIPALI =====")
print(simulazione.keys())

print("\n===== REGOLA =====")
pprint(simulazione["regola"])

print("\n===== METRICHE GLOBALI =====")
pprint(simulazione["metriche_globali"])

print("\n===== PRIMO STAFFETTISTA =====")
pprint(simulazione["staffettisti"][0])

print("\n===== SOTTOGRUPPI =====")
pprint(simulazione["sottogruppi"])
print(simulazione)

print("test",pacchetti2[22])
print(pacchetti2[21])
print("simm22: ")
with open("statistiche/sim022.json", "r", encoding="utf-8") as f:
    s22 = json.load(f)

print(json.dumps(s22, ensure_ascii=False, indent=2))
#d22 = carica_pacchetto2(pacchetti2[22])

#print("d22, regola",d22["simulazione"]["regola"])
#print(len(d22["simulazione"]["staffettisti"]))
#print(d22["simulazione"]["metriche_globali"])
#print(d22["statistiche_simulazione"]["numero_sottogruppi"])
