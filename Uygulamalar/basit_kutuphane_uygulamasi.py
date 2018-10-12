###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

kitapListe=[]

menu="""
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitapları Listele
[q] Çıkış
"""

def kitapEkle(kitap,liste):
    liste+=[kitap]
    print("Kitap Eklendi")
    input("Ana Menu İçin 'enter' basınız")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print("Kitap adı: {}".format(i))
    input("Ana Menu İçin 'enter' basınız")

def cik():
    quit()


while True:
    print(menu)
    secim=input("Seçiminiz:")
    if secim=="1":
        kitapAdi= input("Kitap Adı:")
        kitapEkle(kitapAdi,kitapListe)
    
    elif secim=="2":
        kitapCikar()

    elif secim=="3":
        listele(kitapListe)
    elif secim=="q" or secim=="Q":
        cik()
    else:
        print("hatalı giriş yaptınız")