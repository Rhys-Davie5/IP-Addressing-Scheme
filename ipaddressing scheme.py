
Nsubnets =     ["1",   "2",   "4",  "8",  "16", "32", "64", "128", "256"]
Number_of_hosts =       ["256", "128", "64", "32", "16", "8",  "4",  "2",   "1"]
Number_of_subnet_mask = ["24",  "25",  "26", "27", "28", "29", "30", "31",  "32"]
NetworkID = input("Please enter the Main IP Address: ")
PreFix_Length = input("Enter the Prefix length of the network: ")
Number_of_subnets = input("How many subnets?: ")

print("")

if Number_of_subnets in Nsubnets:
    print("You have entered ")


if PreFix_Length in Number_of_subnet_mask:
    print("You have entered a valid subnet mask ")
else:
    print("you havent entered a valid subnet mask... try again ")
