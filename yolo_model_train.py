from ultralytics import YOLO
import os
from pathlib import Path

def train_model(yaml_path, epochs=100, imgsz=512, batch=16):
    """
    YOLOv8 segmentasyon modelini eğitir.

    Parametreler:
        yaml_path: Veri seti yapılandırma dosyasının yolu
        epochs: Eğitim epoch sayısı
        imgsz: Görüntü boyutu
        batch: Batch size
    """
    try:
        # YOLOv8s-seg modelini yükle
        model = YOLO('yolov8s.pt')  # Segmentasyon modeli için yolov8s-seg.pt kullanılıyor

        # Model eğitimini başlat
        results = model.train(
            data=yaml_path,          # veri seti yapılandırma dosyası
            epochs=epochs,           # toplam epoch sayısı
            imgsz=imgsz,            # görüntü boyutu
            batch=batch,            # batch size
            name='train',       # eğitim sonuçlarının kaydedileceği klasör adı
            device='0',             # GPU kullanımı için '0', CPU için 'cpu'
            patience=20,            # early stopping için sabır değeri
            save=True,              # en iyi modeli kaydet
            plots=True              # eğitim grafiklerini kaydet
        )

        print("Model eğitimi tamamlandı!")
        return results

    except Exception as e:
        print(f"Model eğitimi sırasında hata oluştu: {str(e)}")
        return None

def main():
    # Veri seti yapılandırma dosyasının yolu
    yaml_path = r"C:\Users\def2i\OneDrive\Masaüstü\project see\dataset.yaml"

    # Dosyanın varlığını kontrol et
    if not os.path.exists(yaml_path):
        print(f"Hata: {yaml_path} bulunamadı!")
        return

    print("Model eğitimi başlıyor...")
    results = train_model(
        yaml_path=yaml_path,
        epochs=100,          # Eğitim epoch sayısı
        imgsz=512,          # Görüntü boyutu
        batch=16            # Batch size
    )

if __name__ == "__main__":
    main()