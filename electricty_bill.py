units=int(input())
if units<=199:
    char=1.20
elif units>=200 and units<400:
    char=1.50
elif units>=400 and units<600:
    char=1.80
else:
    char=2.00
bill=char*units
if bill>400:
    sur_charge=0.15*bill
else:
    sur_charge=100
totoal=sur_charge+bill
print("%.2f"%totoal)
