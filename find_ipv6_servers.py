#!/bin/env python3
# read file "ipv6-only-newsservers.txt"
with open("ipv6-only-newsservers.txt", 'r') as f:
    ipv6_only_newsservers = f.read().splitlines()

# sort on lenght, shortest first, to get the most general ones first.
ipv6_only_newsservers.sort(key=len)

shortest = {}
for server in ipv6_only_newsservers:
    #print(server)
    domain = server.split('.')[-2] + "." + server.split('.')[-1]
    #print(domain)
    if domain not in shortest:
        shortest[domain] = server

print("Shortest:")
for domain, server in shortest.items():
    print(f"\"{server}\",")