# utils/color_utils.py
import cv2
import numpy as np
import colorsys

def extract_average_hsl(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("🚫 الصورة ما انقرأت")
        return 0, 0, 0  # مؤقتًا نرجّع HSL وهمي
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img.shape
    crop = img[h//3:2*h//3, w//3:2*w//3]
    avg_color = crop.mean(axis=0).mean(axis=0)
    r, g, b = avg_color / 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360, 2), round(s, 2), round(l, 2)