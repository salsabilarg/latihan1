from kalkulator import tambah, kurang, kali, bagi, persen, pangkat
from riwayat import simpan_riwayat, tampilkan_riwayat, hapus_riwayat
from tampilan import cetak_judul, cetak_menu, minta_angka, tampilkan_hasil

def jalankan():
    cetak_judul()
    print("  Selamat datang! Kalkulator ini menyimpan riwayat kamu.\n")

    while True:
        cetak_menu()
        pilihan = input("  Masukkan pilihan (0-8): ").strip()

        if pilihan == '0':
            print("\n  👋 Terima kasih! Sampai jumpa.\n")
            break

        elif pilihan in ('1', '2', '3', '4', '5', '6'):
            a = minta_angka("  Masukkan angka pertama  : ")
            b = minta_angka("  Masukkan angka kedua    : ")

            try:
                if pilihan == '1':
                    hasil = tambah(a, b)
                    ekspresi = f"{a} + {b}"
                elif pilihan == '2':
                    hasil = kurang(a, b)
                    ekspresi = f"{a} - {b}"
                elif pilihan == '3':
                    hasil = kali(a, b)
                    ekspresi = f"{a} × {b}"
                elif pilihan == '4':
                    hasil = bagi(a, b)
                    ekspresi = f"{a} ÷ {b}"
                elif pilihan == '5':
                    hasil = persen(a, b)
                    ekspresi = f"{a}% dari {b}"
                elif pilihan == '6':
                    hasil = pangkat(a, b)
                    ekspresi = f"{a} ^ {b}"

                if hasil == int(hasil):
                    hasil = int(hasil)

                tampilkan_hasil(ekspresi, hasil)
                simpan_riwayat(ekspresi, hasil)

            except ValueError as e:
                print(f"\n  ❌ Error: {e}")

        elif pilihan == '7':
            print("\n📋 Riwayat Perhitungan (terbaru di atas):")
            tampilkan_riwayat()

        elif pilihan == '8':
            hapus_riwayat()

        else:
            print("  ⚠️  Pilihan tidak valid. Masukkan angka 0-8.")

        input("\n  Tekan Enter untuk lanjut...")

if __name__ == '__main__':
    jalankan()