#Da se napravi programa vo koja ke imate dictionary so licni podatoci za nekoj korisnik (ime, prezime, mesto na ziveenje, godina, datum na ragjanje,pol)
# - da moze da se ispecati poraka vo format: "Korisnikot so {ime}, {prezime}, koj zivee na {mesto na ziveenje} e roden na {datum na raghjanje}"
# - da se ispecatat site klucevi i korisnikot da izbere koj podatok da se ispecati vo format: kluc:vrednost

podatoci={}

imeprezime = input ("Vnesete ime i prezime :")
podatoci["imeprezime"] = imeprezime

mesto = input ("Vnesete mesto na ziveenje :")
podatoci["mesto"] = mesto

godina = input ("Vnesete godina na raganje :")
podatoci["godina"] = godina

datum = input ("Vnesete data na raganja :")
podatoci["datum"] = datum

pol = input ("Vnesete pol :")
podatoci["pol"] = pol

print (podatoci)

