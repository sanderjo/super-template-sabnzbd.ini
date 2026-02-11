SABnzbd gives "Failed to connect: [Errno 113] No route to host" errors to ipv6 servers of eweka and newshosting. 
And if you set 20 connections per server, most connections succeed, and few gives that error.

With testing a lot of different newsservers, the error occurs only on newsservers hosted by eweka/newshosting, not on newsservers hosted by other parties.

So ... a problem on the side of eweka/newshosting?

To verify yourself
1. you must working IPv6
2. stop a running sabnzbd
3. git clone this repo
4. run `python3 create-super-ini.py` to create super.ini
5. run `sabnzbdplus -f super.ini` and click the 100MB test download
6. after a minute stop sabnzbd
7. run `parse_sabnzbdlog.sh`

<img width="1281" height="250" alt="image" src="https://github.com/user-attachments/assets/a74bfc44-1bae-4ad9-99a1-0943fb6a98a0" />
