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
![image](https://github.com/user-attachments/assets/e2738fa0-bf48-40ef-9421-e6bf1df6af4e)
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








