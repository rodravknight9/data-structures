import requests
from bs4 import BeautifulSoup

# URL objetivo
url = "https://quotes.toscrape.com/"

# Hacemos la petición a la página
response = requests.get(url)

# Verificamos que la petición fue exitosa (código 200)
if response.status_code == 200:
    # Parseamos el contenido HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontramos todas las citas
    quotes = soup.find_all("span", class_="text")

    print("Citas encontradas:\n")
    for i, quote in enumerate(quotes, 1):
        print(f"{i}. {quote.get_text()}")
else:
    print(f"Error al acceder a la página: {response.status_code}")
