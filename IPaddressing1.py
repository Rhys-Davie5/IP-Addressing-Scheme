import ipaddress

num_devices = int(input("enter the number of devices that will be connected to the network: "))
address_range = ipaddress.ip_network('192.168.0.0/24')

subnet_size = address_range.num_addresses // num_devices
subnets = list(address_range.subnets(new_prefix=subnet_size))

for subnet in subnets:
    for address in subnet:
        print(address)

