let riwayat = [];

function tambahKarakter(karakter) {
  const layar = document.getElementById('layar');
  if (layar.value === '0' && karakter !== '.') {
    layar.value = karakter;
  } else {
    layar.value += karakter;
  }
}

function hitung() {
  const layar = document.getElementById('layar');
  const ekspresi = layar.value;

  if (!ekspresi) return;

  try {
    const ekspresiJS = ekspresi.replace(/÷/g, '/').replace(/×/g, '*');
    const hasil = Function('"use strict"; return (' + ekspresiJS + ')')();

    simpanRiwayat(ekspresi + ' = ' + hasil);

    layar.value = hasil;
  } catch (e) {
    layar.value = 'Error!';
    setTimeout(() => layar.value = '', 1500);
  }
}

function hapusSemua() {
  document.getElementById('layar').value = '';
}

function hapusSatu() {
  const layar = document.getElementById('layar');
  layar.value = layar.value.slice(0, -1);
}

function simpanRiwayat(teks) {
  riwayat.unshift(teks); 
  if (riwayat.length > 5) riwayat.pop(); 

  const daftar = document.getElementById('daftar-riwayat');
  daftar.innerHTML = riwayat.map(r => `<li>${r}</li>`).join('');
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') hitung();
});