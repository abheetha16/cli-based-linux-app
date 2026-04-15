from utils.runner import run

def install():
    print("\n[+] Installing DEMO package...")
    run("apt update")
    run("apt install -y gcc python3 python3-pip")
    print("✔ Demo package installed (gcc + python)")
