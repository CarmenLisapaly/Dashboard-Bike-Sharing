import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari all_data.csv
all_data = pd.read_csv('all_data.csv')

# Mengatur tema dan estetika Streamlit
st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")
sns.set_palette("muted")

# Header Dashboard
st.title("Bike Sharing Data Analysis Dashboard")
st.subheader("Exploratory Data Analysis on Bike Sharing Dataset")

# Menampilkan Data Overview
st.sidebar.header("Data Overview")
st.sidebar.write("Tabel ini menunjukkan beberapa data terkait peminjaman sepeda.")
st.dataframe(all_data.head())

# Visualisasi Pola Penggunaan Sepeda Berdasarkan Musim
st.header("Pola Penggunaan Sepeda Berdasarkan Musim")
season_usage = pd.Series({
    'Musim Dingin': 2604,
    'Musim Panas': 4922,
    'Musim Semi': 5644,
    'Musim Gugur': 4728
})

season_order = ['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin']
season_usage = season_usage[season_order]
season_colors = ['#98FB98', '#FFD700', '#FF8C00', '#ADD8E6']

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(season_usage.index, season_usage.values, color=season_colors)
ax.set_title('Pola Penggunaan Sepeda Berdasarkan Musim', fontsize=16)
ax.set_xlabel('Musim', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=12)
ax.set_xticks(range(len(season_usage.index)))
ax.set_xticklabels(season_usage.index)
st.pyplot(fig)

# Visualisasi Puncak Penggunaan Sepeda Berdasarkan Jam
st.header("Puncak Penggunaan Sepeda Berdasarkan Jam")
hour_usage = all_data.groupby('hr')['cnt_hour'].sum()

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(hour_usage.index, hour_usage.values, marker='o', color='#72BCD4', linewidth=2)
ax.set_title('Puncak Penggunaan Sepeda Berdasarkan Jam', fontsize=16)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Total Peminjaman', fontsize=12)
ax.set_xticks(hour_usage.index)
ax.grid(True)
st.pyplot(fig)

# Visualisasi Perbedaan Penggunaan Sepeda Antara Hari Kerja dan Hari Libur
st.header("Perbedaan Penggunaan Sepeda Antara Hari Kerja dan Hari Libur")
workday_usage = all_data.groupby('workingday')['cnt_day'].mean()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(workday_usage.index, workday_usage.values, color=['#FF6347', '#32CD32'])
ax.set_title('Perbedaan Penggunaan Sepeda Antara Hari Kerja dan Hari Libur', fontsize=16)
ax.set_xlabel('Hari Kerja', fontsize=12)
ax.set_ylabel('Rata-rata Jumlah Peminjaman', fontsize=12)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
st.pyplot(fig)

# Visualisasi Kontribusi Pengguna terhadap Total Peminjaman
st.header("Kontribusi Pengguna terhadap Total Peminjaman Sepeda")
casual_contribution = all_data['casual_contribution'].sum() / all_data['cnt_hour'].sum()
registered_contribution = all_data['registered_contribution'].sum() / all_data['cnt_hour'].sum()

rfm_contribution = pd.DataFrame({
    'User Type': ['Pengguna Kasual', 'Pengguna Terdaftar'],
    'Contribution': [casual_contribution, registered_contribution]
})

fig, ax = plt.subplots(figsize=(8, 8))
sns.barplot(x="User Type", y="Contribution", data=rfm_contribution, palette=["#72BCD4", "#72BCD4"], ax=ax)
ax.set_title("Kontribusi Pengguna terhadap Total Peminjaman Sepeda", fontsize=16)
ax.set_xlabel("Tipe Pengguna", fontsize=12)
ax.set_ylabel("Persentase Kontribusi", fontsize=12)
st.pyplot(fig)