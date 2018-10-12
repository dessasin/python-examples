###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

def sagslash(adet): # ekrana / yazdırma fonksyonu
    for i in range(int(adet)):
        print("/",end="") # çıktı alt satıra inmemesi için varsayılan olan \n komutunu "" ile değiştirdik


def solslash(adet): # ekrana \ yazdırma fonksyonu
    for i in range(int(adet)):
        print("\\",end="") #eğer "\" koyarsak kaçış dizisi olarak algılanır ve hata veriri bu yüzden \\ kullanılır

def satiratla(adet):
    for i in range(int(adet)):
        print()

def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")

"""
paralel kenarı ortadan bölerek 2 parça halinde işlem yapacağız
/ üst kısım ilk boğluğu çap / 2 - 1 formülü ile hesaplıyoruz

"""

def ustkisim(cap):
    baslangicbosluk=cap/2-1# başlangıç boşluğu bulduk
    for i in range(int(cap/2)):# döngünün yukarıdan aşağıya ne kadar ilerleeceğini çapın yarısı kadar olduğı ile tespit ettik
        bosluk(baslangicbosluk-i)#başlangıç boşluğu çıkararak çoktan aza doğru boşluk bastırıyoruz
        sagslash(1) # sağa bir slash koyduk
        bosluk(i*2)# sağ ve sol slash arasına boşluk koyuyoruz
        solslash(1)
        satiratla(1)


def altkisim(cap):
    baslangicbosluk=cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solslash(1)
        bosluk(baslangicbosluk-(i*2))
        sagslash(1)
        satiratla(1)

def paralel(cap):
    ustkisim(cap)
    altkisim(cap)

paralel(10)  