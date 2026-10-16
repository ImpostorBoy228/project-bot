import ipaddress

ip = '105.224.200.224'
mask = '255.255.255.224'
net = ipaddress.ip_network(f'{ip}/{mask}', strict=False)

print(sum(f"{h:b}".count('1') % 4 == 0 for h in net))

