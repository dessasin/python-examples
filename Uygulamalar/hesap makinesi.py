###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında: Hesap Makinesi Örneği         #
###########################################


#Kütüphaneler ~ Dictionaries


#Değişkenler ~ Variables
sayi1=0
sayi2=0
sonuc=0
islem=""


#Fonksiyonlar ~ Functions

    
def topla():
    sonuc=sayi1+sayi2
    print("Sonuç: ",int(sonuc))
       
def cikar():
    sonuc=sayi1-sayi2
    print("Sonuç: ",int(sonuc))
   
def carp():
    sonuc=sayi1*sayi2
    print("Sonuç: ",int(sonuc))

def bol():
    if  sayi1==0 or sayi2 ==0:
        print("Sıfırdan farklı bir sayı giriniz ")
        
    else:
        sonuc=sayi1/sayi2
        print("Sonuç: ",int(sonuc))
    
           

#Sınıflar ~ Classes


#Ana Kodlar ~ Main Codes
sayi1=float(input("Lütfen ilk sayıyı giriniz:  "))
sayi2=float(input("Lütfen ikinci sayıyı giriniz:  "))

print("Lütfen Yapmak İstediğiniz İşlemin Simgesini Giriniz","\n")
print("Toplama(+)","Çıkarma(-)","Çarpma(*)","Bölme(/)",sep="\n")

islem=input("İşlem: ")
if islem =="+":
    topla()
elif islem=="*":
    carp()
elif islem =="/":
    bol()
else:
    cikar()      
   
