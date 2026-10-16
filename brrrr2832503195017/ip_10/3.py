import ipaddress

ip = '122.159.136.144'
mask = '255.255.255.248'
net = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

print(sum(f"{h:b}".count('1') % 4 != 0 for h in net))

