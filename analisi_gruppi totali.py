import staffettisti
import regole
import analisi
import json
import pandas as pd
with open("simulazioni/simulazione_013.json", "r",  encoding="utf-8") as file:
    simulazione = json.load(file)


df = pd.DataFrame(simulazione["staffettisti"])
print(simulazione.keys())
print("REGOLA:")
print(simulazione["regola"]["nome"])
print(simulazione["regola"]["descrizione"])





def crea_statistiche_gruppo(df, simulazione):

    statistiche_gruppo = {
        "numero_staffettisti": len(df),

        "numero_nodi":
            simulazione["metriche_globali"]["numero_nodi"],

        "eta_media":
            round(df["eta"].mean(), 2),

        "eta_std":
            round(df["eta"].std(), 2),

        "eta_min":
            int(df["eta"].min()),

        "eta_max":
            int(df["eta"].max()),

        "anni_servizio_media":
            round(df["anni_di_servizio"].mean(), 2),

        "anni_servizio_std":
            round(df["anni_di_servizio"].std(), 2),

        "titolo_studio_moda":
            df["titolo_studio"].mode().tolist(),


        "titoli_studio_frequenze":
            df["titolo_studio"].value_counts().to_dict()
    }

    return statistiche_gruppo

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
s2=crea_statistiche_gruppo(df,simulazione)
with open("statistiche/gruppoC.json", "w", encoding="utf-8") as file:

     json.dump(s2, file, indent=4, ensure_ascii=False)
print("Json fatto")