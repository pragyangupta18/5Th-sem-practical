import ipaddress


def subnet_calculation(ip_address, subnet_prefix_length):
    # Parse the given IP address and subnet prefix length
    network = ipaddress.IPv4Network(f'{ip_address}/{subnet_prefix_length}', strict=False)
    
    # Print network details
    print(f"IP Address: {ip_address}")
    print(f"Subnet Prefix Length: {subnet_prefix_length}")
    print(f"Subnet Mask: {network.netmask}")
  

if __name__ == "__main__":
    try:
        ip_address = input("Enter an IP address (e.g., 192.168.1.0): ")
        subnet_prefix_length = int(input("Enter the subnet prefix length (e.g., 24 for /24): "))
        subnet_calculation(ip_address, subnet_prefix_length)
    except ValueError:
        print("Invalid input. Please enter a valid IP address and subnet prefix length.")
