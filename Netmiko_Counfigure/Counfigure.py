from netmiko import ConnectHandler
import threading

def file(device):
    connect = ConnectHandler(**device)
    print(connect.check_config_mode())
    output = connect.send_config_from_file('input.txt')
    print(output)

    connect.disconnect()

devices = ['192.168.122.10', '192.168.122.20', '192.168.122.30']  #IP of devices to connect

threads = list()
for ip in devices:
    device = {
        'device_type': 'cisco_ios',  #change for non cisco devices
        'host': ip,
        'port': 22,
        'username': 'student',   #change according to your account
        'password': 'student',	 #change according to your account	
        'secret': 'student',     #change according to device enable password
        'verbose': True
    }
    th = threading.Thread(target=file,args=(device,))
    threads.append(th)

print(threads)
for th in threads:
    th.start()

for th in threads:
    th.join()