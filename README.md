# 🕷️ Python Web Scraping Project

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-43B02A?logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

> **Veri Toplama Sanatı:** Hem statik mimari (Requests/BS4) hem de dinamik tarayıcı otomasyonu (Selenium) kullanarak verileri özgürleştirin.

Bu proje, modern web kazıma tekniklerini göstermek amacıyla **Books to Scrape** ve **Quotes to Scrape** platformları için geliştirilmiş, Excel çıktısı üreten modüler bir araç setidir.

---

## 📂 Proje Yapısı

```text
.
├── 📜 Books Scraper.py       # Statik kazıyıcı (Hızlı & Hafif - Requests)
├── 📜 Quotes Scraper.py      # Dinamik kazıyıcı (Akıllı & Güçlü - Selenium)
├── 📊 books_dataset.xlsx     # Otomatik üretilen kitap verileri
├── 📊 quotes_dataset.xlsx    # Otomatik üretilen alıntı verileri
├── ⚙️ requirements.txt       # Proje bağımlılıkları
└── 📝 README.md              # Dokümantasyon
```

## 🚀 Özellikler

| Özellik | Books Scraper | Quotes Scraper |
|---------|---------------|----------------|
| **Teknoloji** | `requests` + `BeautifulSoup` | `selenium` (Headless Chrome) |
| **Hedef Site** | books.toscrape.com | quotes.toscrape.com |
| **Yöntem** | HTTP İstekleri (Statik) | Tarayıcı Otomasyonu (Dinamik) |
| **Hız** | ⚡ Çok Hızlı | 🐢 Orta (JS Bekleme Süreli) |
| **Çıktı** | `.xlsx` (Excel) | `.xlsx` (Excel) |

## 🛠️ Kurulum

1.  **Depoyu Klonlayın**
    ```bash
    git clone https://github.com/Utkuaykus/python-web-scraping-project.git
    cd python-web-scraping-project
    ```

2.  **Bağımlılıkları Yükleyin**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Kullanım

### 1. Kitapları Kazıma (Statik)
Tüm kitap kataloğunu saniyeler içinde tarar.
```bash
python "Books Scraper.py"
```
> *Çıktı: `books_dataset.xlsx` (Kitap Adı, Fiyat, Stok Durumu, Açıklama)*

### 2. Alıntıları Kazıma (Dinamik)
JavaScript ile yüklenen içerikleri gerçek bir tarayıcı gibi gezer.
```bash
python "Quotes Scraper.py"
```
> *Çıktı: `quotes_dataset.xlsx` (Alıntı, Yazar, Etiketler)*

---

## 📝 Lisans
Bu proje [MIT](LICENSE) lisansı ile korunmaktadır. Özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.

---
*Geliştirici: [Utku Aykuş](https://github.com/Utkuaykus)*
