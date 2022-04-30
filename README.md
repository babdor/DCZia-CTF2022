# DCZia-CTF2022
All things CTF for Ziacon 2022
---

CTFd: http://ctfd.virus-bucket.biz:8000 (will be https later)

---
3-5 challs per topic maybe a some extra ones hiding here in there where they stop and talk to @bab for extra fun prizes


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

# misc

## Roboto-encodo

Pretty simple Cyberchef challenge. No hosting needed, it just lives in ctfd.
There's a README in the subdir for it.

# forensics

## Robotic magic
This is a small challange to take a quick look at magic bytes in a file

---
# Implemented stuff is ^^
# Ideas are vv
---

# osint

## dragon on the rails

Have folks find a neat train that leaves from Santa Fe

## buffalo island

Find an island of buffalos!

# forensics

## Robotic magic
This is a small challange to take a quick look at magic bytes in a file

