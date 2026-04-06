# 🧮 Kalkulator Web (Node.js)

Aplikasi kalkulator berbasis web yang berjalan menggunakan Node.js murni (tanpa framework tambahan).

## Cara Menjalankan

1. Pastikan Node.js sudah terinstall
2. Jalankan server:
   ```
   node server.js
   ```
3. Buka browser dan akses: `http://localhost:3000`

## Fitur
- Operasi dasar: tambah, kurang, kali, bagi, persen
- Riwayat perhitungan (5 terakhir)
- Tombol hapus satu karakter (⌫) dan hapus semua (AC)
- Bisa digunakan via keyboard (tekan Enter untuk menghitung)

## Struktur File
```
node-demo/
├── server.js        → Server utama Node.js
├── package.json     → Info proyek
├── README.md        → Dokumentasi ini
└── public/
    ├── index.html   → Tampilan halaman web
    ├── style.css    → Desain/tampilan kalkulator
    └── kalkulator.js → Logika perhitungan
```