from random import randint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from re import search

# Bir kere bunları indirdikten sonra bir daha indirmeye gerek kalmıyor
# from nltk import download
# download('stopwords')
# download('punkt_tab')

etkisiz_kelimeler = set(stopwords.words('turkish'))
pozitif_kelimeler = {"mutlu", "güzel", "iyi", "harika", "başarılı", "pozitif", "mükemmel"}
negatif_kelimeler = {"üzgün", "kötü", "berbat", "korkunç", "negatif", "başarısız"}
negatif_ekler = {"ma", "me", "mıyor", "miyor", "maz", "mez", "mamalı", "memeli"}

def calculatePolarite(sent: str) -> str:
    kelimeler = [kelime.lower() for kelime in word_tokenize(sent) if kelime.lower() not in etkisiz_kelimeler]
    print(kelimeler)

    olumsuzluk_var = False

    pozitif_sayisi = sum(1 for kelime in kelimeler if kelime in pozitif_kelimeler)
    negatif_sayisi = sum(1 for kelime in kelimeler if kelime in negatif_kelimeler)

    # Olumsuzluk eklerini tespit et
    for kelime in kelimeler: 
        for ek in negatif_ekler:
            if search(ek,kelime):
                olumsuzluk_var = True

    # Olumsuzluk ekleri varsa negatif kabul et
    if pozitif_sayisi == 0 and negatif_sayisi == 0 and olumsuzluk_var:
        return False  

    # Değil varsa negatif kabul et (değil mi? gibi olan yerlerde ise değilin negatif olarak kullanılmadığını belirt)
    if "değil" in kelimeler and not("?" in sent or "mi" in kelimeler):
        return False  

    return True if pozitif_sayisi >= negatif_sayisi else False
