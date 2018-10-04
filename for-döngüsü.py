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

