import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Sayfa Ayarları
st.set_page_config(page_title="Kitap Tavsiye Sistemi", layout="centered")

# Kaynakları Yükle
@st.cache_resource
def load_data():
    model = joblib.load('book_knn_model.joblib')
    pivot = joblib.load('book_pivot_table.joblib')
    return model, pivot

model_knn, book_pivot = load_data()

#  Arayüz
st.title("📚 Akıllı Kitap Tavsiye Sistemi")
st.write("Okuma alışkanlıklarınıza göre bir sonraki kitabınızı bulun.")

# Kitap Seçimi
selected_book = st.selectbox("Daha önce okuduğunuz bir kitabı seçin:", book_pivot.index)

#  Tavsiye Fonksiyonu
def get_recom(book_name):
    idx = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model_knn.kneighbors(book_pivot.iloc[idx, :].values.reshape(1, -1), n_neighbors=6)
    
    return [book_pivot.index[i] for i in suggestions[0][1:]]

#  Buton
if st.button("Benzer Kitapları Getir"):
    recoms = get_recom(selected_book)
    st.subheader(f"'{selected_book}' Sevenler Bunları da Okudu:")
    for i, book in enumerate(recoms, 1):
        st.write(f"{i}. {book}")

#  İmza (Standart Mühendislik Mührü)
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p><b>Geliştirici:</b> Serdar ÖNAL | İnşaat Mühendisi & Yapay Zeka Geliştiricisi | 2026</p>
    </div>
    """, unsafe_allow_html=True
)