# Netmiko Network Backup Script

This project connects to multiple network devices (routers) using Netmiko over SSH, runs the commands written in input.txt, and displays the output for each device.

---

## Features
- SSH connection to multiple devices simultaneously.
- Execute the same commands across multiple devices and collect outputs.
- Parallel execution using threading for faster command execution.

---

## Setup & Usage

1. Clone this repository:
   git clone https://github.com/SleepyMonke/Network_Automation.git
   cd Network_Automation/Netmiko_Counfigure

2. Install dependencies:
   pip install -r requirements.txt

3. Edit the script:
   a)Update the devices array with the IP addresses of your routers.
   b)Set your username, password, and secret.
   c) Set `device_type` to match your device (default is 'cisco_ios').

4. Change the input file:
   Edit input.txt to include the commands you want to run on all devices.

5. Run the script:

   python Counfigure.py