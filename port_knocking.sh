#!/bin/bash

# Target IP address
IP="192.168.66.2"

# Port knocking sequenced
sudo nmap -sS -Pn $IP -p 2201
sudo nmap -sS -Pn $IP -p 2211
sudo nmap -sS -Pn $IP -p 2234

# Connect to the opened port using netcat
nc $IP 12345