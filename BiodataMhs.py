'''
belum belajar database, jadi data mahasiswa disimpan dalam list, tunggu update selanjutnya 😊😊'''

from colorama import init, Fore, Style
import time
init(autoreset=True)

def banner():
    print(Fore.MAGENTA + "="*50)
    print(Fore.YELLOW + "    🎓 CEK STATUS MAHASISWA 🎓")
    print(Fore.MAGENTA + "="*50)

def userAge(usia):
    kategori = {
        usia > 22: "Semester > 8 \n(Segera lah lulus atau D.O 😨)",
        usia == 22: "Semester 8 \n(Selesaikan skripsi agar lulus tepat waktu 🎓)",
        usia >= 21: "Semester 6 \n(Pasti sedang KKN 🏡)",
        usia >= 20: "Semester 4 \n(Belajar yang giat dan mulai magang 💼)",
        usia >= 19: "Semester 2 \n(Jangan menganggap diri masih SMA 🤓)"
    }
    return kategori.get(True, "Belum masuk kategori mahasiswa 👶")

def inputNama():
    return input(Fore.CYAN + "Masukkan nama anda: ")

def inputJurusan():
    name = inputNama()
    print(Fore.MAGENTA + "-"*50)
    jurusan_list = ["Teknik Informatika", "Sistem Informasi", "Teknik Elektro"]
    while True:
        jurusan = input(Fore.YELLOW + f"Halo {name} 😉, Masukkan jurusan anda: ")
        if jurusan in jurusan_list:
            return name, jurusan
        print(Fore.RED + "Jurusan tidak terdaftar! Coba lagi.")

def inputNim():
    name, jurusan = inputJurusan()
    print(Fore.MAGENTA + "-"*50)
    nim_list = ["16520299", "16520298", "16520297"]
    while True:
        nim = input(Fore.YELLOW + f"Halo {name} 😉, masukkan NIM anda: ")
        if nim in nim_list:
            return name, jurusan, nim
        print(Fore.RED + "NIM tidak terdaftar! Coba lagi.")

def main():
    banner()
    name, jurusan, nim = inputNim()
    print(Fore.MAGENTA + "-"*50)
    while True:
        try:
            usia = int(input(Fore.YELLOW + f"Halo {name} 😉, Masukkan usia anda: "))
            kategori = userAge(usia)
            print(Fore.MAGENTA + "-"*50)
            print(Fore.GREEN + f"Halo {name} 😊, anda berada di: \n{kategori}")
            print(Fore.MAGENTA + "-"*50)
            break
        except ValueError:
            print(Fore.RED + "Masukkan angka yang valid!")
        except KeyboardInterrupt:
            print(Fore.RED + "\nAnda keluar dari program!")
            break

if __name__ == "__main__":
    main()
