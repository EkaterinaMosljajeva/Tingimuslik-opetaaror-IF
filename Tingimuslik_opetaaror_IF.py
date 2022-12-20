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

#8
#try:
#    p=input("Kas soovite piima osta? ")
#    if p.isalpha():
#        if p.lower()==("jah"):
#            print("Piim maksab 2 euro")
#            piim=int(input("Mitu tükki sa tahad? "))
#            piim=piim*2
#            print(f"See maksab {piim} euro")
#        elif p.lower()==("ei"):
#            print()
#            piim=0
#        else:
#            print("Vastus saab olla ainult jah või ei")
#    else:
#        print("Vale Andmetüüp")
#    s=input("Kas soovite saia osta? ")
#    if s.isalpha():
#        if s.lower()==("jah"):
#            print("Saia maksab 1 euro")
#            saia=int(input("Mitu tükki sa tahad? "))
#            saia=saia*1
#            print(f"See maksab {saia} euro")
#        elif s.lower()==("ei"):
#            print()
#            saia=0
#        else:
#            print("Vastus saab olla ainult jah või ei")
#    else:
#        print("Vale Andmetüüp")
#    l=input("Kas soovite leib osta? ")
#    if l.isalpha():
#        if l.lower()==("jah"):
#            print("Leib maksab 3 euro")
#            leib=int(input("Mitu tükki sa tahad? "))
#            leib=leib*3
#            print(f"See maksab {leib} euro")
#        elif l.lower()==("ei"):
#            print()
#            leib=0
#        else:
#            print("Vastus saab olla ainult jah või ei")
#    else:
#        print("Vale Andmetüüp")
#    hind=piim+saia+leib
#    print(f"Hind on {hind} euro")
#except:
#    print("Vale Andmetüüp")

#9 -

#10
#try:
#    a=float(input("Sisestage esimene number: "))
#    b=float(input("Sisestage teine number: "))
#    if a>0 and b>0:
#        z=input("Milliseid meetmeid tuleb võtta(+,-,*,/)? ")
#        if z==("*"):
#            summa=a*b
#            print(f"Vastus on {summa}")
#        elif z==("+"):
#            summa=a+b
#            print(f"Vastus on {summa}")
#        elif z==("-"):
#            summa=a-b
#            print(f"Vastus on {summa}")
#        elif z==("/"):
#            summa=a/b
#            print(f"Vastus on {summa}")
#        else:
#            print("Tuleb valida üks saadaolevatest valikutest(+,-,*,/)")
#    else:
#        print("Arvud peavad olema suuremad kui 0")
#except:
#    print("Vale Andmetüüp")

#11 -

#12
#try:
#    hind=float(input("Sisesta kauba hind: "))
#    if hind<10 and hind>0:
#        hind=hind*0,9
#        print(f"Saate 10% allahindlust, kogumaksumus on {hind}")
#    elif hind>10:
#        hind=hind*0,8
#        print(f"Saate 20% allahindlust, kogumaksumus on {hind}")
#    else:
#        print("Hind peab olema suurem kui 0")
#except:
#    print("Vale Andmetüüp")

#13
try:
    sugu=input("Mis su sugu on? Mees või naine? ")
    if sugu.isalpha():
        if sugu.lower()==("mees"):
            vana=int(input("Kui vana sa oled? "))
            if vana>=16 and vana=<18:
                print("Sa sobid kandidaatidega")
            else:
                print("Te ei kvalifitseeru, vanus peab olema 16–18")
        elif sugu.lower()==("naine"):
            print("Kandidaadid võivad olla ainult mehed")
        else:
            print("Vastuseks saab olla ainult mees või naine")
    else:
        print("Vale Andmetüüp")
except:
    print("Vale Andmetüüp")