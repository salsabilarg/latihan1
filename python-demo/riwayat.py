import os
import json
from datetime import datetime

FILE_RIWAYAT = 'riwayat.json'

def muat_riwayat():
    """Membaca riwayat dari file JSON"""
    if not os.path.exists(FILE_RIWAYAT):
        return []
    with open(FILE_RIWAYAT, 'r') as f:
        return json.load(f)

def simpan_riwayat(ekspresi, hasil):
    """Menyimpan satu perhitungan ke file JSON"""
    data = muat_riwayat()
    entri = {
        'ekspresi': ekspresi,
        'hasil': hasil,
        'waktu': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    data.append(entri)
    if len(data) > 10:
        data = data[-10:]
    with open(FILE_RIWAYAT, 'w') as f:
        json.dump(data, f, indent=2)

def tampilkan_riwayat():
    """Menampilkan semua riwayat perhitungan"""
    data = muat_riwayat()
    if not data:
        print("  (Belum ada riwayat)")
        return
    for i, entri in enumerate(reversed(data), 1):
        print(f"  {i}. {entri['ekspresi']} = {entri['hasil']}  [{entri['waktu']}]")

def hapus_riwayat():
    """Menghapus semua riwayat"""
    if os.path.exists(FILE_RIWAYAT):
        os.remove(FILE_RIWAYAT)
    print("  Riwayat berhasil dihapus.")