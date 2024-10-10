import math

def luas_lingkaran(r):
    return math.pi * r * r

def deret_aritmatika(n, a, b):
    return 0.5 * n * (2*a + (n-1)*b)

def deret_geometri(a, r, n):
    return a * (r**(n-1))

def debit(v, t):
    return v / t

def volume_balok(p, l, t):
    return p * l * t

def luas_permukaan_bola(r):
    return 4 * math.pi * r * r

def energi_potensial(m, h, g=10):
    return m * g * h

def energi_kinetik(m, v):
    return 0.5 * m * v * v

def tegangan_listrik(i, r):
    return i * r

def frekuensi(n, t):
    return n / t

def periode(t, n):
    return t / n

def cepat_rambat_gelombang(s, t):
    return s / t

def main_menu():
    print("\nMenu Rumus Matematika dan Fisika:")
    print("1. Luas Lingkaran")
    print("2. Jumlah Deret Aritmatika")
    print("3. Deret Geometri")
    print("4. Debit")
    print("5. Volume Balok")
    print("6. Luas Permukaan Bola")
    print("7. Energi Potensial")
    print("8. Energi Kinetik")
    print("9. Tegangan Listrik")
    print("10. Frekuensi")
    print("11. Periode")
    print("12. Cepat Rambat Gelombang")
    print("0. Keluar")

def main():
    while True:
        main_menu()
        pilihan = input("Pilih nomor rumus (0-12): ")

        if pilihan == "0":
            print("Thank you for using this program")
            break
        elif pilihan == "1":
            r = float(input("Masukkan jari-jari lingkaran (cm): "))
            print(f"Luas lingkaran: {luas_lingkaran(r):.2f} cm²")
        elif pilihan == "2":
            n = int(input("Masukkan banyaknya suku: "))
            a = float(input("Masukkan suku pertama: "))
            b = float(input("Masukkan beda: "))
            print(f"Jumlah deret aritmatika: {deret_aritmatika(n, a, b):.2f}")
        elif pilihan == "3":
            a = float(input("Masukkan suku pertama: "))
            r = float(input("Masukkan rasio: "))
            n = int(input("Masukkan nilai n: "))
            print(f"Suku ke-{n} dari deret geometri: {deret_geometri(a, r, n):.2f}")
        elif pilihan == "4":
            v = float(input("Masukkan volume (cm³): "))
            t = float(input("Masukkan waktu (detik): "))
            print(f"Debit: {debit(v, t):.2f} cm³/detik")
        elif pilihan == "5":
            p = float(input("Masukkan panjang balok (cm): "))
            l = float(input("Masukkan lebar balok (cm): "))
            t = float(input("Masukkan tinggi balok (cm): "))
            print(f"Volume balok: {volume_balok(p, l, t):.2f} cm³")
        elif pilihan == "6":
            r = float(input("Masukkan jari-jari bola (cm): "))
            print(f"Luas permukaan bola: {luas_permukaan_bola(r):.2f} cm²")
        elif pilihan == "7":
            m = float(input("Masukkan massa (kg): "))
            h = float(input("Masukkan ketinggian (m): "))
            print(f"Energi potensial: {energi_potensial(m, h):.2f} Joule")
        elif pilihan == "8":
            m = float(input("Masukkan massa (kg): "))
            v = float(input("Masukkan kecepatan (m/s): "))
            print(f"Energi kinetik: {energi_kinetik(m, v):.2f} Joule")
        elif pilihan == "9":
            i = float(input("Masukkan arus listrik (Ampere): "))
            r = float(input("Masukkan hambatan (Ohm): "))
            print(f"Tegangan listrik: {tegangan_listrik(i, r):.2f} Volt")
        elif pilihan == "10":
            n = float(input("Masukkan jumlah getaran: "))
            t = float(input("Masukkan waktu (detik): "))
            print(f"Frekuensi: {frekuensi(n, t):.2f} Hz")
        elif pilihan == "11":
            t = float(input("Masukkan waktu (detik): "))
            n = float(input("Masukkan jumlah getaran: "))
            print(f"Periode: {periode(t, n):.2f} detik")
        elif pilihan == "12":
            s = float(input("Masukkan jarak (meter): "))
            t = float(input("Masukkan waktu (detik): "))
            print(f"Cepat rambat gelombang: {cepat_rambat_gelombang(s, t):.2f} m/s")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()