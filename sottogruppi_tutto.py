import staffettisti
import regole
import analisi
import json
import pandas as pd
with open("simulazioni/simulazione_021.json", "r",  encoding="utf-8") as file:
    simulazione = json.load(file)

df = pd.DataFrame(simulazione["staffettisti"])
print(simulazione.keys())
print("REGOLA:")
print(simulazione["regola"]["nome"])
print(simulazione["regola"]["descrizione"])

print("età media:")
print(df["eta"].mean())
print("\n")
print("età, deviazione standard: ")
print(df["eta"].std())
print("anni di servizio media:")
print(df["anni_di_servizio"].mean())
print("\n")
print("anni di servizio std:")
print(df["anni_di_servizio"].std())
print("studio, moda:")
print(df["titolo_studio"].mode())
for numero, sottogruppo in enumerate(
    simulazione["sottogruppi"],
    start=1
):
    df_sotto = df[df["nome"].isin(sottogruppo)]

    print("\nGRUPPO", numero)
    print("Età media:", df_sotto["eta"].mean())
    print("Dev std età:", df_sotto["eta"].std())
    print("Titolo moda:", df_sotto["titolo_studio"].mode().tolist())



def crea_statistiche_globali(df, simulazione):

    sottogruppi_statistiche = []

    for numero, sottogruppo in enumerate(simulazione["sottogruppi"], start=1):
        df_sotto = df[df["nome"].isin(sottogruppo)]

        dati = {
            "numero": numero,
            "numero_componenti": len(df_sotto),

            "eta_media": round(df_sotto["eta"].mean(), 2),
            "eta_std": round(df_sotto["eta"].std(), 2),

            "anni_servizio_media":
                round(df_sotto["anni_di_servizio"].mean(), 2),

            "anni_servizio_std":
                round(df_sotto["anni_di_servizio"].std(), 2),

            "titolo_studio_moda":
                df_sotto["titolo_studio"].mode().tolist()
        }

        sottogruppi_statistiche.append(dati)
    statistiche_simulazione = {
            "gruppo_riferimento": "c",
            "numero_sottogruppi": len(sottogruppi_statistiche),
            "sottogruppi": sottogruppi_statistiche
        }
    return statistiche_simulazione
s3=crea_statistiche_globali(df, simulazione)
with open("statistiche/sim021.json", "w", encoding="utf-8") as file:
    json.dump(s3, file, indent=4, ensure_ascii=False)
print("Json fatto")
