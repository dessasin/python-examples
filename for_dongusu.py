###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

# %% alfabeyi bastırma
alfabe="abcçdefgğhıijklmnoöprsştuüvyz"

for harf in alfabe:
    print(harf)   # alfabeyi baştan sona alt alta yazdırır

for x in alfabe:
    print(x,end="") # alfabeyi tek satırda yazdırır


sayi=0
for x in alfabe:
    sayi+=1      # alfabedeki öğe sayısı kadar sayi değişkenini bir artırarak ekran yazdırır
    print (sayi)

# %% for döngüsü örnek

degisken = "asfajgadjghjdghjafhgjafdhg"

for i in degisken:
    print(i)


for j in range(0,100):
    print(j)   #0 dan 100 e kadar saydırma


for j in range(100):
    print(j)   #0 dan 100 e kadar saydırma 2. yöntem



for j in range(0,100,2):
    print(j)   #0 dan 100 e kadar 2şerli saydırma 
    
    