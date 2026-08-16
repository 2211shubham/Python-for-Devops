import subprocess
import time

def runCommand(cmd):
    try:
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            capture_output=True,
            check=True,
            text=True
        )
        print(f"result : {result.stdout}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with error:\n{e.stderr}")
        return None
    except FileNotFoundError:
        print(f"❌ Command '{cmd[0]}' not found on this system.")
        return None

if __name__ == "__main__":
    runCommand(["ls", "-la"])
    runCommand(["df", "-Th"])
    runCommand(["free", "-h"])
    runCommand(["ping", "example.com"])
    runCommand(["badcommand"])
