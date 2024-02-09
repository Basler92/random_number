from selenium import webdriver
import random
import time

# Inicjalizacja przeglądarki (w tym przypadku Chrome)
driver = webdriver.Chrome()

# Otwórz stronę, na której chcesz przeprowadzić test (możesz zmienić ten adres URL)
url = "https://www.example.com"
driver.get(url)

# Generuj losową liczbę
random_number = random.randint(1, 100)

# Znajdź element na stronie, do którego chcesz wprowadzić losową liczbę (możesz zmienić ten selektor CSS)
input_element = driver.find_element_by_css_selector("#example_input")

# Wprowadź wygenerowaną losową liczbę do pola tekstowego
input_element.send_keys(str(random_number))

# Poczekaj chwilę, aby zobaczyć rezultat (możesz dostosować czas oczekiwania)
time.sleep(5)

# Zamknij przeglądarkę
driver.quit()
