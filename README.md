# Python Web Scraping Project

Bu proje, **Books to Scrape** ve **Quotes to Scrape** web sitelerinden veri çekmek için geliştirilmiş iki farklı Python scripti içerir. Proje, hem statik (BeautifulSoup) hem de dinamik (Selenium) web kazıma tekniklerini örneklendirmektedir.

## Özellikler

-   **Kitap Kazıma (`Books Scraper.py`):**
    -   `requests` ve `BeautifulSoup` kullanarak statik sayfa yapısını tarar.
    -   [books.toscrape.com](https://books.toscrape.com) sitesinden kitap adı, fiyatı ve açıklamasını çeker.
    -   Verileri `books_dataset.xlsx` dosyasına kaydeder.

-   **Alıntı Kazıma (`Quotes Scraper.py`):**
    -   `selenium` kullanarak dinamik ve JavaScript içeren sayfaları tarar.
    -   [quotes.toscrape.com](https://quotes.toscrape.com) sitesinden alıntı metni, yazar ve etiketleri toplar.
    -   Verileri `quotes_dataset.xlsx` dosyasına kaydeder.

## Kurulum

1.  Bu depoyu (repository) klonlayın:
    ```bash
    git clone https://github.com/Utkuaykus/python-web-scraping-project.git
    cd python-web-scraping-project
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

    *Gereksinimler:*
    -   requests
    -   beautifulsoup4
    -   pandas
    -   openpyxl (Excel çıktısı için)
    -   selenium

## Kullanım

### Kitap Verilerini Çekme
Bu script, tüm sayfaları gezerek kitap bilgilerini toplar.
```bash
python "Books Scraper.py"
```

### Alıntıları Çekme
Bu script, Selenium ile tarayıcıyı (headless modda) açar ve tüm sayfalardaki alıntıları toplar.
```bash
python "Quotes Scraper.py"
```

## Notlar

-   **Selenium Sürücüsü:** `Quotes Scraper.py` çalıştırıldığında bilgisayarınızda yüklü olan Google Chrome sürümü ile uyumlu bir ChromeDriver'a ihtiyaç duyabilir. Selenium 4.6+ sürümü kullanıyorsanız, sürücü yönetimi otomatik yapılacaktır.
-   **Etik Kullanım:** Bu scriptler yalnızca eğitim amaçlıdır ve [toscrape.com](https://toscrape.com) sandbox ortamında çalışmak üzere tasarlanmıştır.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
