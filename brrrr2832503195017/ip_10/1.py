import ipaddress

ip = '112.160.0.0'
mask = '255.240.0.0'
net = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

print(sum(f"{h:b}".count('1') % 3 != 0 for h in net))

