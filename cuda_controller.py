import torch

def check_cuda():
    # Check if CUDA is available
    cuda_available = torch.cuda.is_available()

    if cuda_available:
        # Get CUDA information
        cuda_device_count = torch.cuda.device_count()
        cuda_device_name = torch.cuda.get_device_name(0)
        cuda_current_device = torch.cuda.current_device()

        print("CUDA Available: Yes")
        print(f"Total CUDA Device Count: {cuda_device_count}")
        print(f"Active CUDA Device: {cuda_current_device}")
        print(f"CUDA Device Name: {cuda_device_name}")

        # Memory information
        print("\nMemory Information:")
        print(f"Total Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
        print(f"Allocated Memory: {torch.cuda.memory_allocated(0) / 1024**3:.2f} GB")
        print(f"Cached Memory: {torch.cuda.memory_reserved(0) / 1024**3:.2f} GB")

    else:
        print("CUDA Not Available!")
        print("No GPU found, operations will be performed on the CPU.")

if __name__ == "__main__":
    check_cuda()
