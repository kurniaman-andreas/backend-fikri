# backend-fikri

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
   python -m venv venv
   source venv/bin/activate # Untuk Linux/Mac
   venv\Scripts\activate # Untuk Windows
   Sesuaikan pengaturan database di file settings.py proyek Anda.

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Akses Aplikasi Buka browser Anda dan akses: http://127.0.0.1:8000/api/data
