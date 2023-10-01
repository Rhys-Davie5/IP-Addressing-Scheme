# Import the ipaddress module
import ipaddress

# Define the network ID
network_id = '192.168.0.0/24'

# Create an IPv4Network object from the network ID
network = ipaddress.IPv4Network(network_id)

# Print the network ID and subnet mask
print(f'Network ID: {network.network_address}')
print(f'Subnet Mask: {network.netmask}')

# Print the first and last usable IP addresses in the network
print(f'First Usable IP Address: {network.network_address + 1}')
print(f'Last Usable IP Address: {network.broadcast_address - 1}')

# Print the total number of usable IP addresses in the network
print(f'Total Usable IP Addresses: {network.num_addresses - 2}')
