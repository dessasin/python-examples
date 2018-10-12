###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

"""
sozluk=dict()# sözlük tanımlamalar
sozluk2={}
"""

sozluk={"home":"ev","book":"kitap","pen":"kalem"}

print(sozluk["home"])# çıktısı ev
print(sozluk["book"])#çıktısı kitap


# oyunsal sözlük uygulaması

karakter={"ad":"dessas","can":100,"guc":25}

karakter2={"ad":"dessasin","can":100,"guc":35}


def vur():
    karakter2["can"]=karakter2["can"]-karakter["guc"]
    karakter["can"]=karakter["can"]-karakter2["guc"]
    print(karakter["can"])
    print(karakter2["can"])

vur()# hantal bir kod kendim yazdım ancak çalışıyor o zaman ellemeyelim xD
