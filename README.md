# DCZia-CTF2022
All things CTF for Ziacon 2022

---
lets get a little theme going.

since we are at space house this year maybe we can take some sci-fi inspired things and have a bit of fun.

the last few ctf's we've done are all super vauge and don't really give any hints. thats no fun and doesn't get folks intrested. Jeopardy are cool but giving things a bit of layering is cooler.

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

User-agent: (alient-force-name-user-agent)
Allow: /(alien-message-system)
```

solve would look something like:
* using curl to spoof the alien user agent
* f12 in browser to change user agent

## robots.txt.2
### learn to read an email header and or crack an attachment.

after we get into the aliens comms we would find a bunch of messy files, there would be one that looks sort of normal 

# osint

# rev

# forensics 

# misc
