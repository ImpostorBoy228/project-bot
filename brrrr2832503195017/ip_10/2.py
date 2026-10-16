import ipaddress

ip = '172.16.128.0'
mask = '255.255.192.0'
net = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

print(sum(f"{h:b}".count('1') % 2 != 0 for h in net))

