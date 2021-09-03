from Savollar import yakuniy_savollar
import random

def qaysi_fan(savollar):
    whichfan = input("Sizga qaysi fan kerak? ")
    if whichfan in savollar.keys():
        return whichfan
    else:
        return False


def fan_savollari(dic, key):
    return dic[key]

    # Test fan_savollari()
#print(fan_savollari(yakuniy_savollar, 'fan_1'))


def Savollar(baza):
    savollar = []
    fan = qaysi_fan(baza)
    if fan:
        savollar.append(fan_savollari(baza, fan))
    return savollar[0]

""" 
Test Savollar(baza)
    savol = savollar(yakuniy_savollar)
    print(len(savol))
"""

def Savol20(baza):
    savollar = Savollar(baza)
    savol20 = []
    i=0
    while i<20:
        savol20.append(savollar[i])
        i+=1
    return savol20
print(Savol20(yakuniy_savollar))
"""
Test Savol20(baza):
    Savol20(yakuniy_savollar)

"""
list  = [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
]
num = random.randint(1,21)
list.remove(num)


print(list)
#print(dir(random))

#print(random.choice(["Botirjon", "shaxzod", 'Sobir']))