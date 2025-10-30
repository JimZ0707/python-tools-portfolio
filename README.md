<!-- 🐍 PYTHON TOOLS PORTFOLIO BY ZUHDI -->

![Python Tools Thumbnail](https://github.com/JimZ0707/python-tools-portfolio/blob/main/ChatGPT%20Image%20Oct%2030%2C%202025%2C%2012_55_22%20PM.png)

# 🧠 Custom Python Tools & Automation by Zuhdi

Halo! 👋  
Saya Zuhdi, seorang *freelancer Python developer* yang berfokus pada pembuatan **tools otomatisasi**, **analisis data sederhana**, dan **network utilities**.  
Repo ini berisi kumpulan script dan mini-project yang saya buat untuk kebutuhan nyata sehari-hari.  

---

## 🚀 Daftar Tools

### 🗂️ 1. File Renamer Tool
Script ini membantu mengganti nama banyak file sekaligus berdasarkan urutan atau pola tertentu.

**Fitur:**
- Rename otomatis berdasarkan urutan
- Aman (tidak menghapus file asli)
- Mudah digunakan bahkan untuk pemula

**Kode Contoh:**
```python
import os

folder = input("Masukkan folder path: ")
files = os.listdir(folder)

for i, filename in enumerate(files):
    ext = os.path.splitext(filename)[1]
    new_name = f"file_{i+1}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print("Proses rename selesai!")
```

**Cara Jalankan:**
```bash
python file_renamer.py
```

---

### 🌐 2. Simple Network Scanner *(Coming Soon)*
Tool sederhana untuk memindai perangkat aktif di jaringan lokal dengan cepat menggunakan metode `ping sweep`.

---

### 🧩 3. Log Analyzer *(Coming Soon)*
Script untuk membaca file log dan menampilkan statistik seperti jumlah error, waktu kejadian, atau pola teks tertentu.

---

## ⚙️ Teknologi yang Digunakan
- Python 3.x  
- Library bawaan (os, re, time, subprocess)  
- Beberapa tool akan menggunakan GUI via Tkinter  

---

## 💡 Tentang Saya
Saya sedang mengembangkan karier sebagai **freelancer Python dan Cybersecurity Enthusiast**,  
bertujuan membantu pengguna individu maupun bisnis kecil membuat tools yang efisien dan mudah digunakan.

🔗 Hubungi saya di Projects.co.id:  
👉 [Profil Freelancer Zuhdi](https://projects.co.id/public/browse_users/view/USERNAME_KAMU)

---

## 📜 Lisensi
Semua proyek di repo ini bisa dipelajari, dimodifikasi, atau digunakan kembali dengan mencantumkan kredit.  
Lisensi: **MIT License**

---

⭐ Jangan lupa klik **Star** kalau kamu suka proyek ini!  
Terima kasih sudah mampir 🙌
