import platform
import psutil

def get_system_info():
    print(f"System: {platform.system()} {platform.release()}")
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    memory = psutil.virtual_memory()
    total_memory_gb = memory.total / (1024 ** 3)
    available_memory_gb = memory.available / (1024 ** 3)
    print(f"Total Memory: {total_memory_gb:.2f} GB")
    print(f"Available Memory: {available_memory_gb:.2f} GB")



if __name__ == "__main__":
    get_system_info()