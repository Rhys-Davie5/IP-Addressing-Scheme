import ipaddress

def generate_ip_address_scheme(network_id, subnet_mask):
    try:
        network = ipaddress.IPv4Network(f"{network_id}/{subnet_mask}", strict=False)
        print(f"Network: {network.network_address}")
        print(f"Netmask: {network.netmask}")
        print(f"First IP Address: {network.network_address + 1}")
        print(f"Last IP Address: {network.broadcast_address - 1}")
    except ipaddress.AddressValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    network_id = input("Enter the network ID (e.g., 192.168.1.0): ")
    subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")
    generate_ip_address_scheme(network_id, subnet_mask)
