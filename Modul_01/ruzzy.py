print ("===========================")
print("program menghitung predikat lulusan")

print ("===========================")

matematika = float (input("masukan nilai matematika = "))
biologi    = float (input("masukan nilai biologi = "))
fisika     = float (input("masukan nilai fisika = "))

#block proses perhitungan nilai 

IPS= (matematika + biologi + fisika)/3

# block penulisan predikat
print ("indeks prestasi semester =", IPS)

print ("===========================")

if IPS >= 85 :
    print ("anda termasuk predikat istimewa ")
elif IPS >= 75 :
    print ("anda termasuk predikat baik ") 
elif IPS >= 60 :
    print ("anda termasuk predikat cukup ")  
else:
    print ("anda harus mengulang")
print ()
print ("===========================")