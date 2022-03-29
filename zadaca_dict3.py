#3. Da se napravi programa vo koja korisnikot ke moze da vnese 4 broevi, 
# da se najde zbirot na tie 4 broevi i da se presmeta prosekot, i zbirot i prosekot da se zacuvaat vo dictionary


elementi = {}

brojEden = int (input ("Vnesete prv broj: \n"))
elementi["brojEden"] = brojEden
brojDva = int (input ("Vnesete vtor broj: \n"))
elementi["brojDva"] = brojDva
brojTri = int (input ("Vnesete tret broj: \n"))
elementi["brojTri"] = brojTri
brojCetiri = int (input ("Vnesete cetvrt broj: \n"))
elementi["brojCetiri"] = brojCetiri
elementi['zbir'] = elementi['brojEden'] + elementi['brojDva'] + elementi['brojTri'] + elementi['brojCetiri']
print("Zbirot e {}".format(elementi['zbir']))
elementi["prosek"] = elementi["zbir"] / len(elementi)
print("Prosekot e {}".format(elementi['prosek']))
 
 

