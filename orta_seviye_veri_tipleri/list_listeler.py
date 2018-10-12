###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

listem=[1,2,3,4,5,6,7,8,9,0] # temel liste belirleme yöntemi


# listeler C# da kullandığım diziler ile aynı

# listeye veri ekleme

eklenecek="11"

listem+=[eklenecek]

print(listem)


#liste öğelerine erişme

listOne=["nurullah","torun",12123,"dessasin",0.12]
# listeler   0         1       2      3        4         şeklinde sıralanır
print(listOne[1])


# liste içindeki listenin elemanına ulaşmak

listTwo=[12,11,241,5235,[543,999,645]]

print(listTwo[-1][1])#bu komutta listTwo listesinin son elemanının 1.elemanını göster diyoruz
