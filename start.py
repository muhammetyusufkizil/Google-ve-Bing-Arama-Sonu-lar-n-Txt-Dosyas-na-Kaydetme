# Ekrana yazılan kelimeyi al
kelime = input("Aramak istediğiniz kelimeyi girin: ")

# Google ve Bing arama URL'lerini oluştur
google_url = "https://www.google.com/search?q=" + kelime
bing_url = "https://www.bing.com/search?q=" + kelime

# İnternetten veri çekmek için requests modülünü içe aktar
import requests

# Google ve Bing arama sonuçlarını al
google_sonuc = requests.get(google_url)
bing_sonuc = requests.get(bing_url)

# Arama sonuçlarını HTML olarak ayrıştırmak için BeautifulSoup modülünü içe aktar
from bs4 import BeautifulSoup

# Google ve Bing arama sonuçlarını HTML olarak ayrıştır
google_soup = BeautifulSoup(google_sonuc.text, "html.parser")
bing_soup = BeautifulSoup(bing_sonuc.text, "html.parser")

# HTML'den linkleri seçmek için bir CSS seçici tanımla
link_seçici = "a[href^='http']"

# Google ve Bing arama sonuçlarından linkleri seç
google_linkler = google_soup.select(link_seçici)
bing_linkler = bing_soup.select(link_seçici)

# Linkleri txt dosyasına kaydetmek için bir dosya adı belirle
dosya_adı = kelime + ".txt"

# Linkleri txt dosyasına kaydetmek için bir dosya aç
with open(dosya_adı, "w", encoding="utf-8") as dosya:
    # Dosyanın başına bir başlık yaz
    dosya.write(kelime + " için Google ve Bing arama sonuçları\n\n")
    
    # Google linklerini dosyaya yaz
    dosya.write("Google linkleri:\n")
    for link in google_linkler:
        # Linkin href özelliğini al
        href = link["href"]
        # Linki dosyaya yaz
        dosya.write(href + "\n")
    
    # Dosyaya bir boşluk bırak
    dosya.write("\n")
    
    # Bing linklerini dosyaya yaz
    dosya.write("Bing linkleri:\n")
    for link in bing_linkler:
        # Linkin href özelliğini al
        href = link["href"]
        # Linki dosyaya yaz
        dosya.write(href + "\n")

# Dosyayı kapat
dosya.close()

# İşlem tamamlandığını bildir
print("İşlem tamamlandı. Linkler " + dosya_adı + " dosyasına kaydedildi.")
