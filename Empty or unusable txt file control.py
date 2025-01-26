import os

def check_txt_files(txt_folder):
    """
    .txt dosyalarını kontrol eder ve içi boş veya geçersiz formatta olanları ayırt eder.

    Args:
        txt_folder (str): .txt dosyalarının bulunduğu klasör.

    Returns:
        dict: İçi boş ve geçersiz dosyaların listelerini içeren bir sözlük.
    """
    empty_files = []  # İçi boş dosyalar
    invalid_files = []  # Geçersiz formatta dosyalar

    # Tüm .txt dosyalarını al
    txt_files = [f for f in os.listdir(txt_folder) if f.endswith(".txt")]

    for txt_file in txt_files:
        txt_path = os.path.join(txt_folder, txt_file)

        # Dosyanın içeriğini oku
        with open(txt_path, "r") as f:
            lines = f.readlines()

        # İçi boş dosyaları kontrol et
        if len(lines) == 0:
            empty_files.append(txt_file)
            continue

        # Geçersiz formatta dosyaları kontrol et
        for line in lines:
            parts = line.strip().split()
            # YOLO formatı: Her satırda en az 5 eleman olmalı (class_id, x_center, y_center, width, height)
            if len(parts) < 5:
                invalid_files.append(txt_file)
                break

    return {"empty_files": empty_files, "invalid_files": invalid_files}

# Kullanım
if __name__ == "__main__":
    txt_folder = r"C:\Users\def2i\OneDrive\Masaüstü\project see\txt_files"  # .txt dosyalarının bulunduğu klasör

    # Dosyaları kontrol et
    result = check_txt_files(txt_folder)

    # Sonuçları yazdır
    print("İçi boş dosyalar:")
    for file in result["empty_files"]:
        print(f"  - {file}")

    print("\nGeçersiz formatta dosyalar:")
    for file in result["invalid_files"]:
        print(f"  - {file}")