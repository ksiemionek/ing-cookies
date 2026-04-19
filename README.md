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
Uruchomienie z widoczną przeglądarką
```bash
pytest test_cookies.py --headed 
```

Uruchomienie z opóźnieniem, ułatwia widoczność kolejnych kroków
```bash
pytest test_cookies.py --headed --slowmo 1000
```

Uruchomienie w konkretnej przeglądarce
```bash
pytest test_cookies.py --browser chromium
pytest test_cookies.py --browser webkit
pytest test_cookies.py --browser firefox
```
![image](./img/browser-tests.png)

## GitHub Actions
Ze względu na widoczne na zdjęciu poniżej zabezpieczenie hCaptcha, automatyczne testy przez GitHub Actions są niemożliwe do przeprowadzenia.

![image](./img/ci-fail.png)

