# DCZia-CTF2022
All things CTF for Ziacon 2022
---
* todo:
* hosting of files / sites, do we want to toss into the cloud or localhost (we have my small server)

    ctfd?

    have a ctfj like instance for folks to use who don't have a vm set up?

        make sure to have this all do-able via ubuntu. kali is messy.

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

the last few ctf's we've done are all super vauge and don't really give any hints. thats no fun and doesn't get folks intrested. Jeopardy style are fun but can be a bit repetitive. maybe we can do a bit of layering here and there.

* space house is the HQ for a small group of folks looking to protect the planet from some sort of alien force that have come to take over.
* we've broken into their comms and are looking around
* we found they might be advanced but their security is a bit suspect.

# web

## robots.txt
### learn about robots.txt
this would be find a /robots.txt file that has a user-agent listed for the aliens. via http redirect the aliens are able to get to their comms while anyone else is dropped to a fancy splash page.

something like

```txt
User-agent: Googlebot
Disallow: /(alien-message-system)

User-agent: *
Allow: /

User-agent: (alient-force-name-user-agent)
Allow: /(alien-message-system)
```

solve would look something like:
* using curl to spoof the alien user agent gets us their comms url. have a flag here.
* f12 in browser to change user agent gets us their comms url. have a flag here.

## robots.email
### learn to read an email header and or crack an attachment.

after we get into the aliens comms we would find a bunch of messy files, there would be one that looks sort of normal, turns out its saved email that one left behind

```txt
email header:
have some of the urls point to a url on the network when visited gives a flag

attachment might be fun to have the attachment be an image with a flag

```

# osint scav hunt?

## hidden flags around space house.
* one in the spaceship in the back
* one the name of the person who did the art?
* one on the small shelf in the dining room
* hide on under some of the river rocks in the back yard
* 

# rev / pwn



# forensics

## wireshark.1
### learn a bit about wireshark and how to read them

give a pcap file and ask some questions about it mabye have a flag hiding in a packet header, use tcp stream to give a file that needs to be looked at for a flag (jpg or png)

# misc

## cafe K
### visit cafe K for a drink and chat, maybe he'll give you a flag?

have Will give folks who get a drink a flag

this is just a fun way for some interaction and tasty coffee 

## mattermost / zoom flag

put a flag in the mattermost or maybe zoom chat?


## lock picking box

grab a small lockable box with a pickalbe lock on it

flag and candy inside
