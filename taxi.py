#taxi.py

'''
0-1 = 35 b/km
>1-10 = 5.5 b/km
>10-20 = 6.5 b/km
>20-40 = 7.5 b/km
>40-60 = 8.0 b/km
>60-80 = 9.0 b/km
>80 + = 10.5 b/km

# distance = 2.45 km
# 1.0 km = 35
# 2.0 km = 5.5
# 0.45 km = 0.45 * 5.5
'''
import math

def Taxi(dist=10):
    distance = dist #km
    #print(distance)
    # if distance = 10.87
    distance2 = distance - math.floor(distance) #distance2 = 0.87
    distance = math.floor(distance) #distance = 10

    box = 0
    check = {1:5.5,10:6.5,20:7.5,40:8.0,60:9.0,80:10.5}
    for i in range(1,distance+1):
        #print('กิโลเมตรที่:',i)
        if i == 1:
            tx = 35
        elif i > 1 and i <= 10:
            tx = 5.5
        elif i > 10 and i <= 20:
            tx = 6.5
        elif i > 20 and i <= 40:
            tx = 7.5
        elif i > 40 and i <= 60:
            tx = 8.0
        elif i > 60 and i <= 80:
            tx = 9.0
        else:
            tx = 10.5
        box = box + tx #box += tx
        #print(tx)

    if distance in check:
        tx = check[distance]
        extra = distance2 * tx
    else:
        tx = tx
        extra = distance2 * tx
    print('TX:',tx)
    calculate = round(box + extra)
    print(f'คุณเดินทาง: {dist} กิโลเมตร\nต้องจ่ายเงินค่าแท็กซี่: {calculate} บาท')

while True:
    dist = float(input('Enter KM.:'))
    Taxi(dist)
    print('------------')
    
