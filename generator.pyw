import secrets
import string
import math
import tkinter as tk
from tkinter import messagebox

def generuj():
    dlugosc = int(suwak_dlugosci.get())
    
    pula = ""
    if var_wielkie.get():    pula += string.ascii_uppercase
    if var_male.get():       pula += string.ascii_lowercase
    if var_cyfry.get():      pula += string.digits
    if var_specjalne.get():  pula += string.punctuation
    
    if not pula:
        messagebox.showerror("Błąd", "Wybierz przynajmniej jeden zestaw znaków!")
        return

    # Bezpieczne losowanie hasła
    haslo = "".join(secrets.choice(pula) for _ in range(dlugosc))
    
    # Obliczanie kombinacji i czasu łamania
    kombinacje = len(pula) ** dlugosc
    sekundy = kombinacje / 100_000_000_000
    
    if sekundy < 1: czas = "Natychmiast"
    elif sekundy < 3600: czas = f"{sekundy/60:.1f} min"
    elif sekundy < 86400: czas = f"{sekundy/3600:.1f} godz."
    elif sekundy < 31536000: czas = f"{sekundy/86400:.0f} dni"
    else: czas = f"{sekundy/31536000:,.0f} lat"

    # Wyświetlenie wyników w okienku
    pole_hasla.delete(0, tk.END)
    pole_hasla.insert(0, haslo)
    etykieta_czasu.config(text=f"Szacowany czas złamania: {czas}")

# --- Tworzenie okna graficznego ---
root = tk.Tk()
root.title("Lokalny Generator Haseł")
root.geometry("400x350")

tk.Label(root, text="Długość hasła:").pack(pady=5)
suwak_dlugosci = tk.Scale(root, from_=6, to_=32, orient=tk.HORIZONTAL)
suwak_dlugosci.set(12)
suwak_dlugosci.pack()

var_wielkie = tk.BooleanVar(value=True)
var_male = tk.BooleanVar(value=True)
var_cyfry = tk.BooleanVar(value=True)
var_specjalne = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Wielkie litery (A-Z)", variable=var_wielkie).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Małe litery (a-z)", variable=var_male).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Cyfry (0-9)", variable=var_cyfry).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Znaki specjalne (!@#$)", variable=var_specjalne).pack(anchor="w", padx=50)

tk.Button(root, text="GENERUJ HASŁO", command=generuj, bg="lightgreen", font=("Arial", 10, "bold")).pack(pady=15)

pole_hasla = tk.Entry(root, font=("Courier", 14), justify="center", width=25)
pole_hasla.pack(pady=5)

etykieta_czasu = tk.Label(root, text="Szacowany czas złamania: -", font=("Arial", 9, "italic"))
etykieta_czasu.pack(pady=5)

root.mainloop()
