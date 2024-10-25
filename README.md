## Membuat tugas kode program dari flowcart 

Nama: Sheila antica oktaviani

Kelas: TI.24.A.1

NIM: 312410002

## Program Mencari Bilangan Terbesar
Program sederhana untuk mencari nilai terbesar dari sekumpulan bilangan yang dimasukkan oleh pengguna menggunakan loop while True dan break statement.
## Deskripsi Program
Program di buat menggunakan bahasa python
- Menggunakan while True untuk perulangan tak terbatas
- Menggunakan break statement untuk menghentikan program
- Membandingkan setiap input dengan nilai maksimum yang tersimpan
- Menampilkan bilangan terbesar yang ditemukan
## Flowcart program
![image](https://github.com/user-attachments/assets/bf214e04-74d1-4199-891a-39908f45f595)
## Kode Program
```Python
max = 0                                              
while True:                                          
    bilangan = int(input("Masukan bilangan(0 untuk berhenti): "))  
    if bilangan == 0:                               
        break                                       
    if bilangan > max:                     
        max = bilangan                     
print(f"Bilangan terbesar: {max}")
```
## Contoh Output program
```Python
Masukan bilangan(0 untuk berhenti): 13
Masukan bilangan(0 untuk berhenti): 10
Masukan bilangan(0 untuk berhenti): 05
Masukan bilangan(0 untuk berhenti): 12
Masukan bilangan(0 untuk berhenti): 7
Masukan bilangan(0 untuk berhenti): 0
Bilangan terbesar: 13
```
## Cara Kerja Program
Program berfungsi untuk mencari bilangan terbesar dari input yang diberikan pengguna. Pertama, program menginisialisasi variabel max dengan nilai 0. Kemudian, program meminta pengguna untuk memasukkan bilangan. Jika bilangan yang dimasukkan bukan 0, program akan memeriksa apakah bilangan itu lebih besar dari nilai max. Jika iya, nilai max akan diperbarui dengan bilangan tersebut. Proses ini berulang hingga pengguna memasukkan 0, yang menandakan akhir dari input. Setelah itu, program mencetak bilangan terbesar yang ditemukan. 

Namun, untuk meningkatkan program, bisa menginisialisasi max dengan None, sehingga dapat menangani situasi di mana pengguna langsung memasukkan 0 tanpa memberikan bilangan lain. Dengan cara ini, program akan lebih robust dan memberikan pesan yang sesuai jika tidak ada bilangan yang dimasukkan.







