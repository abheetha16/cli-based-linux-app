import argparse
from packages import demo, cse
from utils.checks import check_os, check_root

def main():
    parser = argparse.ArgumentParser(
        description="SystemSoft – Linux installer for CSE tools"
    )

    parser.add_argument(
        "command",
        choices=["install"],
        help="Command to execute"
    )

    parser.add_argument(
        "package",
        choices=["demo", "cse"],
        help="Package to install"
    )

    args = parser.parse_args()

    check_os()
    check_root()

    if args.command == "install":
        if args.package == "demo":
            demo.install()
        elif args.package == "cse":
            cse.install()

if __name__ == "__main__":
    main()
