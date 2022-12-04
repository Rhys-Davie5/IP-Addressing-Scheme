import ipaddress

# Create a network object for the IP address range
network = ipaddress.ip_network('192.0.0.0/24')

# Iterate over the addresses in the network
for address in network:
  print(address)