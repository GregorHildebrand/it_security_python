#!/usr/bin/python

# Copyright (c) 2020 Gregor Hildebrand
# It is a beginner python program what is scanning one port on a specific ip-addr

import socket

# for IPv4-addr and TCP-Packets; TCP-Handshake for one port is executed
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "given_ip_addr"
port = whatever_port_number

def portscanner(port):
	if sock.connect_ex((host,port)):
		print("Port %d is closed" %(port))
	else:
		print("Port %d is opened" %(port))

portscanner(port)
