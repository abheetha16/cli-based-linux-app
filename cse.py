from utils.runner import run

def install():
    print("\n[+] Installing CSE package...")
    run("apt update")

    run(
        "apt install -y "
        "gcc gdb make git "
        "python3 python3-pip "
        "wireshark apache2"
    )

    # Apache setup
    run("systemctl enable apache2")
    run("systemctl start apache2")

    # Wireshark non-root capture
    choice = input("Allow non-root packet capture (Wireshark)? (y/n): ")
    if choice.lower() == "y":
        run("usermod -aG wireshark $SUDO_USER")
        print("✔ User added to wireshark group (logout required)")

    print("✔ CSE package installed successfully")
