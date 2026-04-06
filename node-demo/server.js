const http = require('http');
const fs = require('fs');
const path = require('path');

const hostname = '0.0.0.0';
const port = 3000;

//fungsi untuk menentukan tipe file
function getContentType(filePath) {
  const ext = path.extname(filePath);
  const types = {
    '.html': 'text/html',
    '.css':  'text/css',
    '.js':   'application/javascript',
  };
  return types[ext] || 'text/plain';
}

const server = http.createServer((req, res) => {
  let filePath = req.url === '/' ? './public/index.html' : './public' + req.url;

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Halaman tidak ditemukan');
      return;
    }
    res.writeHead(200, { 'Content-Type': getContentType(filePath) });
    res.end(data);
  });
});

server.listen(port, hostname, () => {
  console.log(`Server kalkulator berjalan di http://localhost:${port}/`);
  console.log('Buka browser dan ketik: http://localhost:3000');
});