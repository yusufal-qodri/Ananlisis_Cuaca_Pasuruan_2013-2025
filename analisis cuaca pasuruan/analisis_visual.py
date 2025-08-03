import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("cuaca_pasuruan_2013_2025.csv")
df["date"] = pd.to_datetime(df["time"])
df["year"] = df["date"].dt.year

# Hitung suhu rata-rata tahunan
df["temp_avg"] = (df["temperature_2m_max"] + df["temperature_2m_min"]) / 2
avg_per_year = df.groupby("year")["temp_avg"].mean().reset_index()

# Plot
plt.figure(figsize=(10, 5))
sns.lineplot(data=avg_per_year, x="year", y="temp_avg", marker='o')
plt.title("Rata-rata Suhu Tahunan di Pasuruan (2013–2023)")
plt.xlabel("Tahun")
plt.ylabel("Suhu Rata-rata (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# === ANALISIS CURAH HUJAN ===

# 1. Hitung total curah hujan per tahun
hujan_per_tahun = df.groupby('year')['precipitation_sum'].sum().reset_index()

# 2. Plot total curah hujan per tahun
plt.figure(figsize=(10, 5))
sns.barplot(data=hujan_per_tahun, x='year', y='precipitation_sum', palette='Blues_d')
plt.title("Total Curah Hujan Tahunan di Pasuruan (2013–2025)")
plt.xlabel("Tahun")
plt.ylabel("Total Curah Hujan (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Hari dengan hujan ekstrem
ekstrem_hujan = df[df['precipitation_sum'] > 50]
print("Jumlah hari dengan hujan ekstrem (>50mm):", len(ekstrem_hujan))
print("Contoh hari ekstrem:")
print(ekstrem_hujan[['date', 'precipitation_sum']].head())
