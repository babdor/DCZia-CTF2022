# DCZia-CTF2022
All things CTF for Ziacon 2022
---

CTFd: http://ctfd.virus-bucket.biz:8000 (will be https later)

* todo:
    hosting of files / sites, do we want to toss into the cloud or localhost (we have my small server)

    ctfd? https://github.com/CTFd/CTFd
    https://www.hetzner.com/dedicated-rootserver
    https://fly.io/docs/getting-started/python/
    https://github.com/juice-shop/juice-shop as a backup
    

    have a ctfj like instance for folks to use who don't have a vm set up?

    make sure to have this all do-able via ubuntu. kali is messy.

    hugo site is sort of done. `hugo server -D` to have a look at it. We might need to figure out DNS for real or move to aws. Unsure of the time it would take to do either -bab

* prizes?
    stickers
    snacks?
    lock picking set?
* art?
    might ask luna for some art?


---
3-5 challs per topic maybe a some extra ones hiding here in there where they stop and talk to @bab for extra fun prizes


lets get a little theme going.

aliens name: The Galactic Union

since we are at space house this year maybe we can take some sci-fi inspired things and have a bit of fun.

the last few ctf's we've done are all super vague and don't really give any hints. thats no fun and doesn't get folks interested. Jeopardy style are fun but can be a bit repetitive. maybe we can do a bit of layering here and there.

* space house is the HQ for a small group of folks looking to protect the planet from some sort of alien force that have come to take over.
* we've broken into their comms and are looking around
* we found they might be advanced but their security is a bit suspect.

# web

## robotic-lfi

Super simple PHP LFI. No code exec required, just tell it to read the file. Easy!

Runs in a Docker container

## Spring4Shell

The example vulnerable app from https://github.com/reznok/Spring4Shell-POC

Runs in a Docker container

## Robots

This whole thing is a flask app with a Docker container

### robots.txt

There's a file listed in robots.txt that only allows requests from a certain
user agent. Use curl to grab that URL with the listed User-Agent.

### WrongedBruntBotanyEdginess

Once you've got the robots.txt thing figured out, there's another URL in here with a hint to give a codeword (also the robots.txt flag). Curl it to get another flag.

### JoinTheUprising

Two paths here: it contains a MIME encoded email. There's an "X-Bots-Only"
header that leads to /HennaIsolationCatalystSycamoreUnranked (somewhat of a
bonus) and an attached image. The image has a flag in it, no stego or anything,
just read it once you get your MIME decode on.

### HennaIsolationCatalystSycamoreUnranked

Page with an image on it. The image contains a flag in some EXIF data. `strings
-a` like Bab will get it, or you can use something that actually knows the
format.

# Misc

## Roboto-encodo

Pretty simple Cyberchef challenge. No hosting needed, it just lives in ctfd.
There's a README in the subdir for it.

---
# Implemented stuff is ^^
# Ideas are vv
---

# osint / scav hunt?

## hidden flags around space house.
* one in the spaceship in the back
* one the name of the person who did the art?
* one on the small shelf in the dining room
* hide on under some of the river rocks in the back yard
* 

# rev / pwn



# forensics

## Wireshark

Maybe one decent-size pcap with a bunch of challenges in it? Could include some
real-ish cover traffic and an FTP session out somewhere. Auth, upload some
zips, download some executables (and a bash script?). Also maybe some HTTP? Some iodine?

* The captured machine transferred some files in and out. What's the IP they were connecting to? (just find the FTP session and HTTP session to the same place)
* What's the username/password they used for that transfer? (in the FTP stream)
* What file did they transfer out? (passworded Zip uploaded via FTP)
* What's the password to that file? (Get Ancients to flex that 3090 or whatever)
* What's the SHA1 of the thing they downloaded? (Find the HTTP stream, extract the file, SHA1 it)

To prep this we'll need a passworded ZIP to upload containing something
plausible looking, a download (Mimikatz?), and some cover traffic. Meh.

# misc

## cafe K
### visit cafe K for a drink and chat, maybe he'll give you a flag?

have Will give folks who get a drink a flag

this is just a fun way for some interaction and tasty coffee 

## mattermost / zoom flag

put a flag in the mattermost or maybe zoom chat?


## lock picking box

grab a small lockable box with a pickable lock on it

flag and candy inside

