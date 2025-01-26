import os
import shutil
import random
import yaml

def create_yolov8_structure_and_move_files(png_folder, txt_folder, base_path, class_names, val_split=0.2):
    """
    YOLOv8 için gerekli klasör yapısını oluşturur ve dosyaları taşır.

    Args:
        png_folder (str): PNG dosyalarının bulunduğu klasör.
        txt_folder (str): TXT dosyalarının bulunduğu klasör (etiketler).
        base_path (str): YOLOv8 veri kümesi ana klasör yolu.
        class_names (list): Sınıf isimlerinin listesi.
        val_split (float): Doğrulama veri seti için ayrılacak oran (0.2 = %20).
    """
    # Gerekli klasör yollarını tanımla
    train_images_path = os.path.join(base_path, "train", "images")
    train_labels_path = os.path.join(base_path, "train", "labels")
    val_images_path = os.path.join(base_path, "val", "images")
    val_labels_path = os.path.join(base_path, "val", "labels")

    # Gerekli klasörleri oluştur
    for path in [train_images_path, train_labels_path, val_images_path, val_labels_path]:
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # PNG ve TXT dosyalarını eşleştir
    png_files = sorted([f for f in os.listdir(png_folder) if f.endswith(".png")])
    txt_files = sorted([f for f in os.listdir(txt_folder) if f.endswith(".txt")])

    if len(png_files) != len(txt_files):
        print("Warning: PNG ve TXT dosyalarının sayısı eşleşmiyor!")
        print(f"PNG dosyaları: {len(png_files)}, TXT dosyaları: {len(txt_files)}")

    # Dosyaları eşleştir ve karıştır
    paired_files = list(zip(png_files, txt_files))
    random.shuffle(paired_files)

    # Doğrulama veri seti için ayrılacak dosya sayısı
    val_count = int(len(paired_files) * val_split)

    # Doğrulama ve eğitim dosyalarını ayır
    val_files = paired_files[:val_count]
    train_files = paired_files[val_count:]

    # Eğitim dosyalarını taşı
    for png_file, txt_file in train_files:
        shutil.copy(os.path.join(png_folder, png_file), os.path.join(train_images_path, png_file))
        shutil.copy(os.path.join(txt_folder, txt_file), os.path.join(train_labels_path, txt_file))

    # Doğrulama dosyalarını taşı
    for png_file, txt_file in val_files:
        shutil.copy(os.path.join(png_folder, png_file), os.path.join(val_images_path, png_file))
        shutil.copy(os.path.join(txt_folder, txt_file), os.path.join(val_labels_path, txt_file))

    print(f"Moved {len(train_files)} files to training set.")
    print(f"Moved {len(val_files)} files to validation set.")

    # YAML dosyasını oluştur
    yaml_data = {
        "path": base_path,  # Ana veri kümesi yolu
        "train": "train/images",  # Eğitim görüntüleri klasörü
        "val": "val/images",      # Doğrulama görüntüleri klasörü
        "names": class_names      # Sınıf isimleri
    }

    yaml_path = os.path.join(base_path, "dataset.yaml")
    with open(yaml_path, "w") as yaml_file:
        yaml.dump(yaml_data, yaml_file, default_flow_style=False)
    print(f"YAML file created: {yaml_path}")

# Kullanım
if __name__ == "__main__":
    # PNG ve TXT dosyalarının bulunduğu klasörler
    png_folder = r"C:\Users\def2i\OneDrive\Masaüstü\project see\png_files"  # PNG dosyalarının olduğu klasör
    txt_folder = r"C:\Users\def2i\OneDrive\Masaüstü\project see\txt_files"  # TXT dosyalarının olduğu klasör

    # YOLOv8 veri kümesi ana klasör yolu
    base_path = r"C:\Users\def2i\OneDrive\Masaüstü\project see"  # YOLOv8 veri kümesi ana klasörü

    # Sınıf isimleri
    class_names = ["Küre"]  # Sınıf isimlerini buraya girin

    # Doğrulama veri seti oranı (%20)
    val_split = 0.2

    # Klasör yapısını oluştur ve dosyaları taşı
    create_yolov8_structure_and_move_files(png_folder, txt_folder, base_path, class_names, val_split)