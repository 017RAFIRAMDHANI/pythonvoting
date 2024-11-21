paslon = {"ANIS MUHAIMIN": 0, "PRABOWO GIBRAN": 0, "GANJAR MAHFUD": 0}
ga_valid = 0
total_suara = 0

print("SELAMAT DATANG DI SISTEM PEMILIHAN CALON PRESIDEN RI PERIODE(2024-2029) ")
print("SILAHKAN PILIH SALAH SATU PASLON BERIKUT:")
print("1. ANIS MUHAIMIN")
print("2. PRABOWO GIBRAN")
print("3. GANJAR MAHFUD")
        
while True:
   pilihan = input("Masukkan nomor pilihan Anda (1-3) atau 0 untuk selesai: ")
        
   if pilihan == '0':
      break
   elif pilihan == '1':
      paslon["ANIS MUHAIMIN"] += 1
      total_suara += 1
   elif pilihan == '2':
      paslon["PRABOWO GIBRAN"] += 1
      total_suara += 1
   elif pilihan == '3':
      paslon["GANJAR MAHFUD"] += 1
      total_suara += 1
   else:
      print("Pilihan tidak valid. Silakan masukkan nomor sesuai paslon yang akan di pilih {1-3} .")
      ga_valid += 1
      
print("\nHasil polling:")
for kandidat, jumlah in paslon.items():
   percentage = (jumlah / total_suara) * 100 if total_suara > 0 else 0
   print(f"{kandidat}\t\t: {jumlah} suara ({percentage:.2f}%)")
    
print(f"\nSuara tidak valid: {ga_valid} suara")
print(f"Total suara: {total_suara}")

