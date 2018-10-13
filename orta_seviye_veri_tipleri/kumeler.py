###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

#kümeler temel matematik kümeleri ile aynı

# tanımlama

kume=set()

#kümelerin içine istenilen veri tipleri eklenebilir örneğin listeler demetler sözlükler



# kümeler içerisine sayılar direkt olarak alınamaz
# ayrıca kümeler içerisinde sadece bir elemandan bir tane bulunur 


""" 
küme metotları

add          =>>> öğe ekle
difference   =>>> aradaki farklar
remowe       =>>> öğe sil
intersection =>>> Kesişim
"""
kum=set(["liste","elemanlarım"])
kum.add("eklediğim")
print(kum)

print(20*"/")

kum.discard("eklediğim")#öğe çıkarma
print(kum)


#farklar 

deste1=set([1,2,3,4,5,6,7,8,9])
deste=set([2,3,5,6,7,8,9])
print(deste1)
print(deste)

print(15*"*")

print(deste1.difference(deste))
