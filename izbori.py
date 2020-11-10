import time

def dobrodoslica():
    print ("#####################################################################\n")
    print ("AI softver za kalkulaciju pobjednika lokalnih izbora 2020\n")
    print ("#####################################################################\n")
    print ("Unesite ime stranke ili skracenicu i pritisnite enter\n")
    print ("Stranke možete unositi sve dok ne unesete STOP i pritisnete enter\n")
    print ("#####################################################################\n\n")

def unesi_stranke():
    stranke = []
    while True:
        ime_stranke = input("Unesite ime strankie ili skracenicu --> ")
        if ime_stranke == "STOP" or ime_stranke == "stop":
            pogodi_izbore(stranke)
            break
        else:
            ime_stranke = " ".join(ime_stranke.split()).lower()
            stranke.append(ime_stranke)

def ml_kalkulacie(imal_nasih):
    print ("Algoritam za pretpostavljanje pobjednika izbora se pokrenuo\n")
    print ("Procjena moze trajati do 5 sekundi\n")
    print ("Kalkulacija ----> 0%\n")
    time.sleep(1)
    print ("Kalkulacija ----> 27%\n")
    time.sleep(1)
    print ("Kalkulacija ----> 48%\n")
    time.sleep(1)
    print ("Kalkulacija ----> 66%\n")
    time.sleep(1)
    print ("Kalkulacija ----> 98%\n")
    time.sleep(1)
    print ("Kalkulacija ----> 100%\n\n")

    #ML magija se dešava ovdje
    if imal_nasih:
        print ("Izbore će pobijediti SDA")
    else:
        print ("Lopta je okrugla. Sve je moguće")


def pogodi_izbore(stranke):
    imal_nasih = False
    for stranka in stranke:
        if stranka == "sda" or stranka == "stranka demokratske akcije":
            imal_nasih = True
            break
    ml_kalkulacie(imal_nasih)

if __name__ == '__main__':
    dobrodoslica()
    unesi_stranke()