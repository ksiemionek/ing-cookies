# ING Cookies

Zadanie rekturacyjne, automatyzacja akceptowania cookie analitycznych na stronie `ing.pl`.

## Uruchomienie

1. Sklonowanie repozytorium
```bash
   git clone https://github.com/ksiemionek/ing-cookies.git
   cd ing-cookies
```

2. Stworzenie środowiska wirtualnego z potrzebnymi bibliotekami
```bash
python -3 venv .venv
source ./venv/bin/activate
pip install -r requirements.txt
playwright install
```

3. Uruchomienie testu
```bash
pytest test_cookies.py --headed 
```
lub z opóźnieniem, ułatwia widoczność kolejnych kroków
```bash
pytest test_cookies.py --headed --slowmo 1000
```