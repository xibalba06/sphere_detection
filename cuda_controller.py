import torch

def check_cuda():
    # CUDA kullanılabilir mi kontrol et
    cuda_available = torch.cuda.is_available()
    
    if cuda_available:
        # CUDA bilgilerini al
        cuda_device_count = torch.cuda.device_count()
        cuda_device_name = torch.cuda.get_device_name(0)
        cuda_current_device = torch.cuda.current_device()
        
        print("CUDA Kullanılabilir: Evet")
        print(f"Toplam CUDA Device Sayısı: {cuda_device_count}")
        print(f"Aktif CUDA Device: {cuda_current_device}")
        print(f"CUDA Device İsmi: {cuda_device_name}")
        
        # Bellek bilgisi
        print("\nBellek Bilgisi:")
        print(f"Toplam Bellek: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
        print(f"Ayrılmış Bellek: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
        print(f"Önbellek: {torch.cuda.memory_reserved(0) / 1024**3:.2f} GB")
        
    else:
        print("CUDA Kullanılamıyor!")
        print("GPU bulunamadı, işlemler CPU üzerinde gerçekleştirilecek.")

if __name__ == "__main__":
    check_cuda()