import cv2
from ultralytics import YOLO

def live_camera_inference(model_path, camera_index=0, conf_threshold=0.6):
    """
    Canlı kamera akışında YOLO modeliyle nesne algılama.

    Parametreler:
        model_path: Eğitilmiş YOLO modelinin yolu (örneğin, 'best.pt')
        camera_index: Kullanılacak kamera indeksi (varsayılan: 0)
        conf_threshold: Algılama için minimum güven eşiği (varsayılan: 0.5)
    """
    # YOLO modelini yükle
    model = YOLO(model_path)

    # Kamerayı başlat
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    print("Kamera akışı başlatıldı. Çıkmak için 'q' tuşuna basın.")

    while True:
        # Kameradan bir kare al
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı, kamera kapatılıyor...")
            break

        # YOLO modelini kare üzerinde çalıştır
        results = model(frame)

        # Algılama sonuçlarını çizin
        annotated_frame = results[0].plot()  # Algılama sonuçlarını çizer

        # Çerçeveyi ekranda göster
        cv2.imshow("YOLOv8 Live Detection", annotated_frame)

        # 'q' tuşuna basıldığında çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera ve pencereleri serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Eğitilmiş modelin yolu
    model_path = r"C:\Users\def2i\OneDrive\Masaüstü\project see\runs\detect\train\weights\best.pt"  # Eğitilmiş model dosyanızın adı

    # Canlı kamera akışını başlat
    live_camera_inference(model_path)