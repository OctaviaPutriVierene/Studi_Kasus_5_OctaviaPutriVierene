def hitung_biaya_parkir (jenis_kendaraan, durasi):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    else:
        return 0

    total = tarif * durasi
    return  total

jenis = input("masukkan jenis kendaraan(mobil/motor):")
jam_masuk = int(input("masukkan jam masuk:"))
jam_keluar = int(input("masukkan jam keluar:"))

if jam_keluar < jam_masuk:
    lama_parkir = (jam_keluar + 24) - jam_masuk
else:
    lama_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis, lama_parkir)

print("===Data parkiran===")
print("Jenis kendaraan: ", jenis)
print("Jam masuk: ", jam_masuk)
print("Jam keluar: ", jam_keluar)
print("Lama parkir: ", lama_parkir, "jam")
print("Total biaya parkiran kendaraan anda adalah:", total_biaya)
