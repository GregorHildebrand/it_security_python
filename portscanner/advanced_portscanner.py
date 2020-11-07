#!/usr/bin/python

# developed in 2020 by: Gregor Hildebrand

import socket, optparse, threading
from termcolor import colored

# first of all set timeout for the scanning process on one  second
socket.setdefaulttimeout(1)

def connScan(host,port):
	try:
		# ipv4-addr and tcp packets
		# setting variable to global to prevent UnboundLocalError
		global sock
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((host,port))
		print(colored(f"[**] {port}/tcp is open", 'green'))
	except:
		print(colored(f"[--] {port}/tcp is closed", 'red'))
	finally:
		sock.close()

# gethostbyname() returns ipv4-addr of host
# gethotsbyaddr() returned a list: first element is hostname, second element is alias list for ip-addr, third element is ip-addr of the host
def portScan(host,ports):
	try:
		chosen_IP = socket.gethostbyname(host)
	except:
		print(f"Unknown host: {host}")
	try:
		chosen_Name = socket.gethostbyaddr(chosen_IP)
		print(f"[**] Scan Results for: {chosen_Name[0]} ")
	except:
		print(f"[**] Scan Results for: {chosen_IP}")
	for port in ports:
		t = threading.Thread(target=connScan, args=(host,int(port)))
		t.start()

def main():
	parser = optparse.OptionParser("Usage for scanning specified host and ports: python3 <the_script> -H <chosen host> -p <chosen ports>\nUsage for scanning all ports on specified host: "+"python3 <the_script> -H <chosen host> -a")
	parser.add_option("-H", dest="chosenHost", type="string", help="specify your host")
	parser.add_option("-p", dest="chosenPorts", type="string", help="specify your ports, separated by comma")
	# action="store_true" for setting option as boolean flag
	parser.add_option("-a", action="store_true", dest="allports", help="scan all ports on specified host")
	(options, args) = parser.parse_args()
	chosen_Host = options.chosenHost
	chosen_Ports = str(options.chosenPorts).split(',')
	# allports is class 'bool'
	# valid portnumbers: 0 to 65535
	if (options.allports == True):
		# ipv4-addr and tcp packets
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		for all_p in range(0,65536):
			t = threading.Thread(target=connScan, args=(chosen_Host,all_p))
			t.start()
		exit(0)
	# check, if host and at least one port is specified
	# None = absence of a value
	if (chosen_Host == None) | (chosen_Ports[0] == None):
		print(parser.usage)
		exit(0)
	portScan(chosen_Host, chosen_Ports)

if __name__ == '__main__':
	main()
