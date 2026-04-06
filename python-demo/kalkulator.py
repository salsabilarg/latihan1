def tambah(a, b):
    """Menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka. Akan error jika pembagi = 0"""
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan angka 0!")
    return a / b

def persen(a, b):
    """Menghitung berapa persen a dari b"""
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan angka 0!")
    return (a / b) * 100

def pangkat(a, b):
    """Menghitung a pangkat b"""
    return a ** b