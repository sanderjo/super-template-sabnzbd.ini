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
6. run `python3 SABnzbd.py -f super.ini` (plain) or `sabnzbdplus -f super.ini` (Ubuntu)
7. In the SABnzbd GUI: click the 100MB test download
8. after a minute stop sabnzbd. Note: no logins for those servers, so no download (and loging errors).
9. run `python3 parse-results.py` to see the results

In short:
```
./create-super-ini.py # creates super.ini
sabnzbdplus -f super.ini # in the SAB GUI: let it try to download the 100MB test file, and stop SABnzbd after a minute
./parse-results.py  | rev | sort -k1,1n | rev
```


# example results

```
sander@x360:~/git/ipv6-tests-newshosting-eweka$ ./parse-results.py  | rev | sort -k1,1n | rev
reader6.newsxs.nl: 2001:67c:174:101:0:65:ff02:122 good: 0, bad: 0
eunews-v6.blocknews.net: 2607:bc40:2:119::1:1 good: 40, bad: 0
news-v6.frugalusenet.com: 2607:bc40:0:119::2:3 good: 40, bad: 0
eunews-v6.usenetnow.net: 2607:bc40:2:119::3:4 good: 40, bad: 0
news6.usenet.farm: 2a00:1d38:fa:1001:119::4 good: 40, bad: 0
news6.tweaknews.nl: 2001:4de0:3:119::176 good: 40, bad: 0
news6.tweaknews.eu: 2001:4de0:3:119::177 good: 40, bad: 0
news6.dwld.link: 2a13:d6c0:1:16::119 good: 40, bad: 0

eu6.astraweb.com: 2001:4de0:1::203 good: 39, bad: 1
news6.pureusenet.nl: 2001:4de0:3:119::164 good: 39, bad: 1
news6.usenetserver.com: 2001:4de0:3:119::64 good: 39, bad: 1
news6.xlned.com: 2001:4de0:3:119::172 good: 38, bad: 2
news6.sunnyusenet.com: 2001:4de0:3:119::173 good: 38, bad: 2
news6.eweka.nl: 2001:4de0:1::204 good: 37, bad: 3
news6.easynews.com: 2001:4de0:3:119::76 good: 35, bad: 5
news6.newshosting.com: 2001:4de0:3:119::129 good: 32, bad: 8
```

So:
* all eweka/newshosting servers (starting with 2001:4de0:): at least 1 bad IPv6 connection
* all non-eweka/newshosting servers: all connections good

Conincidence? I think not.
