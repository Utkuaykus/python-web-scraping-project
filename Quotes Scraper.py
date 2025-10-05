from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Chrome driver'ı başlat
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # görünmez çalışsın
driver = webdriver.Chrome(options=options)

quotes_data = []
page = 1

while True:
    url = f"https://quotes.toscrape.com/js/page/{page}/"
    driver.get(url)
    time.sleep(2)  # JS yüklenmesi için biraz bekle

    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    if not quotes:
        break

    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        tags = [t.text for t in q.find_elements(By.CLASS_NAME, "tag")]
        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })

    page += 1

driver.quit()

# Excel'e kaydet
df = pd.DataFrame(quotes_data)
df.to_excel("quotes_dataset.xlsx", index=False)
print("Quotes başarıyla kaydedildi -> quotes_dataset.xlsx")
