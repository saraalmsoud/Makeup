# utils/recommend.py
from sklearn.metrics.pairwise import euclidean_distances

def recommend_shades_with_image(h, s, l, df_original, scaler, top_n=5):
    df = df_original.copy()
    input_scaled = scaler.transform([[h, s, l]])
    df_scaled = scaler.transform(df[['hue', 'sat', 'lightness']])
    distances = euclidean_distances(input_scaled, df_scaled)[0]
    df['distance'] = distances
    return df.sort_values('distance').head(top_n)[['name', 'specific', 'brand', 'shade_group', 'imgSrc']]