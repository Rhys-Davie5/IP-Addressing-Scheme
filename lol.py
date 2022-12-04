import ipaddress

# Create an IPv4 network
ipv4_net = ipaddress.IPv4Network('192.0.0.0/24')

# Divide the network into 3 subnets
subnets = list(ipv4_net.subnets(new_prefix=26))

# Print the subnet addresses
for subnet in subnets:
    print(subnet)

