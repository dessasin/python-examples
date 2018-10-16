###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

#liste metodlarını listele

for i in dir(list()):
    if "__" not in i:
        print(i)
"""
append -->> ekle
clear  -->> temizle
copy   -->> kopyala
count  -->> hesapla
extend
index  -->> verinin listede kaçıncı indexte olduğunu gösterir
insert -->> listenin istenilen indexsine veri ekleme 
pop
remove  -->> çıkar
reverse -->> terse çevir 
sort    -->> listeyi sıralar
"""        

liste=["araba","traktör","römork","çiftçi"]

#append

liste.append("buğday")

def afterappendlist(liste):
    for i in liste:
        print (i)


afterappendlist(liste)

#remove
liste.remove("araba")

def afterremovelist(liste):
    for i in liste:
        print (i)

afterremovelist(liste)


# count aynı öğeden kaç tane olduğunu bulur 
listetwo=[1,2,3,4,2,1,5,232,41,21,22,1,1,1,45,23,54,34,45,2]
print(listetwo.count(1))# yanıt 5 

#extend listeleri birleştirme

liste.extend(listetwo)
print(liste)

#index
sira=listetwo.index(232)

print(sira) # çıktı 7 

