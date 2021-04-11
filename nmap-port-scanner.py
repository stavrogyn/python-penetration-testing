import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')
print('<-------------------------------------------->')

ip_addr = inpur('PLease enter the ip address that you want to scan: ')
print(f'The ip was entered is - {ip_addr}')
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""").strip()
print('You have selected options: ', resp)

if resp == '1':
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp == '1':
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['udp'].keys())
elif resp == '1':
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print('Open Ports: ', scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print('Please enter a valid option')
