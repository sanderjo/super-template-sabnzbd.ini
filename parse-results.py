#!/usr/bin/env python3

import os

logfile = os.path.join("logs", "sabnzbd.log")


# Get everything from latest run, which is after the last "------" line in the log file.
with open(logfile, 'r') as f:
    content = f.read()
    result = content.rsplit('------', 1)[-1]

#print(result)

'''
We need to find lines that look like this:

2026-02-12 07:34:08,461::INFO::[get_addrinfo:198] Fastest connection to news6.eweka.nl (port=563, IPv4 or IPv6): 2001:4de0:1::205 (news6.eweka.nl) in 11ms (out of 3 results)

2026-02-12 07:34:08,612::INFO::[newswrapper:225] Connecting 13@news6.eweka.nl finished
2026-02-12 07:34:08,619::INFO::[newswrapper:225] Connecting 3@news6.eweka.nl finished
2026-02-12 07:34:09,369::WARNING::[newswrapper:674] Failed to connect: [Errno 113] No route to host 31@news6.eweka.nl:563 (news6.eweka.nl)
2026-02-12 07:34:09,369::WARNING::[newswrapper:674] Failed to connect: [Errno 113] No route to host 5@news6.eweka.nl:563 (news6.eweka.nl)
2026-02-12 07:34:09,370::WARNING::[newswrapper:674] Failed to connect: [Errno 113] No route to host 14@news6.eweka.nl:563 (news6.eweka.nl)
2026-02-12 07:34:09,372::WARNING::[newswrapper:674] Failed to connect: [Errno 113] No route to host 22@news6.eweka.nl:563 (news6.eweka.nl)
2026-02-12 07:34:09,608::INFO::[newswrapper:225] Connecting 37@news6.eweka.nl finished
2026-02-12 07:34:09,610::INFO::[newswrapper:225] Connecting 23@news6.eweka.nl finished
'''

# create hashmap of server name to result, where result is "good", "bad" or "fastest".
results = {}
# fill out the hashmap by parsing the log file.

datetime = None

ipv6found = {}
good_connections = {}
bad_connections = {}

print("Analysis of latest SABnzbd run, according to sabnzbd.log:\n")

for line in result.splitlines():
    if not datetime and "INFO" in line:
        # 2026-02-12 20:40:31,243::INFO::[sabnzbdpl...
        datetime = line.split(",")[0]
        print(f"Logging starting at: {datetime}\n")
        # get datetime from line, which is the first 19 characters. datetime = line[:19] print(f"Datetime of latest run: {datetime}")   
    if "Fastest connection to" in line:
        # 2026-02-12 07:34:08,461::INFO::[get_addrinfo:198] Fastest connection to news6.eweka.nl (port=563, IPv4 or IPv6): 2001:4de0:1::205 (news6.eweka.nl) in 11ms (out of 3 results)

        #print(line)
        # split line on spaces, and get the 8th element (index 7), which is the server name in parentheses.
        parts = line.split()
        if len(parts) >= 8:
            server_name = parts[5]
            #print(f"Server name: {server_name}")
            ipv6_address = parts[10]
            #print(f"IPv6 address: {ipv6_address}")
            ipv6found[server_name] = ipv6_address
    # good
    if line.endswith(" finished"):
        #print(line)
        # 2026-02-12 07:34:08,612::INFO::[newswrapper:225] Connecting 13@news6.eweka.nl finished
        # split line on spaces and "@" and get the second element, which is the server name.
        parts = line.split()
        if len(parts) >= 5:
            server_name = parts[-2].split('@')[-1]
            #print(f"Server name: {server_name}")
            # increase count of good connections for this server
            if server_name in good_connections:
                good_connections[server_name] += 1
            else:
                good_connections[server_name] = 1

    # bad
    if "No route to host" in line:
        # 2026-02-12 07:34:09,369::WARNING::[newswrapper:674] Failed to connect: [Errno 113] No route to host 31@news6.eweka.nl:563 (news6.eweka.nl)
        #print(line)
        parts = line.split()
        if len(parts) >= 10:
            server_name = parts[-2]
            # get info between "@" and ":"
            server_name = server_name.split('@')[-1].split(':')[0]
            #print(f"bad Server name: {server_name}")
            # increase count of bad connections for this server
            if server_name in bad_connections:
                bad_connections[server_name] += 1
            else:
                bad_connections[server_name] = 1

# print results
#print("\nResults:")
bad = ""


print("\nThe Good ... :")
for server, ipv6 in ipv6found.items():
    # find server in good_connections and bad_connections, and print counts
    good_count = good_connections.get(server, 0)
    bad_count = bad_connections.get(server, 0)  
    #print(f"{server}: {ipv6} good: {good_count}, bad: {bad_count}")
    output = f"{server}: {ipv6} good: {good_count}, bad: {bad_count}"
    if bad_count == 0:
        # all good, print now
        print(output)
    else:
        # some bad, print later
        bad = bad + output + "\n"
print("\nThe bad:")
print(bad)
