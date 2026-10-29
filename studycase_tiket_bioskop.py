no_transaksi = 0
total_tiket = 0
total_pendapatan = 0

print("SISTEM KASIR TIKET BIOSKOP")
kode_studio = int(input("Masukkan kode studio (1=Reguler, 2=Premiere, 0=Tutup): "))

#loop
while kode_studio != 0:
    kode_hari = int(input("Masukkan kode hari (1=Weekday, 2=Weekend): "))
    jumlah_tiket = int(input("Masukkan Jumlah tiket: "))

    if kode_studio == 1 or kode_studio == 2) and kode_hari == 1 or kode_hari == 2) and jumlah_tiket >= 1:

        if kode_studio == 1:
            if kode_hari == 1:
                harga = 35000
            else:
                harga = 45000
        else:
            if kode_hari == 1:
                harga = 75000
            else:
                harga = 100000

        tiket_gratis = jumlah_tiket // 5
        tiket_bayar  = jumlah_tiket - tiket_gratis
        total_transaksi = tiket_bayar * harga

        no_transaksi += 1
        total_tiket += jumlah_tiket
        total_pendapatan += total_transaksi

        print(f"TTransaksi ke-{no_transaksi} | Tiket Gratis: {tiket_gratis} | Total Bayar: Rp{total_transaksi:,}\n")
    else:
        print("Input tidak valid\n")

    kode_studio int(input("Masaukkan kode studio (1=Reguler. 2=Premiere, 0=Tutup): "))

print("\n=== REKAP PENJUALAN ===")
print(f"Total Transaksi Valid : {no_transaksi}")
print(f"Total Tiket Terjual   : {total_tiket}")
print(f"Total Pendapatan      : Rp{total_pendapatan:,}")
