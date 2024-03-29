import ipaddress
from prettytable import PrettyTable

# Define the classes
    classes = {
    'A': '0.0.0.0/1',
    'B': '128.0.0.0/2',
    'C': '192.0.0.0/3'
    }

# Print the details for each class
    for class_name, network in classes.items():
# Create a new table for each class
    table = PrettyTable(['Prefix', 'Netmask'])

    for prefix in range(1, 33):
        net = ipaddress.ip_network(f'{network.split("/")[0]}/{prefix}', strict=False)
        # Add the details to the table
        table.add_row([prefix, str(net.netmask)])

# Print the table
    print(f'\nClass {class_name}:')
    print(table)

    def calculate_ip_scheme(ip_input):
         try:
# Create an IP interface for subnet mask calculation
        ip_interface = ipaddress.ip_interface(ip_input)
        # Create a network from the IP interface
        network = ip_interface.network

# Get the first and last usable IP addresses in the network
        first_usable = next(network.hosts())
        last_usable = list(network.hosts())[-1]

        print("-----------------------------------------------------------------------------------------------")

        # Print the network ID, subnet mask, broadcast ID, and the maximum possible number of hosts
        print(f"Network ID: {network.network_address}")
        print(f"Subnet mask: {ip_interface.netmask}")
        print(f"First usable IP address: {first_usable}")
        print(f"Last usable IP address: {last_usable}")
        print(f"Broadcast ID: {network.broadcast_address}")
        print(f"Maximum possible number of hosts: {network.num_addresses - 2}")  # Subtracting network and broadcast addresses

    except ValueError as e:
        print(f"Error: {e}")

    while True:
# Prompt the user for the IP address and subnet mask
    ip_input = input("Enter the IP address with subnet (192.168.1.0/24) or type 'exit': ")
    
# Check if the user wants to exit the loop
    if ip_input.lower() == 'exit':
        print("Exiting the program.")
        break

    calculate_ip_scheme(ip_input)
    print("\n")  # Print a newline for better readability before the next prompt
