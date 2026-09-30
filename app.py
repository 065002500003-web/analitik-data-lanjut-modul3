import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul utama aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

# Halaman 1: Dataset
if page == "Dataset":
    st.header("Halaman Dataset")
    
    # Baca file CSV PDDikti
    data = pd.read_csv("pddikti_example.csv")
    
    # Tampilkan data di Streamlit
    st.write("Berikut adalah preview data dari file pddikti_example.csv:")
    st.dataframe(data)

# Halaman 2: Visualisasi
elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    
    # Baca file CSV
    data = pd.read_csv("pddikti_example.csv")
    
    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]
    
    # Buat visualisasi menggunakan Matplotlib
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        
        # Urutkan data berdasarkan 'id' dengan urutan menurun
        subset = subset.sort_values(by="id", ascending=False)
        
        ax.plot(subset['semester'], subset['jumlah'], label=prog_studi, marker='o')
        
    ax.set_title(f"Visualisasi Data untuk {selected_university}")
    ax.set_xlabel('Semester')
    plt.xticks(rotation=90)  # Rotasi label sumbu x menjadi vertikal
    ax.set_ylabel('Jumlah')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Tampilkan plot ke Streamlit menggunakan fig eksplisit
    st.pyplot(fig)