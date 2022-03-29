#Da se napravi programa vo koja korisnikot ke moze vo dictionary so key listaPazarenje.
#da zacuva lista so produkti za pazarenje, da moze dase dodavaat produkti kolku sto saka korisnikot
#UPDATE da raboti so while t.e. da moze da se vnesuva se dodeka korisnikot saka
#da nemate pomosna lista tuku direkno vo dictionary da vnesuvate


di={}

prodolzhi="da"
while prodolzhi == "da" or prodolzhi=="DA":

    produkt=input("Vnesete gi vashite produkti: ")
    di[produkt]="produkt"
    print("Vashiot dodaden produkt e: {}".format(produkt))
    prodolzhi=input("Dali sakate da prodolzhite? ")   
      
if prodolzhi.lower!="da":
   print("Vi blagodarime, vashite produkti se: {}".format(di.keys()))
