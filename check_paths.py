from pathlib import Path
import os

def check_paths():
    """
    Klasör yollarını kontrol et ve detaylı bilgi ver
    """
    # Klasör yollarını belirle
    base_dir = Path(r"C:\Users\def2i\OneDrive\Masaüstü\project see")
    image_dir = base_dir / "png_files"
    label_dir = base_dir / "txt_files"
    output_dir = base_dir / "dataset"

    # Kontrol edilecek klasörleri ve açıklamalarını listele
    paths_to_check = {
        "Ana klasör": base_dir,
        "Görüntü klasörü": image_dir,
        "Etiket klasörü": label_dir,
        "Çıktı klasörü": output_dir
    }

    # Her klasörü kontrol et
    for description, path in paths_to_check.items():
        print(f"\nKontrol ediliyor: {description}")
        print(f"Yol: {path}")

        if path.exists():
            print("✓ Klasör mevcut")

            # Klasör içeriğini kontrol et
            if description in ["Görüntü klasörü", "Etiket klasörü"]:
                files = list(path.glob('*.*'))
                print(f"- Dosya sayısı: {len(files)}")
                if files:
                    print(f"- Örnek dosyalar: {', '.join(str(f.name) for f in files[:3])}")

            # Yazma izinlerini kontrol et
            if os.access(path, os.W_OK):
                print("✓ Yazma izni mevcut")
            else:
                print("✗ Yazma izni yok!")
        else:
            print("✗ Klasör bulunamadı!")

if __name__ == "__main__":
    try:
        check_paths()
    except Exception as e:
        print(f"\nHata oluştu: {str(e)}")