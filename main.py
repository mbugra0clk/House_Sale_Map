import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = 'C:/ML/House_Sale/HouseSale2/house_sales.csv'
df = pd.read_csv(data)
df.head()


# Sadece sayısal değişkenleri seçelim
df_numeric = df.select_dtypes(include=["number"])

# Korelasyon matrisini hesaplayalım
corr_matrix = df_numeric.corr()

# SalePrice ile en yüksek korelasyona sahip 10 değişkeni seçelim
top_corr_features = corr_matrix["SalePrice"].abs().sort_values(ascending=False).head(10)
top_corr_features


import seaborn as sns
import matplotlib.pyplot as plt

# Seçili en iyi korelasyona sahip değişkenler için korelasyon matrisini alalım
top_corr_matrix = corr_matrix[top_corr_features.index].loc[top_corr_features.index]

# Isı haritasını çizelim
plt.figure(figsize=(10, 6))
sns.heatmap(top_corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("En Çok Korelasyon Gösteren Özellikler")
plt.show()


# Posta kodu bazında ortalama fiyatları hesapla
zipcode_prices = df.groupby("ZipCode")["SalePrice"].mean().reset_index()

# En çok satış yapılan ilk 20 posta kodunu seçelim
top_zipcodes = zipcode_prices.sort_values("SalePrice", ascending=False).head(20)

# Bar grafiği çizelim
plt.figure(figsize=(10, 6))
sns.barplot(x=top_zipcodes["ZipCode"].astype(str), y=top_zipcodes["SalePrice"], palette="Blues_r")
plt.xlabel("Posta Kodu")
plt.ylabel("Ortalama Satış Fiyatı")
plt.title("Posta Koduna Göre Ortalama Ev Fiyatları (İlk 20)")
plt.xticks(rotation=45)
plt.show()


import folium

# Posta kodları ve ilgili enlem-boylam değerleri
locations = {
    98039: {"lat": 47.6175, "lon": -122.2421},
    98008: {"lat": 47.6240, "lon": -122.1220},
    98004: {"lat": 47.6184, "lon": -122.2031},
    98112: {"lat": 47.6298, "lon": -122.2970},
    98040: {"lat": 47.5697, "lon": -122.2325},
}

# En pahalı 10 evi seçelim
top_10_expensive_houses = df.nlargest(10, "SalePrice")[["ZipCode", "SalePrice"]]

# Haritayı oluştur (Seattle bölgesine odaklanarak)
m = folium.Map(location=[47.6062, -122.3321], zoom_start=11)

# Her ev için haritaya bir işaretçi ekleyelim
for _, row in top_10_expensive_houses.iterrows():
    zipcode = row["ZipCode"]
    if zipcode in locations:
        folium.Marker(
            location=[locations[zipcode]["lat"], locations[zipcode]["lon"]],
            popup=f"Posta Kodu: {zipcode}<br>Satış Fiyatı: ${row['SalePrice']:,.0f}",
            icon=folium.Icon(color="red", icon="home")
        ).add_to(m)

# Haritayı kaydedelim
m.save("en_pahali_evler_haritasi.html")
m