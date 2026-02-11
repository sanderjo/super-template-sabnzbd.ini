supergoal = "super.ini"

# read in "pre.template"

print(supergoal)

newsservers = [
    "news6.eweka.nl",
    "news6.newshosting.com",
    "news-v6.frugalusenet.com",
    "us6.astraweb.com",
    "news6.easynews.com",
    "news6.astraweb.com",
    "news6.tweaknews.eu",
    "news6.usenet.farm",
    "news6.usenetserver.com",
    "reader6.newsxs.nl",
]


with open("pre.template", 'r') as file:
    pre = file.read()

with open("post.template", 'r') as file:
    post = file.read()

all_servers = ""
with open("newsservers.template", 'r') as file:
    onenewsserver = file.read()
    for server in newsservers:
        print(server)
        filled_out = onenewsserver.replace("XXX", server)
        all_servers = all_servers + filled_out

fulloutput = pre + all_servers + post

with open(supergoal, 'w') as file:
    file.write(fulloutput)
