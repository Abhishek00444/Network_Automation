import threading

from netmiko import ConnectHandler
from datetime import datetime


def backup(device):
    connect = ConnectHandler(**device)
    connection.enable()
    output = connect.send_command('sh run')
    hostname = connect.find_prompt()[0:-1]  //get the hostname of device to use in filename

    filename = f'{hostname}_{day}-{month}-{year}'

    with open(filename, 'w') as backup:
        backup.write(output)

    connect.disconnect()


devices = ['192.168.122.10', '192.168.122.20', '192.168.122.30']  #IP of devices to connect
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year

threads = list()
for ip in devices:
    device = {
        'device_type': 'cisco_ios',  #change for non cisco devices
        'host': ip,
        'port': 22,
        'username': 'student',  #change according to your account
        'password': 'student',  #change according to your account
        'secret': 'student',    #change according to device enable password
        'verbose': True
    }
    th = threading.Thread(target=backup,args=(device,))
    threads.append(th)

print(threads)
for th in threads:
    th.start()

for th in threads:
    th.join()

