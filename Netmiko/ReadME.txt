# Netmiko Network Backup Script

This project automatically connects to multiple network devices (routers) using Netmiko over SSH, retrieves the running configuration, and saves it as a text file.  
Each backup file is named in the format: 

{hostname}_{day}-{month}-{year}.txt

Example: `R1_27-09-2025.txt`

---

## Features
- SSH connection to multiple devices
- Automatic backup of running configuration
- Saves config with timestamped filenames
- Parallel processing using threading to improve backup speed

---

## Setup & Usage

1. Clone this repository:
   git clone https://github.com/SleepyMonke/Network_Automation.git
   cd Network_Automation/Netmiko_Backup

2. Install dependencies:
   pip install -r requirements.txt

3. Edit the script:
   a)Update the devices array with the IP addresses of your routers.
   b)Set your username, password, and secret.

4. Run the script:

   python Auto_Backup.py
