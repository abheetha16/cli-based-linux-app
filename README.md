# SystemSoft

SystemSoft is a CLI-based Linux automation tool that installs essential Computer Science development tools with a single command.

It simplifies environment setup for students and developers by automating package installation and configuration.

---

## Features

* One-command installation of CSE tools
* Modular package system (demo, cse)
* CLI-based (lightweight and fast)
* Root and OS validation
* Automated installation using apt
* Basic service configuration (Apache)
* Logging support for executed commands

---

## Packages

### Demo Package

Installs minimal tools:

* gcc
* python3
* python3-pip

Command:
systemsoft install demo

---

### CSE Package

Installs a full development environment:

Programming:

* gcc, gdb, make
* python3, python3-pip
* git

Networking:

* wireshark
* net-tools
* curl

Web:

* apache2

Command:
systemsoft install cse

---

## Usage

Clone the repository:
git clone <your-repo-link>
cd systemsoft

Run the tool:
sudo python3 systemsoft.py install demo

or

sudo python3 systemsoft.py install cse

---

## Requirements

* Linux (Ubuntu/Debian-based systems)
* Python 3
* Root privileges (sudo)

---

## Project Structure

systemsoft/
├── systemsoft.py
├── packages/
│   ├── demo.py
│   └── cse.py
├── utils/
│   ├── runner.py
│   ├── logger.py
│   └── checks.py

---

## Future Improvements

* Dry-run mode (--dry-run)
* Config file support
* Multi-distro support
* Package verification
* .deb installer
