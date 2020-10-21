#!/usr/bin/python

# Copyright (c) 2020 Gregor Hildebrand

import socket

def returnBanner(ip,port):
	try:
		socket.setdefaulttimeout(1) # default-timeout in seconds
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024) # receiving data in bytes
		return banner
	except:
		return


def main():
	# type in the ipv4-addr
	ip = raw_input("[*?*] Enter ip-addr: ")
	# scanning specified port
	port = int(raw_input("[*?*] enter port number: "))
	banner = returnBanner(ip,port)
	if banner:
		print("[+]" + ip + ": " + banner)
main()
