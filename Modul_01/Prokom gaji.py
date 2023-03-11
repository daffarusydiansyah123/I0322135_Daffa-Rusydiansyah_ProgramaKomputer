#input
print("=====================")
nama = input( 'nama karyawan : ')
gol = int(input('golongan : '))
kel = int(input('kelebihan jam kerja (jam) : '))
print("=====================")
print()

#proses perhitungan gaji
a = nama
b = golongan
c = gol *1000000
d = kel*2000000
e = c+d

#total gaji
print("=====================")
print( 'nama karyawan :', a)
print( 'golongan :', b)
print('gaji pokok :', c)
print('lembur :', d)
print('pendapatan :',e)
print("=====================")

