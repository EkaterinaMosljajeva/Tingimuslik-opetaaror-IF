from math import *


#1
#try:
#    nimi=input("Sisestage oma nimi: ")
#    if nimi.upper()==("JUKU"):
#        print("Lähme kinno")
#        vanus=int(input("Sisestage oma vanus: "))
#        if vanus<0 or vanus>100:
#            print("Viga andmetega")
#        elif vanus<6:
#            print("Tasuta")
#        elif vanus>=6 and vanus<=14:
#            print("Lastepilet")
#        elif vanus>=15 and vanus<=65:
#            print("Täispilet")
#        elif vanus>65:
#            print("Sooduspilet")
#    else:
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüüp")

#2
#nimi1=input("Sisestage esimese isiku nimi: ")
#nimi2=input("Sisestage teise isiku nimi: ")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1.lower()==("juku") and nimi2.lower()==("nami"):
#        print(f"{nimi1} ja {nimi2} olete täna naabrid")
#    else:
#        print("Sa ei ole Juku ja Nami")
#else:
#    print("Vale Andmetüüp")

#3
#try:
#    pikkus=float(input("Sisesta pikkus: "))
#    laius=float(input("Sisesta laius: "))
#    if pikkus>0 and laius>0:
#        S=laius*pikkus
#        print(f"Ruumi pindala on {S}")
#        vast=input("Kas soovite remonti teha? ")
#        if vast.lower()==("jah"):
#            rm=float(input("Kui palju on ruutmeeter? "))
#            if rm>0:
#                hind=S*rm
#                print(f"Remondi maksumus jääb {hind}")
#            else:
#                print("Vale Andmetüüp")
#        elif vast.lower()==("ei"):
#            print("Kahju")
#        else:
#            print("Vastus saab olla ainult jah või ei")
#    else:
#        print("Andmed peavad olema suuremad kui 0")
#except:
#    print("Vale Andmetüüp")

#4
#try:
#    hind=float(input("Sisesta hind: "))
#    if hind>700:
#        hind=hind*0,7
#        print(f"Hind saab olema {hind}")
#    elif hind<=700 and hind>0:
#        print(f"Hind saab olema {hind}")
#    else:
#        print("Andmed peavad olema suuremad kui 0")
#except:
#    print("Vale Andmetüüp")

#5 -

#6
#try:
#    pikk=int(input("Kui pikk sa oled? "))
#    if pikk>100 and pikk<160:
#        print("Sa oled lühike")
#    elif pikk>=160 and pikk<180:
#        print("Sa oled keskmine")
#    elif pikk>=180 and pikk<220:
#        print("Sa oled pikk")
#    else:
#        print("Sisestage tegelik kõrgus")
#except:
#    print("Vale Andmetüüp")

#7
#try:
#    sugu=input("Mis su sugu on? Mees või naine? ")
#    if sugu.isalpha():
#        if sugu.lower()==("mees"):
#            pikk=int(input("Kui pikk sa oled? "))
#            if pikk>100 and pikk<170:
#                print("Sa oled lühike")
#            elif pikk>=170 and pikk<180:
#                print("Sa oled keskmine")
#            elif pikk>=180 and pikk<220:
#                print("Sa oled pikk")
#            else:
#                print("Sisestage tegelik kõrgus")
#        elif sugu.lower()==("naine"):
#            pikk=int(input("Kui pikk sa oled? "))
#            if pikk>100 and pikk<160:
#                print("Sa oled lühike")
#            elif pikk>=160 and pikk<170:
#                print("Sa oled keskmine")
#            elif pikk>=170 and pikk<220:
#                print("Sa oled pikk")
#            else:
#                print("Sisestage tegelik kõrgus")
#        else:
#            print("Vastuseks saab olla ainult mees või naine")
#    else:
#        print("Vale Andmetüüp")
#except:
#    print("Vale Andmetüüp")
