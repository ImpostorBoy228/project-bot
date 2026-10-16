import ipaddress

ip = '192.168.32.128'
mask = '255.255.255.192'
net = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

print(sum(f"{h:b}".count('1') % 2 == 0 for h in net))

