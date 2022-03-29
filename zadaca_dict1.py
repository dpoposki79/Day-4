#Da se napravi programa vo koja ke imate dictionary so licni podatoci za nekoj korisnik (ime, prezime, mesto na ziveenje, godina, datum na ragjanje,pol)
# - da moze da se ispecati poraka vo format: "Korisnikot so {ime}, {prezime}, koj zivee na {mesto na ziveenje} e roden na {datum na raghjanje}"
# - da se ispecatat site klucevi i korisnikot da izbere koj podatok da se ispecati vo format: kluc:vrednost

podatoci = {
        "ime" : "Dimitar",
        "prezime" : "Poposki",
        "mesto" : "Skopje",
        "godina" : 1979,
        "data" : "25 Maj",
        "pol" : "maski"
        }
print ("Korisnikot so ime {} prezime {}, koj zivee vo {} e roden {} {}".format (podatoci["ime"], podatoci["prezime"], podatoci["mesto"], podatoci["data"], podatoci["godina"]))

print(podatoci.keys())

#for i in range(1):
g = input ("Odberete kluc :")

print ("{}: {}".format(g, podatoci.get(g)))
