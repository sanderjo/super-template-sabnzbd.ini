#!/usr/bin/env python3
import http.client
import socket

def get_public_ipv6():
    remote_host = "self-test.sabnzbd.org"
    remote_port = 80  # Plain HTTP, to keep code simple and avoid SSL complications
    my_public_ip = None    
    try:
        addr_info = socket.getaddrinfo(remote_host, remote_port, socket.AF_INET6, socket.SOCK_STREAM)
        ipv6_addr = addr_info[0][4][0]
        conn = http.client.HTTPConnection(f"[{ipv6_addr}]", remote_port, timeout=3)        
        conn.request("GET", "/", headers={"Host": remote_host})        
        response = conn.getresponse()
        my_public_ip = response.read().decode('utf-8')
        conn.close()        
    except Exception as e:
        pass
    return my_public_ip


def get_ipv6_prefix():
    if my_ipv6_address := get_public_ipv6():
        #print(f"Your public IPv6 address is: {my_ipv6_address}")
        prefix = ":".join(my_ipv6_address.split(":")[:3]) + ":"
        #print(f"Your IPv6 prefix is: {prefix}...")
        return prefix
    else:        
        #print("Could not determine your public IPv6 address. You may not have IPv6 connectivity or there was an error during the test.")
        return None

if __name__ == "__main__":
    print(get_ipv6_prefix())