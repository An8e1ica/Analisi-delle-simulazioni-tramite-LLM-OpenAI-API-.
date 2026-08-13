import random
from staffettisti import Staffettista

def simpatia (persona1,persona2):
    simpatia = random.randint(1, 10)
    return type(simpatia)

def calcola_peso_caso(persona1, persona2):
   simpatia= random.randint(1,10)

   return simpatia
def calcola_peso_distanza(persona1,persona2):

    d= persona1.calcola_distanza(persona2)
    peso= 10 / (1 + d)
    return peso
def calcola_peso_amici_distanza(persona1, persona2):
   simpatia= random.randint(1,10)

   d = persona1.calcola_distanza(persona2)
   peso=0.8*d+0.2*simpatia
   return peso

def calcola_peso_amici_distanza2(persona1, persona2):
   simpatia= random.randint(1,10)

   d = persona1.calcola_distanza(persona2)
   peso=0.8*simpatia+0.2*d
   return peso
def calcola_peso_anni_servizio_simpatia(persona1, persona2):
    simpatia = random.randint(1, 10)

    e1=persona1.eta
    e2=persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta=e2-e1
    if dif_eta>20:
        e=10
    elif dif_eta>10:
        e=7
    elif dif_eta<0:
        e=0
    else:
      e=1
    dif_serv = serv2-serv1
    if dif_serv > 20:
        s = 10
    elif dif_serv > 10:
        s = 7
    elif dif_serv < 0:
        s = 0
    else:
        s = 1

    peso=0.6*e+0.2*s+0.2*simpatia
    return peso

def calcola_peso_servizio_anni_simpatia(persona1, persona2):
    simpatia = random.randint(1, 10)

    e1=persona1.eta
    e2=persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta=e2-e1
    if dif_eta>20:
        e=10
    elif dif_eta>10:
        e=7
    elif dif_eta<0:
        e=0
    else:
      e=1
    dif_serv = serv2-serv1
    if dif_serv > 20:
        s = 10
    elif dif_serv > 10:
        s = 7
    elif dif_serv < 0:
        s = 0
    else:
        s = 1

    peso=0.2*e+0.6*s+0.2*simpatia
    return peso

def calcola_peso_simpatia_servizio_anni(persona1, persona2):
    simpatia = random.randint(1, 10)
    #print(type(simpatia), "tipo")
    e1=persona1.eta
    e2=persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta=e2-e1
    if dif_eta>20:
        e=10
    elif dif_eta>10:
        e=7
    elif dif_eta<0:
        e=0
    else:
      e=1
    dif_serv = serv2-serv1
    if dif_serv > 20:
        s = 10
    elif dif_serv > 10:
        s = 7
    elif dif_serv < 0:
        s = 0
    else:
        s = 1

    peso=0.2*e+0.2*s+0.6*simpatia
    return peso
def assegna_criteri(gruppo, seed=10):
    persone = list(gruppo.values())

    random.seed(seed)
    random.shuffle(persone)

    criteri = {}

    for persona in persone[:3]:
        criteri[persona] = "simpatia"

    for persona in persone[3:6]:
        criteri[persona] = "distanza"

    for persona in persone[6:9]:
        criteri[persona] = "eta"

    criteri[persone[9]]="distanza"


    return criteri


def calcola_peso_personalizzato(persona1, persona2, criteri):
    criterio = criteri[persona1]

    simpatia = random.randint(1, 10)

    # print(type(simpatia), "tipo")
    e1 = persona1.eta
    e2 = persona2.eta
    dif_eta=e2-e1
    if dif_eta>20:
        e=10
    elif dif_eta>10:
        e=7
    elif dif_eta<0:
        e=0
    else:
      e=1

    d = persona1.calcola_distanza(persona2)
    dist = 10 / (1 + d)
    #preferenze=[dist, s, simpatia]
    if criterio == "simpatia":
        return simpatia



    elif criterio == "eta":
        return e

    else:
        return dist

def calcola_peso_studio(persona1, persona2):
    livelli = {"licenza media": 1,"diploma": 2, "laurea triennale": 3, "laurea magistrale": 4 }
    livello1 = livelli[persona1.titolo_studio]
    livello2 = livelli[persona2.titolo_studio]
    d=livello1-livello2
    if d==3:
        peso=10
    elif d==2:
        peso =7
    elif d==1:
        peso=5
    elif d==0:
        peso=0
    else:
        peso=-1
    return peso






def calcola_peso_studio_eta(persona1, persona2):
    livelli = {"licenza media": 1,"diploma": 2, "laurea triennale": 3, "laurea magistrale": 4 }
    livello1 = livelli[persona1.titolo_studio]
    livello2 = livelli[persona2.titolo_studio]
    d=livello1-livello2
    diff_eta=persona2.eta-persona1.eta
    if d==3 :
        peso_t=10
    elif d==3 :
        peso_t=10
    elif d==2:
        peso_t =7
    elif d==1:
        peso_t=5
    elif d==0:
        peso_t=0
    else:
        peso_t=-1
    if diff_eta >= 20:
        peso_eta = 10
    elif diff_eta >= 10:
        peso_eta = 5
    elif diff_eta > 0:
        peso_eta = 2
    else:
        peso_eta = 0
    peso=0.7*peso_t+0.3*peso_eta
    return peso
def calcola_peso_tutto(persona1, persona2):
    simpatia = random.randint(1, 10)

    e1 = persona1.eta
    e2 = persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta = e2 - e1
    if dif_eta > 20:
        e = 10
    elif dif_eta > 10:
        e = 7
    elif dif_eta < 0:
        e = 0
    else:
        e = 1
    dif_serv = serv2 - serv1
    if dif_serv > 20:
        s = 10
    elif dif_serv > 10:
        s = 7
    elif dif_serv < 0:
        s = 0
    else:
        s = 1
    livelli = {"licenza media": 1, "diploma": 2, "laurea triennale": 3, "laurea magistrale": 4}
    livello1 = livelli[persona1.titolo_studio]
    livello2 = livelli[persona2.titolo_studio]
    d = livello1 - livello2
    if d == 3:
        st = 10
    elif d == 2:
        st = 7
    elif d == 1:
        st = 5
    elif d == 0:
        st = 0
    else:
        st = -1
    di = persona1.calcola_distanza(persona2)
    dist = 10 / (1 + di)
    peso= 0.15*st+0.1*e+0.20*s+0.25*simpatia+0.3*dist
    return peso

def calcola_antipatia_compensata_titolo_eta(persona1,persona2):
    simpatia=random.randint(-5,7)
    e1 = persona1.eta
    e2 = persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta = e2 - e1
    if dif_eta > 20:
        e = 10
    elif dif_eta > 10:
        e = 7
    elif dif_eta < 0:
        e = 0
    else:
        e = 1
    livelli = {"licenza media": 1, "diploma": 2, "laurea triennale": 3, "laurea magistrale": 4}
    livello1 = livelli[persona1.titolo_studio]
    livello2 = livelli[persona2.titolo_studio]
    d = livello1 - livello2
    if d == 3:
        st = 10
    elif d == 2:
        st = 7
    elif d == 1:
        st = 5
    elif d == 0:
        st = 0
    else:
        st = -1
    peso=0.3*st+0.3*e+0.3*simpatia
    return peso

def calcola_peso_antipatia_ncom(persona1, persona2):
    simpatia = random.randint(-5, 7)
    e1 = persona1.eta
    e2 = persona2.eta
    serv1 = persona1.anni_di_servizio
    serv2 = persona2.anni_di_servizio
    dif_eta = e2 - e1
    if dif_eta > 20:
        e = 10
    elif dif_eta > 10:
        e = 7
    elif dif_eta < 0:
        e = 0
    else:
        e = 1
    livelli = {"licenza media": 1, "diploma": 2, "laurea triennale": 3, "laurea magistrale": 4}
    livello1 = livelli[persona1.titolo_studio]
    livello2 = livelli[persona2.titolo_studio]
    d = livello1 - livello2
    if d == 3:
        st = 10
    elif d == 2:
        st = 7
    elif d == 1:
        st = 5
    elif d == 0:
        st = 0
    else:
        st = -1
    if simpatia < 0:

        peso = 0
    else:
        # simpatia: entra nel calcolo normale
        peso = ( 0.3 * simpatia+0.4 * e + 0.3 * st )
    return peso