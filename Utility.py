def stampaDizionario(diz):
   for key,value in dizionario .items():
    print("la chiave è ..."+ key)
    print("il valore è ..."+str(value))
    return 
def totaleOre(diz):
    somma=0
    for key,value in diz.items():
         somma+=value
    print(somma) 
def cattedraPiena(diz):
    i=0
    for key,value in diz.items():
        if value==18:
            i+=1
    print(i)
def assegnaOre(diz,prof,ore):
    if prof in diz:
       diz[prof]=ore
def togliOre(prof;ore):
    if 
dizionario ={"rossi":18,"bianchi":16,"verdi":6}
#inserire un elemento nel dizionario
dizionario["viola"]=14
print(dizionario)

assegnaOre(dizionario,"rossi",6)

#modificare una coppia chiave valore
dizionario["bianchi"]=18
print(dizionario)
stampaDizionario(dizionario)
totaleOre(dizionario)
cattedraPiena(dizionario)
#iterare sul dizionario

#calcolare il totale delle ore del dizionario

#numero degli insegnanti con cattedra piena (18)
