"""
📚 LIBRARY MANAGER - Project Python Pertama
Oleh: Arip
SMP 2 Kota Kediri

Fungsi: Menyimpan daftar buku ke file JSON, bisa tambah, lihat, cari, Tandai, dan hapus.
"""

import json
import os

DATA_FILE = "library.json"

# Fungsi dasar ya man teman!
def load_books():
  """Memuat data buku dari file library.json.
     kalau file belum ada, otomatis bikin list kosong."""
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE), "r") as file:
      return json.load(file)
  return []

def save_books(books):
  """Menyimpan data buku ke file library.json dengan format rapi."""
  with open(DATA_FILE), "w") as file:
    json.dump(books, file, indent=4)

# Fitur aplikasinya ini anjg

def tambah_buku(books):
  """Menambahkan 1 bukubaru ke dalam daftar."""
  print("\n--- 📖 TAMBAH BUKU BARU ---")
  judul = input("Masukkan judul bukunya guys: ").strip()
  penulis = input("Masukkan nama penulis guys: ").strip()
  tahun = input("Masukkan tahun terbitnya buku guys: ").strip()

# data buju ke dictionary asu
buku_baru = {
  "id": len(books) + 1,
  "judul": judul,
  "penulis": tahun,
  "sudah_dibaca": False
}

books.append(buku_baru)
save_books(books)
print("f"✅ Buku '{judul}' berhasil ditambahkan!")

def lihat_semua_buku(books):
    """Menampilkan seluruh daftar buku yang tersimpan."""
    print("\n--- 📚 DAFTAR SEMUA BUKU ---")
    if not books:
        print("📭 Belum ada buku di perpustakaan.")
        return

    for buku in books:
        status = "✅ Selesai" if buku["sudah_dibaca"] else "📖 Belum dibaca"
        print(f"[{buku['id']}] {buku['judul']} - {buku['penulis']} ({buku['tahun']}) | {status}")

def cari_buku(books):
    """Mencari buku berdasarkan judul atau penulis (tidak case sensitive)."""
    print("\n--- 🔍 CARI BUKU ---")
    keyword = input("Masukkan judul atau penulis: ").strip().lower()
    
    hasil = []
    for buku in books:
        if keyword in buku["judul"].lower() or keyword in buku["penulis"].lower():
            hasil.append(buku)

    if hasil:
        print(f"\nDitemukan {len(hasil)} buku:")
        for buku in hasil:
            print(f"- {buku['judul']} oleh {buku['penulis']} ({buku['tahun']})")
    else:
        print("❌ Buku tidak ditemukan.")

def tandai_selesai(books):
    """Menandai buku yang sudah selesai dibaca berdasarkan ID."""
    lihat_semua_buku(books)
    try:
        id_buku = int(input("\nMasukkan ID buku yang sudah selesai dibaca: "))
        for buku in books:
            if buku["id"] == id_buku:
                buku["sudah_dibaca"] = True
                save_books(books)
                print(f"✅ '{buku['judul']}' telah ditandai selesai!")
                return
        print("❌ ID buku tidak ditemukan.")
    except ValueError:
        print("❌ Masukkan angka yang valid untuk ID.")

def hapus_buku(books):
    """Menghapus buku berdasarkan ID."""
    lihat_semua_buku(books)
    try:
        id_buku = int(input("\nMasukkan ID buku yang ingin dihapus: "))
        for i, buku in enumerate(books):
            if buku["id"] == id_buku:
                judul_terhapus = books.pop(i)
                save_books(books)
                print(f"🗑️ Buku '{judul_terhapus['judul']}' berhasil dihapus.")
                return
        print("❌ ID buku tidak ditemukan.")
    except ValueError:
        print("❌ Masukkan angka yang valid untuk ID.")

def main():
    """Fungsi utama yang menjalankan program."""
    books = load_books()  # Muat data saat program dimulai

    while True:
        print("\n" + "="*40)
        print("📚 SELAMAT DATANG DI LIBRARY MANAGER")
        print("="*40)
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Cari Buku")
        print("4. Tandai Buku Selesai Dibaca")
        print("5. Hapus Buku")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menunya asu (0-5): ")

        if pilihan == "1":
            tambah_buku(books)
        elif pilihan == "2":
            lihat_semua_buku(books)
        elif pilihan == "3":
            cari_buku(books)
        elif pilihan == "4":
            tandai_selesai(books)
        elif pilihan == "5":
            hapus_buku(books)
        elif pilihan == "0":
            print("\n👋 Terima kasih sudah menggunakan Library Manager. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
