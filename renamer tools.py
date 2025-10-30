import os

folder = input("Masukkan folder path: ")
files = os.listdir(folder)

for i, filename in enumerate(files):
    ext = os.path.splitext(filename)[1]
    new_name = f"file_{i+1}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print("Proses rename selesai!")
