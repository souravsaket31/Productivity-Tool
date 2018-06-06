import time
from datetime import datetime as dt

redirect = '127.0.0.1'
host_path = r'C:\Windows\System32\drivers\etc\hosts'
sites_to_block = ['www.fb.com','facebook.com','www.facebook.com','www.yahoo.com','https://in.yahoo.com/?p=us']
print(dt.now())

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('Working Hours!!')
        with open(host_path,'r+') as f:
            content = f.read()
            for site in sites_to_block:
                if site in content:
                    pass
                else:
                    f.write(redirect + ' ' + site + '\n')
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(x in line for x in sites_to_block):
                    file.write(line)
            file.truncate()
        print("Relax!!")
    time.sleep(5)
