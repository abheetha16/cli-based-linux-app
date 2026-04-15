import os
import sys
import platform

def check_os():
    if platform.system() != "Linux":
        print("❌ This tool supports Linux only.")
        sys.exit(1)

def check_root():
    if os.geteuid() != 0:
        print("❌ Please run using sudo.")
        sys.exit(1)
