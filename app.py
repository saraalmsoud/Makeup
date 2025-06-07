from flask import Flask, render_template, request
import pandas as pd
from utils.color_utils import extract_average_hsl
from utils.recommend import recommend_shades_with_image
from sklearn.preprocessing import StandardScaler
import os

app = Flask(__name__)
df = pd.read_csv('allShades.csv')
df_recommend = df[['brand', 'hue', 'sat', 'lightness', 'name', 'specific', 'shade_group', 'imgSrc']].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['hue', 'sat', 'lightness']])

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join('static', 'uploaded.jpg')
            file.save(filepath)
            print("✅ الصورة انحفظت")
            
            h, s, l = extract_average_hsl(filepath)
            print(f"HSL ➜ h: {h}, s: {s}, l: {l}")
            
            recommendations = recommend_shades_with_image(h, s, l, df, scaler, top_n=5).to_dict(orient='records')
            print("📦 عدد التوصيات:", len(recommendations))
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)