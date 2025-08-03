# Load package
library(tidyverse)
library(lubridate)

# Baca data
data <- read_csv("cuaca_pasuruan_2013_2025.csv")

# Rename kolom & buat kolom tambahan
data <- data %>%
  rename(
    tanggal = time,
    suhu_max = temperature_2m_max,
    suhu_min = temperature_2m_min
  ) %>%
  mutate(
    tanggal = ymd(tanggal),
    rata_rata_suhu = (suhu_max + suhu_min) / 2,
    tahun = year(tanggal),
    bulan = month(tanggal, label = TRUE, abbr = TRUE)
  )

# INSIGHT 1: Apakah suhu meningkat dari tahun ke tahun?
ggplot(data, aes(x = tanggal, y = rata_rata_suhu)) +
  stat_summary(fun = mean, geom = "line", color = "tomato", size = 1.2) +
  labs(title = "Tren Suhu Rata-Rata Tahunan (Pasuruan 2013–2025)",
       x = "Tahun", y = "Suhu Rata-rata (°C)") +
  theme_minimal()
ggsave("hasil_visualisasi/Tren Suhu Rata-Rata Tahunan.png", width = 8, height = 5)


# INSIGHT 2: Bulan mana yang paling banyak hujan?
ggplot(data, aes(x = bulan, y = precipitation_sum)) +  # pastikan nama kolom ini bener
  stat_summary(fun = mean, geom = "bar", fill = "steelblue") +
  labs(title = "Rata-Rata Curah Hujan Bulanan (2013–2025)",
       x = "Bulan", y = "Curah Hujan (mm)") +
  theme_minimal()
ggsave("hasil_visualisasi/Rata-Rata Curah Hujan Bulanan.png", width = 8, height = 5)


# INSIGHT 3: Pola musim hujan / kemarau
ggplot(data, aes(x = bulan, y = precipitation_sum, group = tahun)) +
  stat_summary(fun = mean, geom = "line", aes(color = as.factor(tahun)), show.legend = FALSE) +
  labs(title = "Pola Musiman Curah Hujan per Tahun",
       x = "Bulan", y = "Curah Hujan (mm)") +
  theme_minimal()
ggsave("hasil_visualisasi/Pola Musiman Curah Hujan Per Tahun.png", width = 8, height = 5)


# INSIGHT 4: Pengaruh El-Nino / La-Nina
el_nino_years <- c(2015, 2019)
la_nina_years <- c(2016, 2020)

data$anomali <- case_when(
  data$tahun %in% el_nino_years ~ "El-Nino",
  data$tahun %in% la_nina_years ~ "La-Nina",
  TRUE ~ "Normal"
)

ggplot(data, aes(x = tahun, y = precipitation_sum, fill = anomali)) +
  stat_summary(fun = mean, geom = "bar") +
  scale_fill_manual(values = c("El-Nino" = "red", "La-Nina" = "blue", "Normal" = "gray")) +
  labs(title = "Curah Hujan Tahunan vs El-Nino / La-Nina",
       x = "Tahun", y = "Curah Hujan Rata-Rata (mm)", fill = "Kondisi Iklim") +
  theme_minimal()
ggsave("hasil_visualisasi/Curah Hujan Rata-Rata.png", width = 8, height = 5)


data$hari = day(data$tanggal)
data$bulan_nama = month(data$tanggal, label = TRUE, abbr = TRUE)

ggplot(data, aes(x = hari, y = bulan_nama, fill = rata_rata_suhu)) +
  geom_tile(color = "white") +
  scale_fill_viridis_c(option = "C", name = "Suhu (°C)") +
  labs(title = "📆 Kalender Suhu Harian (Gradasi Warna)") +
  theme_minimal()
ggsave("hasil_visualisasi/Kalender Suhu Harian.png", width = 8, height = 5)


ggplot(data, aes(x = tahun, y = bulan, fill = precipitation_sum)) +
  geom_tile(color = "white") +
  scale_fill_gradient(low = "lightblue", high = "darkblue", name = "Curah Hujan (mm)") +
  labs(title = "Heatmap Curah Hujan Pasuruan, Jawa Timur") +
  theme_minimal()
ggsave("hasil_visualisasi/suhu_tahunan.png", width = 8, height = 5)
