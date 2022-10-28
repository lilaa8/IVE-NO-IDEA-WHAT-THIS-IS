

#a)


#d
from dataclasses import asdict
import datetime


class Avtale:
    def __init__(self, tittel, sted , starttidspunkt , varighet):

        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = datetime.datetime.fromisoformat(starttidspunkt)
        self.varighet = int(varighet)

    #e

    def __str__(self):
        return f'{self.tittel} , {self.sted} ,{ self.starttidspunkt} , { self.varighet}'
       


avtale1 = Avtale("9a", "Stavanger", "2022-10-10 13:00", 15)



#f

def skrivAvtale():
    try:
        itittel = input("skriv inn tittel ")
        isted = input("skriv inn sted ")
        istart = input("skriv inn starttidspunkt ( yyyy-mm-dd hh:mm)")
        ivar = input("skriv inn varighet")
        obj = Avtale(itittel, isted , istart , ivar)
    except ValueError:
        print("prov igjen")
        skrivAvtale()

    else:
        
        return obj
    
#skrivAvtale()



#g


def skrivListe(liste , overskrift = ""):
    for i in range (len(liste)):
        print(overskrift)
        print(i)
        print(liste[i])
        print("\n")


#h

import pickle

def saveListe( liste1 ):
    file = open('test.pkl','wb')
    pickle.dump(liste1, file)
    #for i in liste1:
    #    pickle.dump(i , file )
    
    file.close()



#example to check

Avtale2 = Avtale("2a", "Stavanger", "2022-11-10 13:00", 15)
Avtale3 = Avtale("3b", "Stavanger", "2022-12-10 13:00", 15)
Avtale4 = Avtale("4c", "Stavanger", "2022-01-10 13:00", 15)
Avtale5 = Avtale("5d", "Stavanger", "2022-10-10 13:00", 15)

exampleListe = [avtale1, Avtale2, Avtale3 , Avtale4, Avtale5]

#skrivListe(exampleListe)
saveListe(exampleListe)

#i

def leseListe(file1):
    file = open(file1, 'rb')
    liste1 = pickle.load(file)
    file.close()
    return liste1
    

#liste3000 = leseListe('test.pkl')
#skrivListe(liste3000)


#j

def DatoListe(listej , datoj):
    listej2 = []
    for i in listej:
        datei = str(getattr(i, "starttidspunkt").date())
        
        if datei == datoj :
            listej2.append(i)

    return listej2



#example
"""newlist = DatoListe(exampleListe , '2022-11-10')
skrivListe(newlist)
print(len(newlist))"""


#k

def tittelListe( listek , strengk):
    listek2 = []
    for i in listek:
        tittelk = getattr(i , "tittel")
        count = tittelk.find(strengk)

        if count > 0 :
            listek2.append(i)

    return listek2
            

#example
"""a =tittelListe(exampleListe , 'a')
skrivListe(a)"""


#l

avtaler =[]

def meny():
    valg = float(input ("velg nr 1-7 \
    \n 1 for å lese inn avtaler fra fil \n 2 skrive avtalene til fil \
    \n 3 skrive inn en ny avtale \n 4 skrive ut alle avtalene \n 5 slette avtale \n 6 redigere avtale \n 7 avslutte \n :"))

    

    if valg == 1:
        filnavn = input("skriv inn fil navn: ")
        liste11 = leseListe(filnavn)
        for i in liste11:
            avtaler.append(i)

        meny()

    elif valg == 2:
        saveListe(avtaler)
        meny()

    elif valg ==3:
        avtaler.append(skrivAvtale())
        print("p")
        meny()

    elif valg == 4:
        skrivListe(avtaler)
        meny()
    
    elif valg == 5:
        skrivListe(avtaler)
        hvilken = int(input("hvilken avtale vil du slette: "))
        avtaler.pop(hvilken)
        meny()

        

    elif valg == 6:
        skrivListe(avtaler)
        redigere = int(input("hvilken avtale vil du redigere: "))
        rattribute = int(input ("vil du redigere \n 1 tittel, \n 2 sted , \n 3 starttidspunkt , \n4 varighet \n5 meny  \n:"))
        nyverdi = input("skriv inn ny verdi : ")

        if rattribute == 1:
            avtaler[redigere].tittel = nyverdi
            meny()


        elif rattribute == 2:
            avtaler[redigere].sted = nyverdi
            meny()


        elif rattribute ==3:
            avtaler[redigere].starttidspunkt = nyverdi
            meny()


        elif rattribute == 4:
            avtaler[redigere].varighet = nyverdi
            meny()

        
        elif rattribute == 5:
            meny()

    
    elif valg == 7:
        pass

    else:
        print("prøv igjen")
        meny()

meny()

















