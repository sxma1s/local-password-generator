# Lokalny Generator Haseł (Offline)

Prosty, bezpieczny i działający w 100% lokalnie generator haseł z graficznym interfejsem użytkownika (GUI). Narzędzie powstało jako bezpieczna, offline'owa alternatywa dla internetowych generatorów haseł.

## 🚀 Funkcje
- **Pełna prywatność**: Kod działa całkowicie offline, nie wysyła żadnych danych do sieci.
- **Bezpieczeństwo kryptograficzne**: Generowanie haseł opiera się na module `secrets` w Pythonie, który zapewnia losowość odporną na cyberataki.
- **Szacowanie odporności**: Program wylicza przybliżony czas potrzebny na złamanie hasła przy założeniu ataku offline z prędkością 100 miliardów prób na sekundę.
- **Pełna konfiguracja**: Możliwość wyboru długości (6-32 znaków) oraz zestawów znaków (wielkie/małe litery, cyfry, znaki specjalne).

## 🛠️ Jak uruchomić kod źródłowy?
Aby uruchomić program z poziomu kodu, wymagane jest posiadanie zainstalowanego środowiska **Python 3**.

1. Pobierz plik `generator.pyw`.
2. Kliknij na niego dwukrotnie, aby uruchomić aplikację.

## 📦 Jak zbudować samodzielny plik .exe?
Jeśli chcesz stworzyć wersję `.exe`, która zadziała na każdym komputerze z systemem Windows (nawet bez zainstalowanego Pythona):

1. Otwórz Wiersz polecenia (CMD) i zainstaluj bibliotekę PyInstaller:
   ```bash
   python -m pip install pyinstaller
   ```
2. Przejdź do folderu z plikiem projektu (np. Pulpit):
   ```bash
   cd Desktop
   ```
3. Uruchom proces kompilacji:
   ```bash
   python -m PyInstaller --noconsole --onefile generator.pyw
   ```
4. Gotowy program znajdziesz w nowo utworzonym folderze `dist/`.

## 📄 Licencja
Projekt udostępniany na licencji MIT. Możesz go dowolnie modyfikować i rozpowszechniać.
