import json
import numpy as np
from pathlib import Path
import os

def convert_isaac_to_yolo(input_folder, output_folder):
    """
    input_folder: Isaac Sim çıktılarının bulunduğu klasör
    output_folder: YOLO formatındaki .txt dosyalarının kaydedileceği klasör
    """
    # Çıktı klasörünü oluştur
    os.makedirs(output_folder, exist_ok=True)

    # Tüm label dosyalarını bul
    label_files = list(Path(input_folder).glob("*labels*.json"))
    print(f"Toplam işlenecek dosya sayısı: {len(label_files)}")

    for label_file in label_files:
        try:
            # Dosya numarasını al (örn: 0000)
            file_num = label_file.stem.split('_')[-1]

            # İlgili .npy dosyasının yolunu oluştur
            npy_file = Path(input_folder) / f"bounding_box_2d_tight_{file_num}.npy"

            if not npy_file.exists():
                print(f"Uyarı: {npy_file} bulunamadı, bu dosya atlanıyor.")
                continue

            # NPY dosyasını oku
            bbox_data = np.load(npy_file)

            # (1,) boyutlu veriyi tuple'a dönüştür
            bbox = bbox_data.item()

            if len(bbox) != 6:
                print(f"Beklenmeyen veri uzunluğu ({file_num}): {len(bbox)}")
                continue

            # Çıktı dosyasını oluştur
            output_file = Path(output_folder) / f"{file_num}.txt"

            # Görüntü boyutları (varsayılan olarak 512x512)
            image_width = 512
            image_height = 512

            with open(output_file, 'w') as f:
                # bbox formatı: (class_id, x_min, y_min, x_max, y_max, confidence)
                class_id = int(bbox[0])
                x_min, y_min = float(bbox[1]), float(bbox[2])
                x_max, y_max = float(bbox[3]), float(bbox[4])

                # YOLO formatına dönüştür
                x_center = (x_min + x_max) / (2 * image_width)
                y_center = (y_min + y_max) / (2 * image_height)
                width = (x_max - x_min) / image_width
                height = (y_max - y_min) / image_height

                # Değerleri 0-1 aralığında sınırla
                x_center = min(max(x_center, 0), 1)
                y_center = min(max(y_center, 0), 1)
                width = min(max(width, 0), 1)
                height = min(max(height, 0), 1)

                # YOLO formatında yaz
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

            if int(file_num) % 100 == 0:
                print(f"İşlenen dosya: {file_num}")

        except Exception as e:
            print(f"Hata oluştu ({file_num}): {str(e)}")
            print(f"bbox_data içeriği: {bbox_data}")

    print("Dönüştürme tamamlandı!")



# Kullanım
input_folder = "C:\\Users\\def2i\\OneDrive\\Masaüstü\\project see\\data"  # Isaac Sim çıktılarının bulunduğu klasör
output_folder = "C:\\Users\\def2i\\OneDrive\\Masaüstü\\project see\\txt_files"  # YOLO etiketlerinin kaydedileceği klasör

convert_isaac_to_yolo(input_folder, output_folder)