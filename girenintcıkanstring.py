#girilen sayının 3 er basamaklar halinde göndereceğim fonksiyon
from decimal import Decimal
import math

birler = {'0': '', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dört', '5': 'beş', '6': 'altı', '7': 'yedi',
              '8': 'sekiz', '9': 'dokuz'}
onlar = {'0': '', '1': 'on', '2': 'yirmi', '3': 'otuz', '4': 'kırk', '5': 'elli', '6': 'altmış', '7': 'yetmiş',
             '8': 'seksen', '9': 'doksan'}
yuz = ['yüz']

def fonk(sayi):
    if(len(sayi)==3):
#sayının ilk basamağının 1 olma durumunu ve 0 olma durumunu kontrol etmem lazım
        if(sayi[0]=='1'):
            yaz=yuz[0]+' '+onlar[sayi[1]]+' '+birler[sayi[2]]
            return yaz
        if(sayi[0]=='0'):
            yaz=onlar[sayi[1]]+' '+birler[sayi[2]]
            return yaz
        else:
            yaz=birler[sayi[0]]+' '+yuz[0]+' '+onlar[sayi[1]]+' '+birler[sayi[2]]
            return yaz
    if(len(sayi)==2):
        yaz = onlar[sayi[0]]+' ' + birler[sayi[1]]
        return yaz
    if(len(sayi)=='1'):
        if(sayi[0]=='0'):
            yaz='sıfır'
            return yaz
        else:
            yaz=birler[0]+' '
            return yaz

#sayımızın basamak sayısını bulup 3 ün katı değilse başına 0 koyarak 3 e tamamlayalım

f=1
while f==1:
    s=1
    while s==1:
        c=''
        b=''
        sayi1=str(Decimal(input("bir sayı değeri giriniz:")))

        for i in range (len(sayi1)-1):
            if sayi1[i]=='.':
                for j in range(i+1,len(sayi1)):
                   c+=str(sayi1[j])

                break
            else:
                b+=str(sayi1[i])
        if len(c)>2:
            print('noktadan sonra en fazla 2 sayı yazınız')
            break
        sayi=b
        basamak= len(sayi)%3

        if (basamak==1):
            sayi='00'+sayi
        elif(basamak==2):
            sayi='0'+sayi
        else:
            sayi=sayi
        #sayımızın içinde kaç tane 3 lü grup olduğunu bulalım
        grup=math.ceil(int(len(sayi))/3.0)

        uclugrup={'0':'','1':'yüz','2':'bin','3':'milyon','4':'milyar','5':'trilyon','6':'kattrilyon'}

        #2 sorgu yazıyorum bir tanesi göndereceğim 3lü basamağın hepsi 000 sa sayı atamadan bir sonraki sayıya geçmeli
        # ikincisi 001 ise sayı değeri yerine basamak yazmalı ama bu sayı 1001 şeklindeyse de birler basamağı için sayı değerini yazmalı
        a=1
        yaz=''
        sayi=list(sayi)

        if(len(sayi)>18):
            print('Çok büyük bir sayı girdiniz ')
        else:
            for i in range(int(grup)):

                if sayi[-1*((i*3)+3)]+ sayi[-1*((i*3)+2)]+ sayi[-1*((i*3)+1)]=='000':
                    yaz=yaz

                elif sayi[-1*((i*3)+3)]+ sayi[-1*((i*3)+2)]+ sayi[-1*((i*3)+1)]=='001'and len(sayi)==6 :
                    if i==0:
                        yaz=birler[sayi[-1*((i*3)+1)]]+' '+yaz
                    elif sayi[-1*(((i-1)*3)+3)]+ sayi[-1*(((i-1)*3)+2)]+ sayi[-1*(((i-1)*3)+1)]=='000':
                        yaz=birler[sayi[-1*((i*3)+1)]]+' '+uclugrup[str(i+1)]+' '+yaz
                    else:
                        yaz= ' '+uclugrup[str(i+1)]+' '+yaz
                elif sayi[-1*((i*3)+3)]+ sayi[-1*((i*3)+2)]+ sayi[-1*((i*3)+1)]=='001'and i==1 :

                   yaz = ' '+uclugrup[str(i + 1)]+' ' + yaz
                else:
                    if(a==1):
                       yaz= fonk(sayi[-1*((i*3)+3)]+ sayi[-1*((i*3)+2)]+ sayi[-1*((i*3)+1)]) +' '+ uclugrup[str(i)]+' '+yaz
                    else:
                       yaz= fonk(sayi[-1 * ((i * 3) + 3)] + sayi[-1 * ((i * 3) + 2)] + sayi[-1 * ((i * 3) + 1)]) +' '+ uclugrup[str(i+1)]+' ' +yaz
                a+=1


        if c[0] == '0' and c[1] == '0':
            yaz += 'TL sıfır KURUŞ'
        elif len(c)==2 :

            if c[1]=='0':
                yaz += 'TL ' + onlar[c[0]] + ' KURUŞ'

            elif c[0]=='0':

                yaz += 'TL ' + 'sıfır '+birler[c[1]] + ' KURUŞ'

        else:
            yaz += 'TL ' + birler[c[0]]+' KURUŞ'
            print("ddf")
        print(yaz)
        s=0
    print('Tekrar sayı girmek ister misiniz? Evet ise 1 e hayır ise 0 ye basın')
    f=int(input())

