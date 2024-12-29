# Konverter Data CSV ke Excel

Skrip Python ini berfungsi untuk mengonversi file CSV yang berisi data produk dan komisi menjadi file Excel yang terkonsolidasi. Dirancang untuk memproses beberapa file CSV dari direktori dasar dan menggabungkannya menjadi satu spreadsheet Excel yang terorganisir dengan tetap menjaga integritas dan struktur data.

## Fitur Utama

Konverter ini menyediakan kemampuan berikut:

- Memproses beberapa file CSV sekaligus dari direktori yang ditentukan
- Membuat direktori output secara otomatis
- Menjaga konsistensi format data
- Memberikan penomoran urut secara otomatis
- Menangani file dengan encoding UTF-8 dengan BOM
- Menghasilkan file Excel terkonsolidasi dengan kolom yang terorganisir
- Menampilkan kemajuan proses konversi secara real-time

## Persyaratan Sistem

Sebelum menggunakan skrip ini, pastikan Anda telah menginstal:

- Python 3.6 atau versi yang lebih baru
- Paket Python yang diperlukan:
  ```bash
  pip install pandas
  openpyxl
  ```

## Struktur Direktori

Skrip ini memerlukan struktur direktori sebagai berikut:

```
folder_project_anda/
│
├── basedata/           # Tempat menyimpan file CSV
│   ├── file1.csv
│   ├── file2.csv
│   └── ...
│
├── outputs/           # Dibuat secara otomatis
│   └── datakomisi.xlsx
│
└── converter.py       # Skrip utama
```

## Format File CSV

File CSV Anda harus memiliki kolom-kolom berikut:

- ID Produk
- Nama Produk
- Harga
- Penjualan
- Nama Toko
- Komisi hingga
- Komisi
- Link Produk
- Link Komisi Ekstra

## Cara Instalasi

1. Buat direktori baru untuk project Anda
2. Salin skrip ke dalam file bernama `converter.py`
3. Buat folder bernama `basedata` di direktori yang sama
4. Letakkan file-file CSV Anda di dalam folder `basedata`

## Cara Penggunaan

1. Pastikan file CSV Anda sudah ditempatkan di folder `basedata`
2. Buka terminal atau command prompt
3. Arahkan ke direktori project
4. Jalankan skrip dengan perintah:
   ```bash
   python converter.py
   ```

Skrip akan melakukan:
1. Membuat folder `outputs` jika belum ada
2. Memproses semua file CSV di folder `basedata`
3. Menghasilkan file Excel terkonsolidasi di `outputs/datakomisi.xlsx`
4. Menampilkan update progres di konsol

## Contoh Output

File Excel yang dihasilkan akan memiliki kolom-kolom berikut:

- Number (Nomor urut yang dibuat otomatis)
- ID Produk
- Nama Produk
- Harga
- Penjualan
- Nama Toko
- Komisi hingga
- Komisi
- Link Produk
- Link Komisi Ekstra

## Penyelesaian Masalah

Masalah umum dan solusinya:

1. **FileNotFoundError**: Pastikan folder `basedata` ada dan berisi file CSV
2. **UnicodeDecodeError**: Pastikan file CSV menggunakan encoding UTF-8
3. **Permission Error**: Periksa apakah Anda memiliki izin menulis di direktori project
4. **Output Kosong**: Verifikasi bahwa file CSV memiliki header kolom yang benar dan berisi data

## Penanganan Error

Skrip ini mencakup penanganan error dasar untuk:
- Direktori yang tidak ditemukan
- Error saat membaca file
- Masalah dalam pemrosesan data

Jika Anda mengalami error, periksa output konsol untuk pesan error spesifik.

## Kustomisasi

Anda dapat memodifikasi variabel berikut dalam skrip untuk menyesuaikan perilakunya:

- `base_folder`: Mengubah nama direktori input (default: "basedata")
- `output_folder`: Mengubah nama direktori output (default: "outputs")
- `output_excel`: Mengubah nama dan lokasi file output (default: "outputs/datakomisi.xlsx")

## Kontribusi

Silakan fork repository ini dan ajukan pull request untuk perbaikan atau peningkatan.

## Lisensi

Project ini tersedia untuk digunakan dan dimodifikasi secara bebas.