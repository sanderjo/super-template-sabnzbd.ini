# The problem

SABnzbd gives "Failed to connect: [Errno 113] No route to host" errors to ipv6 servers of eweka and newshosting. 
If you set 20 connections per server, most connections succeed, and few gives that error.

<img width="1281" height="250" alt="image" src="https://github.com/user-attachments/assets/a74bfc44-1bae-4ad9-99a1-0943fb6a98a0" />


With testing a lot of different newsservers, the error occurs only on newsservers hosted by eweka/newshosting, not on newsservers hosted by other parties.

So ... a problem on the side of eweka/newshosting?

# Verify yourself

To verify yourself
1. you must working IPv6 within SABnzbd. Verify via Wrench: check that SABnzbd says it has an IPv6 address
2. no need for accounts on the newsservers!
3. stop a running sabnzbd
4. git clone this repo
5. run `python3 create-super-ini.py` to create super.ini
6. run `python3 SABnzbd.py -f super.ini` (plain) or `sabnzbdplus -f super.ini` (Ubuntu) and click the 100MB test download
7. after a minute stop sabnzbd
8. run `parse_sabnzbdlog.sh`


# example results

```
All servers with one or more failed connections:
news6.astraweb.com
news6.easynews.com
news6.eweka.nl
news6.newshosting.com
news6.tweaknews.eu
news6.usenetserver.com

FAILED ... with their ipv6 addresses:
news6.astraweb.com 2001:4de0:1::201
news6.astraweb.com 2001:4de0:1::203
news6.easynews.com 2001:4de0:3:119::76
news6.eweka.nl 2001:4de0:1::204
news6.eweka.nl 2001:4de0:1::233
news6.newshosting.com 2001:4de0:3:119::129
news6.newshosting.com 2001:4de0:3:119::65
news6.newshosting.com 2001:4de0:3:119::97
news6.tweaknews.eu 2001:4de0:3:119::177
news6.usenetserver.com 2001:4de0:3:119::64
news6.usenetserver.com 2001:4de0:3:119::96
```
