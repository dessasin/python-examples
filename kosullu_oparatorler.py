###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

#%% Bool operatorler kullanımı

# and operatörü

sayi = int(input("sayı "))
if sayi > 5:
    if sayi%2==0:           # birinci kullanım biçimi
        print("doğru")

if sayi >5 and sayi %2 ==0:
    print("doğru")           # düzenlenmiş ve olması gereken kullanım
    
"""
bu fonksiyonda sayı beşten büyük ve 2 ye bölümünden kalan 0 ise doğru yaz komutunu veriyoruz

"""

# or operatoru

#
#if sayi>=5:
#    print("doğru") # birinci kullanım biçimi
#    
#
#if sayi > 5 or sayi ==5:
#    print("doğru") # düzenlenmiş kullanım 

"""
bu fonksiyon ile sayı 5 den büyük "yada" eşitse
""" 

x=int(input("X gir : "))
y=int(input("Y gir : "))

if x==4 or y== 4 :
    print("doğru")
else:
     print("en az biri 4 olmalı") 
     

# not operatörü

x=input("X gir : ")
y=input("Y gir : ")

if bool (x):                #not operatöründen hiçbir şey anlamadım kilit
    print("yanlış")
if not bool(x):
    print("doğru")
    
# %% in operatörü aitlik
    
parola="desasin"
                    
if "*" not in parola: # eğer parolanın içinde * yoksa ekrana mesajı yaz 
    print("lütfen parolanızda * kullanınız")
    
    
# %% kimlik operatörü

# is ve id işleci

a=5 
b=5

if a==b: #      == değişkenlerin içeriğine bakar
    print("aynı")

if a is b: # is ifadesi değişkenlerin kimlik değerlerine bakar 
    print ("aynı")    
    
    