import os
from pathlib import Path

def rename_png_files(directory):
    """PNG dosyalarının isimlerini değiştirir"""
    # Klasördeki tüm PNG dosyalarını listele
    png_files = sorted([f for f in os.listdir(directory) if f.endswith('.png')])

    print(f"Toplam {len(png_files)} PNG dosyası bulundu.")
    print("\nDosya isimleri değiştiriliyor...")

    # Her dosya için
    for png_file in png_files:
        # Mevcut dosya yolu
        old_path = os.path.join(directory, png_file)

        # Yeni isim oluştur (rgb_ kısmını kaldır)
        new_name = png_file.replace('rgb_', '')  # 'rgb_' önekini kaldır

        # Yeni dosya yolu
        new_path = os.path.join(directory, new_name)

        try:
            # Dosyayı yeniden adlandır
            os.rename(old_path, new_path)
            print(f"Değiştirildi: {png_file} -> {new_name}")
        except Exception as e:
            print(f"Hata: {png_file} değiştirilemedi - {str(e)}")

    print("\nİşlem tamamlandı!")

def main():
    # PNG dosyalarının bulunduğu klasör
    png_directory = r"C:\Users\def2i\OneDrive\Masaüstü\project see\png_files"

    # Klasörün varlığını kontrol et
    if not os.path.exists(png_directory):
        print(f"Hata: {png_directory} klasörü bulunamadı!")
        return

    # Örnek bir dosya ismi göster
    example_files = os.listdir(png_directory)[:1]
    if example_files:
        print(f"Örnek dosya ismi: {example_files[0]}")

    # Kullanıcıdan onay al
    response = input("\nDosya isimlerini değiştirmek istediğinizden emin misiniz? (evet/hayır): ")
    if response.lower() != 'evet':
        print("İşlem iptal edildi.")
        return

    # Dosya isimlerini değiştir
    rename_png_files(png_directory)

if __name__ == "__main__":
    main()