a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka: "))
c = int(input("Masukkan angka: "))

if a > b:
    if a > c:
        terbesar = a    
    else:
        terbesar = c
else:
    if b > c:
        terbesar = b
    else:      
       terbesar = c 
print(f"Bilangan terbesar adalah {terbesar}")