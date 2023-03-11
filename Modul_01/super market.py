print("============================")
hargabaju= int(input("masukan harga baju"))

total_harga = 0
potongan_harga = 0


if harga_baju >= 100000:
    potongan_hargabaju= hargabaju * 10/100
    total_harga = harga_baju-potongan_harga

print("nilai pembayaran anda adalah = ", total_harga)
print("nilai nilai discount yang diperoleh = ", potongan_harga)

