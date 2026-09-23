Nama   : Octavia Putri Vierene<br>
NIM    : 012<br>
Kelas  : A<br>

# Penjelasan:<br>
`def hitung_biaya_parkir()` menerima 2 jenis parameter: 'jenis_kendaraan' dan 'durasi'<br>
`return 0` di gunakan kalau semisalnya jenis kendaraan yang di input tidak sesuai<br>
`jenis = input("masukkan jenis kendaraan(mobil/motor):")` ini program akan meminta input jenis kendaraan<br>
`jam_masuk = int(input("masukkan jam masuk:"))` ini untuk input jam masuk<br>
`jam_keluar = int(input("masukkan jam keluar:"))` ini untuk input jam keluar<br>

`if jam_keluar < jam_masuk:
    lama_parkir = (jam_keluar + 24) - jam_masuk
else:
    lama_parkir = jam_keluar - jam_masuk` kalau semisalnya jam keluar itu lebih kecil dari jam masuk, berarti kendaraan parkir itu sudah melewati tengah malam, sehingga saya menambahkan 24 jam, sehingga hasil dari total biaya tidak negatif atau mines.<br> Kalau tidak maka cukup jam keluar - jam masuk.



# Output:

<img width="514" height="239" alt="image" src="https://github.com/user-attachments/assets/048699c4-ce4f-403d-a8ae-62a964d242e0" />
