# 📚 Kitap Tavsiye Sistemi (Book Recommendation System)
<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Books-ECEFF4?style=for-the-badge&logo=google-books&logoColor=black" />
</div>

---

Bu proje, okuyucu davranışlarını ve puanlama modellerini temel alarak geliştirilmiş bir **İşbirlikçi Filtreleme (Collaborative Filtering)** sistemidir. Kullanıcıların ortak okuma zevklerini matematiksel bir düzlemde eşleştirerek kişiselleştirilmiş kitap önerileri sunar.

## 🏗️ Mühendislik Metodolojisi

Proje, verinin işlenmesinden modelin üretim ortamına aktarılmasına kadar uçtan uca bir veri bilimi hattı (pipeline) izler:

1.  **Veri Temizliği & Filtreleme:** İstatistiksel gürültüyü azaltmak için en az 200 oy veren kullanıcılar ve 50+ oylamaya sahip popüler kitaplar filtrelenmiştir.
2.  **Vektör Uzayı Modellemesi:** Kitaplar, kullanıcı puanlarından oluşan çok boyutlu bir vektör uzayında temsil edilmiştir.
3.  **K-Nearest Neighbors (KNN):** Benzer içerikleri bulmak için **Cosine Similarity** metriği kullanılarak "en yakın komşu" tespiti yapılmıştır.
4.  **Bellek Optimizasyonu:** Milyonlarca hücreden oluşan pivot tablolar, bellek dostu `CSR Matrix` (Sparse Matrix) formatına dönüştürülmüştür.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** Python 3.12
* **Analiz:** Pandas, NumPy
* **Makine Öğrenmesi:** Scikit-learn (KNN)
* **Veri Yapısı:** Scipy (Sparse Matrix)
* **Model Kayıt:** Joblib
* **Arayüz:** Streamlit

## 📊 Analiz Çıktıları

Proje içerisinde gerçekleştirilen görselleştirmeler şunları içerir:
* En çok etkileşim alan kitapların popülarite dağılımı.
* Kitaplar arası benzerlik mesafelerinin (distance) grafiksel analizi.

## 🚀 Kurulum ve Çalıştırma

1.  Depoyu klonlayın:
    ```bash
    git clone [https://github.com/kullaniciadi/kitap-tavsiye-sistemi.git](https://github.com/kullaniciadi/kitap-tavsiye-sistemi.git)
    ```
2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3.  Uygulamayı başlatın:
    ```bash
    streamlit run app_book.py
    ```

## 👤 Geliştirici
**Serdar ÖNAL**
*İnşaat Mühendisi & Yapay Zeka Geliştiricisi*
2026

---
*Bu proje, veri odaklı karar verme ve makine öğrenmesi algoritmalarının pratik uygulaması amacıyla geliştirilmiştir.*