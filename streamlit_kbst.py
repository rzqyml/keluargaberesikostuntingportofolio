import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Membaca model
kbst_model = pickle.load(open('kbst_model.sav', 'rb'))

# Judul web
st.title('SISTEM PREDIKSI KELUARGA BERESIKO STUNTING')

# Upload file CSV
uploaded_file = st.file_uploader("Unggah File Exel", type=["xlsx","xls"])

# DataFrame untuk data dari file exce,
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Menampilkan DataFrame
    st.write('DataFrame dari File Excel')
    st.write(df)

    # Tombol untuk prediksi
    if st.button('Lakukan Prediksi'):
        # Menggunakan model untuk melakukan prediksi
        kbst_prediction = kbst_model.predict(df)

        # Menyimpan hasil prediksi ke dalam DataFrame hasil
        hasil = pd.DataFrame(kbst_prediction, columns=['hasil prediksi'])

 # Menggabungkan dataframe hasil prediksi dengan dataframe asli
        merged_df = pd.concat([df, hasil], axis=1)
        
        # Menampilkan dataframe gabungan
        st.write('DataFrame Hasil Prediksi:')
        st.write(merged_df)
        
 # Generate pie chart
        prediction_counts = merged_df['hasil prediksi'].value_counts()
        prediction_counts.index = ['Tidak Beresiko Stunting' if idx == 0 else 'Beresiko Stunting' for idx in prediction_counts.index]
        fig = px.pie(prediction_counts, values=prediction_counts.values, names=prediction_counts.index, title='Persentase Prediksi')
        st.plotly_chart(fig)
