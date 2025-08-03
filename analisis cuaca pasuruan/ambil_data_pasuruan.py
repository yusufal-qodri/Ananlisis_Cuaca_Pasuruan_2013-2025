import requests
import pandas as pd

# Koordinat Pasuruan
latitude = -7.6441
longitude = 112.9061

# Rentang waktu
start_date = "2013-01-01"
end_date = "2025-08-01"

# URL API
url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={latitude}&longitude={longitude}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    f"&timezone=Asia%2FBangkok"
)

# Ambil data
response = requests.get(url)
data = response.json()

# Buat DataFrame
df = pd.DataFrame(data['daily'])

# Simpan ke CSV
df.to_csv("cuaca_pasuruan_2013_2025.csv", index=False)
print(" Yeayyyy, Data cuaca berhasil disimpan ke cuaca_pasuruan_2013_2025.csv")
