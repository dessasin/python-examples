###########################################
# Author:Dessasin                         #
# E-mail:muhammednurullahtorun@gmail.com  #
# github.com/dessasin                     #
# gitlab.com/dessasin                     #
# Hakkında:                               #
###########################################

#bir üçgenin üçgen olabilmesi için a**2+b**2=c**2 förmülün referans alıyoruz


def ucgen_mi(a,b,hip):
    if hip**2==a**2+b**2:
       return "bu bir üçgendir"
    else:
        return "bu üçgen değildir"

print(ucgen_mi(3,4,5))