# 
# Zadanie String replace
# 1) Stwórz funkcję cleanText, która będzie czytać
#    przykładowy tekst z określonych słów.
# 2) Użyj funkcję replace do zamiany podanych słów na 
#    wykropkowane, które wielokrotnie może pojawić się
#    w przekazanym łańcuchu. Dla uproszczenia będziesz
#    zamieniać nazwy języków programowania ;) np.
#    php zmienisz na ***, java na **** itd
# 3) Zastąp następujące słowa kluczowe: 
#    JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji cleanText.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#   """ Programowanie zacząłem z językiem php, następnie
#   poznałem: html i css, ale obecnie skupiam się na 
#   JavaScript"""
#   Wynik pokaż w konsoli.
# 

def cleanText(text):
    text = text.replace("JavaScript", "*" * 8)
    text = text.replace("Python", "*" * 5)
    text = text.replace("PHP", "*" * 3)
    text = text.replace("HTML", "*" * 4)
    text = text.replace("CSS", "*" * 3)
    
    print(text)
    return text

cleanText("""
          Naukę programowania, rozpoczęłam z Hipertekstowym językiem znaczników HTML,
          następnie poznałam CSS, PHP i JavaScript, ale obecnie skupiam się na języku
          wysokiego poziomu ogólnego przeznaczenia - jakim jest Python. :)
          """)