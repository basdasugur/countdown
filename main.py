import time # Zamanı Kontrol Etmek İçin

number = int(input("Roket Kaçtan Geriye Saysın ? : "))

print(" --- Geri Sayım Başlıyor --- ")

for i in range(number, 0 ,-1):
    print(i)
    time.sleep(1)
print("Kalkış")
