nama_barang = input("Masukkan nama barang  : ")
harga_satuan = int(input("Masukkan harga satuan : "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

print(f"Subtotal {subtotal}, PPN {ppn}, Total {total_bayar}")
