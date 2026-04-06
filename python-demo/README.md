# 🧮 Kalkulator Terminal (Python)

Aplikasi kalkulator interaktif yang berjalan di terminal, dibuat menggunakan Python 3.
Riwayat perhitungan disimpan otomatis ke file JSON.

## Cara Menjalankan

1. Pastikan Python 3 sudah terinstall
2. (Opsional) Aktifkan virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Jalankan program:
   ```
   python3 main.py
   ```

## Fitur
- Operasi: tambah, kurang, kali, bagi, persen, pangkat
- Riwayat otomatis disimpan ke file `riwayat.json`
- Bisa melihat dan menghapus riwayat
- Validasi input (tidak crash jika salah ketik)

## Struktur File
```
python-demo/
├── main.py        → File utama, jalankan ini
├── kalkulator.py  → Fungsi-fungsi perhitungan
├── tampilan.py    → Fungsi tampilan di terminal
├── riwayat.py     → Menyimpan/membaca riwayat (file JSON)
└── README.md      → Dokumentasi ini
```