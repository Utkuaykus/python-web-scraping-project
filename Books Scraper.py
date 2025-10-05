import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/catalogue/category/books/default_15/page-{}.html"
books_data = []
page = 1

while True:
    url = base_url.format(page)
    headers = {"User-Agent": "Mozilla/5.0"}  # Sunucu güvenliği için
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    if not books:
        break

    for b in books:
        title = b.h3.a["title"]
        price = b.find("p", class_="price_color").get_text(strip=True).replace("Â","")

        # Kitap detay sayfası URL'sini güvenli şekilde oluştur
        book_url = urljoin(url, b.h3.a["href"])
        book_resp = requests.get(book_url, headers=headers)
        book_soup = BeautifulSoup(book_resp.text, "html.parser")

        # Gerçek description alma (div sonrası p)
        desc_tag = book_soup.find("div", id="product_description")
        if desc_tag:
            description = desc_tag.find_next_sibling("p").get_text(strip=True)
        else:
            description = "No description"

        # Çok uzun açıklamayı kısalt (170 karakter)
        description = description[:170]+"..." if len(description) > 170 else description

        books_data.append({
            "Kitap": title,
            "Açıklama": description,
            "Fiyat": price
        })

    page += 1

# Excel'e yaz
df = pd.DataFrame(books_data)
df.to_excel("books_dataset.xlsx", index=False)
print("Books başarıyla kaydedildi -> books_dataset.xlsx")
