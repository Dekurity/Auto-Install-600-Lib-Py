# 📦 Instalasi 600+ Library CLI untuk Termux/Linux

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) 

📜 Proyek ini bertujuan untuk mempermudah instalasi lebih dari 600 library Python CLI untuk Termux/Linux. Dengan menggunakan `installlibpy.py`, Anda dapat menginstal berbagai library yang bermanfaat untuk berbagai keperluan seperti peningkatan terminal, pentesting, web scraping, automasi, jaringan, pemrosesan file, dan banyak lagi.

## 📂 Daftar Isi

- [Fitur](#✨-fitur)
- [Persyaratan](#📋-persyaratan)
- [Cara Instalasi](#🛠️-cara-instalasi)
- [Cara Penggunaan](#🚀-cara-penggunaan)
- [Daftar Library](#📚-daftar-library)
- [Kontributor](#👥-kontributor)

## ✨ Fitur

- Instalasi lebih dari 600 library Python CLI
- Proses instalasi otomatis dengan tampilan progres
- Deteksi otomatis library yang sudah terinstal

## 📋 Persyaratan

- Python 3.x
- Pip (Python package installer)

## 🛠️ Cara Instalasi

1. Clone repositori ini:

    ```sh
    git clone https://github.com/Dekurity/Auto-Install-600+-Lib-Py.git
    cd Auto-Install-600+-Lib-Py
    ```

2. Pastikan Anda memiliki `pip` dan `virtualenv` terinstal. Jika belum, Anda dapat menginstalnya dengan:

    ```sh
    sudo apt-get install python3-pip
    pip3 install virtualenv
    ```

3. Buat dan aktifkan virtual environment:

    ```sh
    virtualenv venv
    source venv/bin/activate
    ```

4. Install semua dependensi yang diperlukan:

    ```sh
    pip install rich importlib
    ```

## 🚀 Cara Penggunaan

1. Jalankan skrip `installlibpy.py` dengan Python 3:

    ```sh
    python3 installlibpy.py
    ```

2. Skrip akan mulai menginstal library yang tercantum dalam daftar. Selama proses, Anda akan melihat progres instalasi di terminal.

## 📚 Daftar Library

Daftar lengkap library yang akan diinstal dapat dilihat di dalam file `installlibpy.py`. Library tersebut mencakup kategori berikut:

- **Terminal & CLI Enhancement**
- **Pentesting & Cybersecurity**
- **Web Scraping & Automation**
- **Networking & API Tools**
- **Database & Storage**
- **File Processing & Archive**
- **Machine Learning & Data Science**
- **Cryptography & Security**
- **System & Process Management**
- **Development & Testing Tools**
- **GUI & Multimedia**
- **IoT & Hardware**
- **Natural Language Processing**
- **API Development**
- **Miscellaneous Utilities**

## 👥 Kontributor

- [Dekurity](https://github.com/Dekurity)

Nikmati kemudahan instalasi dan semoga proyek ini bermanfaat bagi Anda! 🎉
