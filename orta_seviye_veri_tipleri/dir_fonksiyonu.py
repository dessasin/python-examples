###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

# dir() fonksiyonu bir değişkenin fonksiyonun önceden eklenmiş olan metotlarını gösterir

#örnek olarak bir listeye gönderilecek metotlar listesi

listem=["denem","deneme"]

for i in dir(listem):
    print(i)
    

"""
bu döngünün çıktısı

__add__
__class__
__contains__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__gt__
__hash__
__iadd__
__imul__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__rmul__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
"""

#örnek bir kullanım

listem2=["ders","kalem"]

listem2.append("silgi") # listeye öğe ekleme
print(listem2)

listem2.remove(listem2[-1])# listeden öğe çıkarma

print(listem2)

listem2.reverse()# listeyi ters çevirme
print(listem2)