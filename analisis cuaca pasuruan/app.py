import streamlit as st
from PIL import Image

st.header("Visualisasi R ")

# Gambar suhu tahunan dari R
img1 = Image.open("grafik_suhu_tahunan.png")
st.image(img1, caption="Grafik Suhu Tahunan (dibuat di R)", use_column_width=True)

# Gambar heatmap hujan dari R
img2 = Image.open("heatmap_hujan.png")
st.image(img2, caption="Heatmap Curah Hujan Bulanan (dibuat di R)", use_column_width=True)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cuaca_pasuruan_2013_2025.csv")
df["date"] = pd.to_datetime(df["time"])
df["year"] = df["date"].dt.year
df["temp_avg"] = (df["temperature_2m_max"] + df["temperature_2m_min"]) / 2

# Judul Aplikasi
st.title("Dashboard Cuaca Pasuruan (2013–2025)")

# Slider tahun
tahun_dipilih = st.slider("Pilih Tahun", int(df["year"].min()), int(df["year"].max()), 2025)

# Filter data sesuai tahun
df_tahun = df[df["year"] == tahun_dipilih]

# Suhu rata-rata tahun ini
rata_suhu = df_tahun["temp_avg"].mean()
total_hujan = df_tahun["precipitation_sum"].sum()

st.metric(label="🌡️ Suhu Rata-rata", value=f"{rata_suhu:.2f} °C")
st.metric(label="🌧️ Total Curah Hujan", value=f"{total_hujan:.2f} mm")

# Grafik suhu rata-rata per tahun
avg_suhu = df.groupby("year")["temp_avg"].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=avg_suhu, x="year", y="temp_avg", marker='o', ax=ax1)
ax1.set_title("Tren Suhu Rata-rata per Tahun")
ax1.set_ylabel("°C")
st.pyplot(fig1)

# Grafik total hujan per tahun
hujan_tahunan = df.groupby("year")["precipitation_sum"].sum().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=hujan_tahunan, x="year", y="precipitation_sum", palette="Blues_d", ax=ax2)
ax2.set_title("Total Curah Hujan per Tahun")
ax2.set_ylabel("mm")
st.pyplot(fig2)
