#4.Da se napravi programa vo koja korisnikot ke moze vo dictionary so key listaPazarenje, 
# da zacuva lista so produkti za pazarenje, da moze da se dodavaat produkti kolku sto saka korisnikot
listaPazarenje = []
listaProdukti = {"listaPazarenje":[]}
x = int (input ("Kolku produkti sakate da vnesete: \n"))
for i in range(x):
    proizvod=input("Vnesete proizvod: \n")
    
    listaPazarenje.append(proizvod)
    
print (listaPazarenje)
listaProdukti.update({"listaPazarenje" : listaPazarenje})
print(listaProdukti)
    
