#!/bin/env python3

import os
multiipv6onlysabgoal = "multiipv6onlysab.ini"
templatedir = "templates"



# read in "pre.template"

print(multiipv6onlysabgoal)

newsservers = [
    "news6.eweka.nl",
    "news6.dwld.link",
    "news6.xlned.com",
    "eu6.astraweb.com",
    "news6.usenet.farm",
    "reader6.newsxs.nl",
    "news6.easynews.com",
    "news6.tweaknews.eu",
    "news6.tweaknews.nl",
    "news6.pureusenet.nl",
    "news6.newshosting.com",
    "news6.sunnyusenet.com",
    "news6.usenetserver.com",
    "eunews-v6.blocknews.net",
    "eunews-v6.usenetnow.net",
    "news-v6.frugalusenet.com",
]


with open(os.path.join(templatedir, "pre.template"), 'r') as file:
    pre = file.read()

with open(os.path.join(templatedir, "post.template"), 'r') as file:
    post = file.read()

all_servers = ""
with open(os.path.join(templatedir, "newsservers.template"), 'r') as file:
    onenewsserver = file.read()
    for server in newsservers:
        print(server)
        filled_out = onenewsserver.replace("XXX", server)
        all_servers = all_servers + filled_out

fulloutput = pre + all_servers + post

with open(multiipv6onlysabgoal, 'w') as file:
    file.write(fulloutput)
    
print(f"Successfully created {multiipv6onlysabgoal}")