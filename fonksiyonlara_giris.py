###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

# fonksiyon tanımlama

def fuction_name(): # fonksiyon başlığı def (definition) function_name(fonksiyon adı) () parametre alanı : blok ayracı

    sayi=12+12 # fonksiyon işleci
    print(sayi) # çıktı


# tekrarlanabilme

def topla ():
    sonuc=3+5
    print(sonuc)

topla() #fonksionun istenilen miktarda çağrılabilmesi özelliği
topla()

#parametrize etme özelliği

def toplam(x,y):
    sonuc2=x+y
    print(sonuc2) # x ve y fonksiyonun parametreleridir eğer parametre vermeden fonksiyon çağrılırsa hata alınır


toplam(123,123) 


"""
fonksiyonlar bir problemi çözer aldıkları girdileri her zaman çıktı olarak kulanıcıya vermezler  
bunun için ilgili ayarlamaların yapılması lazımdır örneğin:

def fonksiyon(parametre1,parametre2):
    output=parametre1+parametre2
    return output

print(fonksiyon(parametre1,parametre2)) 

"""

def returned (j,k):
    output=j*k
    return output # return ile fonksiyon işleminin çıktısı fonksiyon dışın aktarılır aksi halde fonksiyon none değer döndürür

print(returned(123,123))