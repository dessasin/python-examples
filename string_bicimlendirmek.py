###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

#standart denemeler ders 1

baslangic="cümlenin basi"
orta="cümlenin ortasi"
son="cümlenin sonu"

newString=baslangic+orta+son
print(newString)

# format metodu 2. ders

# format metodu ile sürekli değişkenlik gösteren alanları doldurmak için kullanıyoruz
cumle="""
english:hello world
türkçe: {} {}
""".format("merhaba","dunya")

print(cumle)

cumlem="Bu cümleyi yukarıdan aşağıya bastıracağım"

for i in cumlem:
    print("bastırılan karakter: {}".format(i))


# format metodunun kulanım şekilleri ders 3

# 1-Konumları belirleme

str1="nurullah"
str2="torun"

ifade1="{1} {0} ".format(str1,str2)
ifade2="{0} {1} ".format(str2,str1)

print(ifade1)
print(ifade2)


# örnekleri burada bırakıyorum çok üzerine düşülecek bir durum yok bence lazım oldukça bakacağım