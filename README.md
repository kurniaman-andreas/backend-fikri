# backend-fikri

![Alt text](/fikri_project/static/images/screenshoot-api.png)

## Prerequisites

Pastikan Anda memiliki perangkat lunak berikut terinstal:

- Python 3.x
- PostgreSQL (atau database lain yang Anda gunakan)
- Git

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal proyek ini:

1. **Clone Repositori**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. **Buat Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Sesuaikan Pengaturan Database : Buka file settings.py dan sesuaikan pengaturan database sesuai kebutuhan Anda.**

4. **Instal Dependensi**

   ```bash
   pip install -r requirements.txt
   ```

5. **Migrate Database**

   ```bash
   python manage.py migrate
   ```

6. **Jalankan Server**

   ```bash
   python manage.py runserver
   ```

7. **Akses Aplikasi : Buka browser Anda dan akses: http://127.0.0.1:8000/api/data**
