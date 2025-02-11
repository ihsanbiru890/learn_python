from colorama import Fore, Style

def usia_user(usia):
    """
    Mengembalikan kategori usia berdasarkan nilai yang diberikan.
    """
    if usia >= 60:
        return Fore.RED + 'Lansia\n(Usia lanjut, hati-hati dalam beraktivitas)' + Style.RESET_ALL
    elif usia >= 20:
        return Fore.GREEN + 'Dewasa\n(Usia produktif, jangan sia-siakan waktu)' + Style.RESET_ALL
    elif usia >= 12:
        return Fore.BLUE + 'Remaja\n(Usia yang penuh semangat, jangan lupa belajar)' + Style.RESET_ALL
    elif usia >= 6:
        return Fore.LIGHTYELLOW_EX + 'Anak-anak\n(Usia yang penuh keceriaan, jangan lupa bermain)' + Style.RESET_ALL
    elif usia >= 3:
        return Fore.MAGENTA + 'Balita\n(Usia yang penuh kepolosan, jangan lupa bermain)' + Style.RESET_ALL
    elif usia >= 1:
        return Fore.CYAN + 'Bayi\n(Usia yang penuh kelembutan, jangan lupa bermain)' + Style.RESET_ALL
    else:
        return None

def main():
    nama = input("Masukkan nama: ")
    attempts = 3  # Batasi jumlah percobaan
    
    while attempts > 0:
        try:
            usia = int(input(f"Hai {nama}, masukkan usiamu: "))
            kategori = usia_user(usia)
            if kategori:
                print(f"{nama}, di usia anda yang {usia} tahun, anda termasuk dalam kategori: {kategori}")
                break
            else:
                print(Fore.RED + "Usia yang dimasukkan tidak valid\n(Masukkan usia dengan benar)" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Usia yang dimasukkan tidak valid\n(Masukkan usia dengan angka)" + Style.RESET_ALL)
        
        attempts -= 1
        if attempts == 0:
            print(Fore.RED + "Kesempatan habis! Silakan coba lagi nanti." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
