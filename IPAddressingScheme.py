import ipaddress

def calculate_subnet(ip, mask):
    # Create an IPv4Network object from the IP and mask
    network = ipaddress.IPv4Network(ip + '/' + mask, strict=False)
    
    # Extract subnet information
    network_address = str(network.network_address)
    broadcast_address = str(network.broadcast_address) 
    netmask = str(network.netmask)
    total_hosts = network.num_addresses
    usable_hosts = network.num_addresses - 2
    
    # Generate host IP range
    host_min = network_address.split('.')[-1] 
    host_min = int(host_min) + 1
    host_max = broadcast_address.split('.')[-1]
    host_max = int(host_max) - 1
    host_range = f"{network_address.split('.')[0]}.{network_address.split('.')[1]}.{network_address.split('.')[2]}.{host_min} - {network_address.split('.')[0]}.{network_address.split('.')[1]}.{network_address.split('.')[2]}.{host_max}"
    
    # Print the results
    print(f"Network address: {network_address}")
    print(f"Broadcast address: {broadcast_address}") 
    print(f"Subnet mask: {netmask}")
    print(f"Total number of hosts: {total_hosts}")
    print(f"Number of usable hosts: {usable_hosts}")
    print(f"Host IP range: {host_range}")

# Get user input 
ip_address = input("Enter an IP address: ")
subnet_mask = input("Enter a subnet mask (e.g. 24 or 255.255.255.0): ")

# Handle subnet mask format
if '.' not in subnet_mask:
    subnet_mask = str(ipaddress.IPv4Network('0.0.0.0/' + subnet_mask, strict=False).netmask)

# Calculate and display the subnet information
calculate_subnet(ip_address, subnet_mask)
