'''
Prompt a user to enter in an IP address from standard input.
Read the IP address in and break it up into its octets.
Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

​$ python exercise2.py 

Please enter an IP address: 80.98.100.240

    Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
'''
# Version 1
#
def usage():
    print()
    print("   Program Usage")
    print("-" *30)
    print("python print_ip.py { -h | help | <ip address> }")
    print()
    print("python print_ip.py -h\t\tprints this help menu")
    print()
    print("python print_ip.py help\t\tprints this help menu")
    print()
    print("Example:")
    print("python print_ip.py 192.168.0.1")
    print()
    print()
#
def valid_octet(test_octet):
    # test if the octect is a valid number bewteen 0-255
    if 0 <= test_octet <= 255:
        return True
    else:
        return False
    #
def break_ip_into_list(arg1):
    temp_list = arg1.split(".")
    print(f"test: 'arg1' equals: {arg1}")
    print(f"test: 'temp_list' equals: {temp_list}")
    # First Octet
    try:
        octet_1 = int(temp_list[0])
    except:
        ValueError
        return False
    if valid_octet(octet_1) == False:
        exit("First value is out of range...IP must be 0-255")
    print(f"test: first 'octet' is: {octet_1}")
    # Second Octet
    try:
        octet_2 = int(temp_list[1])
    except:
        ValueError
        return False
    if valid_octet(octet_2) == False:
        exit("Second value is out of range...IP must be 0-255")
    print(f"test: second 'octet' is: {octet_2}")
    # Third Octet
    try:
        octet_3 = int(temp_list[2])
    except:
        ValueError
        return False
    if valid_octet(octet_3) == False:
        exit("Third value is out of range...IP must be 0-255")
    print(f"test: third 'octet' is: {octet_3}")
    # Fourth Octet
    try:
        octet_4 = int(temp_list[3])
    except:
        ValueError
        return False
    if valid_octet(octet_4) == False:
        exit("Fourth value is out of range...IP must be 0-255")
    print(f"test: fourth 'octet' is: {octet_4}")
    # check for invalid entry
    if len(temp_list) > 4:
        exit("Error: The entry has too many values")
    return True
#
def check_valid_input(arg1):
    if break_ip_into_list(arg1) == True:
        print("IP Passed valid check!")
        return True
    else:
        print("IP failed valid check!")
        return False
#
def test_arguments(test_arg1):
    print(f"test: 'arg1' equals: {arg1}")
    if arg1 == "-h" or arg1 == "help":
        print("test: arg1 must be '-h' or 'help'")
        usage()
        exit()
    else:
        print("I got:")
        print(f"test: 'script' equals: {script_name}")
        print(f"test: 'arg1' equals: {arg1}")
        return arg1
#
# 
#                  MAIN
# -----------------------------------------
from sys import argv
#
IP = ""
#
if len(argv) > 2:
    print("test: more than 2 arguments...")
    usage()
    exit()
elif len(argv) == 1:
    print("test: no arguments...so use cli")
    IP = input("Enter an IP address: ")
    if IP == "":
        exit()
    print(f"Test: the input was{IP}")
    valid_check = check_valid_input(IP)
    if valid_check == False:
        print("That was invalid input")
        exit()
else:
    print("test: one argument used...skip cli")
    # get the arg1
    script_name, arg1 = argv
    IP = test_arguments(arg1)
    valid_check = check_valid_input(IP)
    if valid_check == False:
        print("That was invalid input")
        exit()
#
col_h1 = "Octet 1"
col_h2 = "Octet 2"
col_h3 = "Octet 3"
col_h4 = "Octet 4"
print(IP)
ip = IP.split(".")
o1 = int(ip[0])
o2 = int(ip[1])
o3 = int(ip[2])
o4 = int(ip[3])
print()
print("{:^15}{:^15}{:^15}{:^15}".format(col_h1, col_h2, col_h3, col_h4))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(o1, o2, o3, o4))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(o1), bin(o2), bin(o3), bin(o4)))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(o1), hex(o2), hex(o3), hex(o4)))
print()
print()
print()
#