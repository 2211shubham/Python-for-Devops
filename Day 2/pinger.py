import subprocess
import time

def checkhost(host, retries=3, delay=1):
    for i in range(1,retries+1):
        try:
            print(f"Pinging {host} (Attempt {i}/{retries})...")
            subprocess.run(["ping", "-c", '1', host],capture_output=True, check=True)
            print(f"{host} is reachable.")
            return True
        except subprocess.CalledProcessError:
            print(f"{host} is not reachable.")
            time.sleep(delay)
    return False

if(__name__ == "__main__"):
    checkhost("193.168.1.1")