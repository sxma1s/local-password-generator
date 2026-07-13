import secrets
import string
import math
import tkinter as tk
from tkinter import messagebox, ttk

# --- Lista polskich słów do generatora passphrase ---
SLOWA = [
    "dom", "kot", "pies", "drzewo", "okno", "brama", "rzeka", "gora", "las", "droga",
    "ksiazka", "zegarek", "krzeslo", "stol", "lampa", "samochod", "rower", "niebo", "slonce", "morze",
    "chleb", "woda", "kawa", "herbata", "jablko", "kwiat", "ptak", "ryba", "kamien", "piasek",
    "trawa", "ziemia", "chmura", "wiatr", "deszcz", "snieg", "ogien", "cieplo", "zimno", "noc"
]

# --- Kolory dla motywów ---
MOTYWY = {
    "dark": {"bg": "#2b2b2b", "fg": "#ffffff", "accent": "#3c3f41", "btn": "#2d7d46", "tab_text": "#ffffff"},
    "light": {"bg": "#f0f0f0", "fg": "#000000", "accent": "#ffffff", "btn": "#4caf50", "tab_text": "#000000"}
}
obecny_motyw = "dark"

def przelacz_motyw():
    global obecny_motyw
    obecny_motyw = "light" if obecny_motyw == "dark" else "dark"
    m = MOTYWY[obecny_motyw]
    
    # Aktualizacja okna głównego i elementów
    root.configure(bg=m["bg"])
    btn_motyw.config(text="🌙 Tryb Ciemny" if obecny_motyw == "light" else "☀️ Tryb Jasny", bg=m["accent"], fg=m["fg"])
    
    # Styl zakładek
    style.configure('TNotebook', background=m["bg"])
    style.configure('TNotebook.Tab', background=m["accent"], foreground=m["tab_text"])
    style.map('TNotebook.Tab', background=[('selected', m["bg"])], foreground=[('selected', m["btn"])])
    
    # Elementy Zakładki 1
    tab1.configure(bg=m["bg"])
    lbl_dl.configure(bg=m["bg"], fg=m["fg"])
    suwak_dlugosci.configure(bg=m["bg"], fg=m["fg"])
    for cb in chk_buttons_tab1:
        cb.configure(bg=m["bg"], fg=m["fg"], selectcolor=m["accent"])
    btn_gen1.configure(bg=m["btn"], fg="#ffffff")
    ramka_hasla.configure(bg=m["bg"])
    pole_hasla.configure(bg=m["accent"], fg=m["fg"], insertbackground=m["fg"])
    btn_oko.configure(bg=m["accent"], fg=m["fg"])
    btn_kopiuj1.configure(bg=m["accent"], fg=m["fg"])
    etykieta_czasu.configure(bg=m["bg"], fg=m["fg"])
    
    # Elementy Zakładki 2
    tab2.configure(bg=m["bg"])
    lbl_sl.configure(bg=m["bg"], fg=m["fg"])
    suwak_slow.configure(bg=m["bg"], fg=m["fg"])
    btn_gen2.configure(bg=m["btn"], fg="#ffffff")
    ramka_pass.configure(bg=m["bg"])
    pole_pass.configure(bg=m["accent"], fg=m["fg"], insertbackground=m["fg"])
    btn_kopiuj2.configure(bg=m["accent"], fg=m["fg"])
    etykieta_czasu_pass.configure(bg=m["bg"], fg=m["fg"])

def kopiuj_efekt(przycisk, pole):
    haslo = pole.get()
    if haslo:
        root.clipboard_clear()
        root.clipboard_append(haslo)
        
        # Zmiana tekstu przycisku bez wyskakującego okna
        stary_tekst = przycisk.cget("text")
        przycisk.config(text="✓ Skopiowano")
        
        # Przywrócenie starego tekstu po 1.5 sekundy
        root.after(1500, lambda: przycisk.config(text=stary_tekst))

# --- Funkcje dla Zakładki 1 (Zwykłe Hasło) ---
def przelacz_widocznosc_hasla():
    if pole_hasla.cget('show') == '':
        pole_hasla.config(show='*')
        btn_oko.config(text="👁")
    else:
        pole_hasla.config(show='')
        btn_oko.config(text="🔒")

def generuj_standardowe():
    dlugosc = int(suwak_dlugosci.get())
    pula = ""
    if var_wielkie.get():    pula += string.ascii_uppercase
    if var_male.get():       pula += string.ascii_lowercase
    if var_cyfry.get():      pula += string.digits
    if var_specjalne.get():  pula += string.punctuation
    
    if var_wyklucz.get():
        pula = "".join(z for z in pula if z not in "l1Io0O")
    
    if not pula:
        messagebox.showerror("Błąd", "Wybierz przynajmniej jeden zestaw znaków!")
        return

    haslo = "".join(secrets.choice(pula) for _ in range(dlugosc))
    kombinacje = len(pula) ** dlugosc
    sekundy = kombinacje / 100_000_000_000
    
    if sekundy < 1: czas = "Natychmiast"
    elif sekundy < 3600: czas = f"{sekundy/60:.1f} min"
    elif sekundy < 86400: czas = f"{sekundy/3600:.1f} godz."
    elif sekundy < 31536000: czas = f"{sekundy/86400:.0f} dni"
    else: czas = f"{sekundy/31536000:,.0f} lat"

    pole_hasla.config(show='')
    btn_oko.config(text="🔒")
    pole_hasla.delete(0, tk.END)
    pole_hasla.insert(0, haslo)
    etykieta_czasu.config(text=f"Szacowany czas złamania: {czas}")

# --- Funkcje dla Zakładki 2 (Passphrase) ---
def generuj_passphrase():
    ile_slow = int(suwak_slow.get())
    wylosowane = [secrets.choice(SLOWA) for _ in range(ile_slow)]
    haslo = "-".join(wylosowane)
    
    kombinacje = len(SLOWA) ** ile_slow
    sekundy = kombinacje / 100_000_000_000
    
    if sekundy < 1: czas = "Natychmiast"
    elif sekundy < 3600: czas = f"{sekundy/60:.1f} min"
    elif sekundy < 86400: czas = f"{sekundy/3600:.1f} godz."
    elif sekundy < 31536000: czas = f"{sekundy/86400:.0f} dni"
    else: czas = f"{sekundy/31536000:,.0f} lat"
    
    pole_pass.delete(0, tk.END)
    pole_pass.insert(0, haslo)
    etykieta_czasu_pass.config(text=f"Szacowany czas złamania: {czas}")

# --- Budowanie Interfejsu ---
m = MOTYWY[obecny_motyw]
root = tk.Tk()
root.title("Lokalny Generator Haseł v1.1.0")
root.geometry("450x500")
root.configure(bg=m["bg"])

# Górny przycisk zmiany motywu
btn_motyw = tk.Button(root, text="☀️ Tryb Jasny", command=przelacz_motyw, bg=m["accent"], fg=m["fg"], relief="flat", padx=10)
btn_motyw.pack(anchor="ne", padx=10, pady=5)

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook', background=m["bg"], borderwidth=0)
style.configure('TNotebook.Tab', background=m["accent"], foreground=m["tab_text"], padding=[5, 10])
style.map('TNotebook.Tab', background=[('selected', m["bg"])], foreground=[('selected', m["btn"])])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=5)

# --- ZAKŁADKA 1 ---
tab1 = tk.Frame(notebook, bg=m["bg"])
notebook.add(tab1, text="Zwykłe Hasło")

lbl_dl = tk.Label(tab1, text="Długość hasła:", bg=m["bg"], fg=m["fg"])
lbl_dl.pack(pady=5)
suwak_dlugosci = tk.Scale(tab1, from_=6, to_=32, orient=tk.HORIZONTAL, bg=m["bg"], fg=m["fg"], highlightthickness=0)
suwak_dlugosci.set(12)
suwak_dlugosci.pack()

var_wielkie, var_male, var_cyfry, var_specjalne, var_wyklucz = tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=True), tk.BooleanVar(value=False)

chk_buttons_tab1 = [
    tk.Checkbutton(tab1, text="Wielkie litery (A-Z)", variable=var_wielkie, bg=m["bg"], fg=m["fg"], selectcolor=m["accent"]),
    tk.Checkbutton(tab1, text="Małe litery (a-z)", variable=var_male, bg=m["bg"], fg=m["fg"], selectcolor=m["accent"]),
    tk.Checkbutton(tab1, text="Cyfry (0-9)", variable=var_cyfry, bg=m["bg"], fg=m["fg"], selectcolor=m["accent"]),
    tk.Checkbutton(tab1, text="Znaki specjalne (!@#$)", variable=var_specjalne, bg=m["bg"], fg=m["fg"], selectcolor=m["accent"]),
    tk.Checkbutton(tab1, text="Wyklucz podobne znaki (l, 1, I, o, 0)", variable=var_wyklucz, bg=m["bg"], fg=m["fg"], selectcolor=m["accent"])
]
for cb in chk_buttons_tab1: cb.pack(anchor="w", padx=60)

btn_gen1 = tk.Button(tab1, text="GENERUJ", command=generuj_standardowe, bg=m["btn"], fg="#ffffff", font=("Arial", 10, "bold"), width=15)
btn_gen1.pack(pady=10)

ramka_hasla = tk.Frame(tab1, bg=m["bg"])
ramka_hasla.pack(pady=5)

pole_hasla = tk.Entry(ramka_hasla, font=("Courier", 14), justify="center", width=18, bg=m["accent"], fg=m["fg"], insertbackground=m["fg"])
pole_hasla.grid(row=0, column=0, padx=2)

btn_oko = tk.Button(ramka_hasla, text="🔒", command=przelacz_widocznosc_hasla, bg=m["accent"], fg=m["fg"])
btn_oko.grid(row=0, column=1, padx=2)

btn_kopiuj1 = tk.Button(ramka_hasla, text="📋 Kopiuj", command=lambda: kopiuj_efekt(btn_kopiuj1, pole_hasla), bg=m["accent"], fg=m["fg"])
btn_kopiuj1.grid(row=0, column=2, padx=2)

etykieta_czasu = tk.Label(tab1, text="Szacowany czas złamania: -", font=("Arial", 9, "italic"), bg=m["bg"], fg=m["fg"])
etykieta_czasu.pack(pady=5)

# --- ZAKŁADKA 2 ---
tab2 = tk.Frame(notebook, bg=m["bg"])
notebook.add(tab2, text="Hasło Słowne (Passphrase)")

lbl_sl = tk.Label(tab2, text="Liczba słów w haśle:", bg=m["bg"], fg=m["fg"])
lbl_sl.pack(pady=15)
suwak_slow = tk.Scale(tab2, from_=3, to_=8, orient=tk.HORIZONTAL, bg=m["bg"], fg=m["fg"], highlightthickness=0)
suwak_slow.set(4)
suwak_slow.pack()

btn_gen2 = tk.Button(tab2, text="GENERUJ FRAZĘ", command=generuj_passphrase, bg=m["btn"], fg="#ffffff", font=("Arial", 10, "bold"), width=15)
btn_gen2.pack(pady=25)

ramka_pass = tk.Frame(tab2, bg=m["bg"])
ramka_pass.pack(pady=5)

pole_pass = tk.Entry(ramka_pass, font=("Courier", 12), justify="center", width=22, bg=m["accent"], fg=m["fg"], insertbackground=m["fg"])
pole_pass.grid(row=0, column=0, padx=2)

btn_kopiuj2 = tk.Button(ramka_pass, text="📋 Kopiuj", command=lambda: kopiuj_efekt(btn_kopiuj2, pole_pass), bg=m["accent"], fg=m["fg"])
btn_kopiuj2.grid(row=0, column=2, padx=2)

etykieta_czasu_pass = tk.Label(tab2, text="Szacowany czas złamania: -", font=("Arial", 9, "italic"), bg=m["bg"], fg=m["fg"])
etykieta_czasu_pass.pack(pady=5)

root.mainloop()
