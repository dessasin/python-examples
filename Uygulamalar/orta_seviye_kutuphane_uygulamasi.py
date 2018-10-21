###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################
import os

# gereklilikler
#liste
# kitap adlarını demetler ile ekleyeceğiz


kitapliste=list()

menu="""

[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış
"""
def kitapekle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme İşlemi Tamamlandı")
    print("Ana Menü İçin Enter Basınız ")
    input()

def kitap_varmi(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapCikar(kitap:tuple,liste:list):
    if kitap_varmi(kitap,liste):
        #kitap çıkartıyoruz
        liste.remove(kitap)
        print("Kitap Çıkarma İşlemi Tamamlandı")
        print("Ana Menü İçin Enter Basınız ")
        input()
    else:
        print("Aradığınız Kitap Listelerimizde Mevcut değil")
        print("Ana Menü İçin Enter Basınız ")
        input()  


def listele(liste:list):
    for i in liste:
        print("Kitap Adı: {}   Yazar:{}".format(i[0],i[1]),end="")
    print("Ana Menü İçin Enter Basınız ")
    input()
       


while True:
    os.system("clear")#terminali temizler
    print(menu)
    secim=input("İşleminizi Seçiniz: ")

    if secim=="1":
        kitap_isim=input("Kitap Adı: ")
        kitap_yazar=input("Kitap Yazar: ")
        kitap=(kitap_isim,kitap_yazar)
        kitapekle(kitap,kitapliste)

    elif secim=="2":
        kitap_isim=input("Kitap Adı: ")
        kitap_yazar=input("Kitap Yazar: ")
        kitap=(kitap_isim,kitap_yazar)
        kitapCikar(kitap,kitapliste)

    elif secim=="3":
        listele(kitapliste)
    elif secim=="Q"or"q":
        quit()
    else:
        prin("hatalı giriş yaptınız")
