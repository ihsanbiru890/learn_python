import customtkinter as ctk
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as messagebox

'''---------------------Database Connection-------------------------'''

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="login_page"
    )
    cursor = conn.cursor()
except Error as e:
    print(f"Error: {e}")
    exit()

'''---------------------Aplikasi GUI-------------------------'''

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Project 1 - Login Page")
app.geometry("550x500")


'''---------------------Fungsi Login & Register-------------------------'''

def login_user():
    username = entry_username_user.get()
    email = entry_email_user.get()
    password = entry_password_user.get()

    query = "SELECT * FROM users WHERE username=%s AND email=%s AND password=%s"
    cursor.execute(query, (username, email, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Berhasil", "Selamat datang, User!")
        print("login berhasil")
    elif not username or not email or not password:
        messagebox.showwarning("Register Gagal", "Isi semua form login!")
    else:
        messagebox.showerror("Login Gagal", "Username, Email, atau Password salah!")
        print("login gagal")


def login_admin():
    username = entry_username_admin.get()
    email = entry_email_admin.get()
    password = entry_password_admin.get()

    query = "SELECT * FROM admins WHERE username=%s AND email=%s AND password=%s"
    cursor.execute(query, (username, email, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login Berhasil", "Selamat datang, Admin!")
    elif not username or not email or not password:
        messagebox.showwarning("Register Gagal", "Isi semua form login!")
    else:
        messagebox.showerror("Login Gagal", "Username, Email, atau Password salah!")


def register_user():
    username = entry_username_register.get()
    email = entry_email_register.get()
    password = entry_password_register.get()

    cursor.execute("SELECT * FROM users WHERE username=%s OR email=%s", (username, email))
    if cursor.fetchone():
        messagebox.showwarning("Register Gagal", "Username atau Email sudah digunakan!")
        return
    elif not username or not email or not password:
        messagebox.showwarning("Register Gagal", "Isi semua form register!")
        return
    
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()

    messagebox.showinfo("Register Berhasil", "Akun berhasil dibuat! Silakan login.")

'''---------------------Tab View-------------------------'''

tabView = ctk.CTkTabview(app, width=300, height=400, fg_color="#2D336B", corner_radius=30)
tabView.pack(padx=20, pady=(20, 10))
tabView.pack_propagate(False)

tabView.add("user")
tabView.add("admin")
tabView.add("register")

tabView.set("user")

'''---------------------User Login-------------------------'''

custom_font = ctk.CTkFont(family="Comic Sans MS", size=20, weight="bold")

label_user = ctk.CTkLabel(tabView.tab("user"), text="User Login", font=custom_font)
label_user.pack(pady=(10, 10))

entry_username_user = ctk.CTkEntry(tabView.tab("user"), width=250, height=30, placeholder_text="Username")
entry_username_user.pack(pady=(20, 10))

entry_email_user = ctk.CTkEntry(tabView.tab("user"), width=250, height=30, placeholder_text="Email")
entry_email_user.pack(pady=10)

entry_password_user = ctk.CTkEntry(tabView.tab("user"), width=250, height=30, placeholder_text="Password", show="*")
entry_password_user.pack(pady=10)

button_login_user = ctk.CTkButton(tabView.tab("user"), width=250, height=40, text="Login", command=login_user)
button_login_user.place(relx=0.5, rely=0.9, anchor="center")

'''---------------------Admin Login-------------------------'''

label_admin = ctk.CTkLabel(tabView.tab("admin"), text="Admin Login", font=custom_font)
label_admin.pack(pady=(10, 10))

entry_username_admin = ctk.CTkEntry(tabView.tab("admin"), width=250, height=30, placeholder_text="Username")
entry_username_admin.pack(pady=(20, 10))

entry_email_admin = ctk.CTkEntry(tabView.tab("admin"), width=250, height=30, placeholder_text="Email")
entry_email_admin.pack(pady=10)

entry_password_admin = ctk.CTkEntry(tabView.tab("admin"), width=250, height=30, placeholder_text="Password", show="*")
entry_password_admin.pack(pady=10)

button_login_admin = ctk.CTkButton(tabView.tab("admin"), width=250, height=40, text="Login", command=login_admin)
button_login_admin.place(relx=0.5, rely=0.9, anchor="center")

'''---------------------Register User-------------------------'''

label_register = ctk.CTkLabel(tabView.tab("register"), text="Register User", font=custom_font)
label_register.pack(pady=(10, 10))

entry_username_register = ctk.CTkEntry(tabView.tab("register"), width=250, height=30, placeholder_text="Username")
entry_username_register.pack(pady=(20, 10))

entry_email_register = ctk.CTkEntry(tabView.tab("register"), width=250, height=30, placeholder_text="Email")
entry_email_register.pack(pady=10)

entry_password_register = ctk.CTkEntry(tabView.tab("register"), width=250, height=30, placeholder_text="Password", show="*")
entry_password_register.pack(pady=10)

button_register = ctk.CTkButton(tabView.tab("register"), width=250, height=40, text="Register", command=register_user)
button_register.place(relx=0.5, rely=0.9, anchor="center")

app.mainloop()
