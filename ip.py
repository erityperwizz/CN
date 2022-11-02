ip = input("Enter IP address: ")
ip = ip.split(".") #Splitting the IP address into octets
n = int(input("Enter the number of leftmost bits to be used for subnetting:"))
subnet_mask_bin = "1"*n + "0"*(32-n)
subnet_mask = []
for i in range(0,32,8):
    subnet_mask.append(str(int(subnet_mask_bin[i:i+8],2)))
subnet_mask = ".".join(subnet_mask) 
print("Subnet mask is: ", subnet_mask) #Printing the subnet mask
ip_bin = ""
for i in ip:
    ip_bin += bin(int(i))[2:].zfill(8)
ip_bin = ip_bin[:n] + "0"*(32-n)
ip_bin = [ip_bin[i:i+8] for i in range(0,32,8)]
ip_bin = [str(int(i,2)) for i in ip_bin]
ip_bin = ".".join(ip_bin)
print("First IP address of the subnet is: ", ip_bin)
ip_bin = ""
for i in ip:
    ip_bin += bin(int(i))[2:].zfill(8)
ip_bin = ip_bin[:n] + "1"*(32-n)
ip_bin = [ip_bin[i:i+8] for i in range(0,32,8)]
ip_bin = [str(int(i,2)) for i in ip_bin]
ip_bin = ".".join(ip_bin)
print("Last IP address of the subnet is: ", ip_bin)
print("Number of addresses in the subnet is: ", 2**(32-n))
