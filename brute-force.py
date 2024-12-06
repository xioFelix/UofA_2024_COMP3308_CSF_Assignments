#!/usr/bin/env python3
import sys, socket, itertools

socket.setdefaulttimeout(0.1)  # set timeout to 100ms
def dns_brute_force(domain, subdomain):
    host = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(host)
        print(f"{host} resolves to {ip}")
    except socket.error:
        pass  # ignore error

# Main
if __name__ == "__main__":
    domain = "adelaide.edu.au"
    dictionary_path = "dnsmap.txt"

    with open(dictionary_path, "r") as file:
        for line in file:
            subdomain = line.strip()
            dns_brute_force(domain, subdomain)