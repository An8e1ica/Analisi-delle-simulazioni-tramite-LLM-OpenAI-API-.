import json
from pprint import pprint

nome_file = ("simulazioni/simulazione_021.json")



with open(nome_file, "r", encoding="utf-8") as file:
    simulazione = json.load(file)

print("\n===== CHIAVI PRINCIPALI =====")
print(simulazione.keys())
print
print("\n===== REGOLA =====")
pprint(simulazione["regola"])

print("\n===== METRICHE GLOBALI =====")
pprint(simulazione["metriche_globali"])

print("\n===== PRIMO STAFFETTISTA =====")
pprint(simulazione["staffettisti"][0])

print("\n===== SOTTOGRUPPI =====")
pprint(simulazione["sottogruppi"])
