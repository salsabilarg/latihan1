def cetak_garis(karakter='─', panjang=40):
    print(karakter * panjang)

def cetak_judul():
    cetak_garis('═')
    print("        🧮  KALKULATOR TERMINAL  🧮")
    print("          Dibuat dengan Python 3")
    cetak_garis('═')

def cetak_menu():
    print("\n📌 Pilih operasi:")
    print("  1. ➕  Tambah")
    print("  2. ➖  Kurang")
    print("  3. ✖️   Kali")
    print("  4. ➗  Bagi")
    print("  5. 🔢  Persen (a% dari b)")
    print("  6. 🔺  Pangkat (a^b)")
    cetak_garis()
    print("  7. 📋  Lihat riwayat")
    print("  8. 🗑️   Hapus riwayat")
    print("  0. 🚪  Keluar")
    cetak_garis()

def minta_angka(pesan):
    """Meminta input angka dari pengguna, terus meminta jika salah"""
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print(" Itu bukan angka! Coba lagi.")

def tampilkan_hasil(ekspresi, hasil):
    print(f"\n  Hasil: {ekspresi} = {hasil}")