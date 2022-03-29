#2. Da se napravi programa vo koja korisnikot ke moze da vnese tri broja vo keys (brojEden, brojDva, brojTri) vo key zbir da se zacuva zbirot na prvite dva broevi, 
# vo key proizvod da se zacuva proizvodot na vtorite dva broevi, a vo key pogolem da se zacuva pogolemiot od dvata rezultati. Da se ispecatat site potrebni informacii za programta. Formatot ostanuva na vas

podatoci={}

brojEden = int (input ("Vnesete prv broj: \n"))
podatoci["brojEden"] = brojEden

brojDva = int (input ("Vnesete vtor broj : \n"))
podatoci["brojDva"] = brojDva

brojTri = int (input ("Vnesete tret broj : \n"))
podatoci["brojTri"] = brojTri

print ("Vnesenite broevi se {}, {}, {}".format (brojEden, brojDva, brojTri))
podatoci['zbir'] = podatoci['brojEden'] + podatoci['brojDva']
#podatoci.update({"keyZbir":keyZbir})
print ("Zbirot od dvata broja e {} i e zacuvan vo keyZbir".format (podatoci['zbir']))

#keyProzivod = (brojDva*brojTri)
podatoci['proizvod'] = podatoci['brojDva'] * podatoci['brojTri']
print ("Proizvodot od dvata broja e {} i e zacuvan vo keyProizvod".format (podatoci["proizvod"]))

if (podatoci['zbir'])>(podatoci['proizvod']):
 #   podatoci.update({"keyZbir":keyZbir})
    print ("Zbirot e pogolem od proizvodot")

else:
#    podatoci.update({"keyProizvod": keyProzivod})
    print ("Proizvodot e pogolem od zbirot")




