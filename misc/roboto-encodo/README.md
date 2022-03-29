20220327 

---

# ROBOTO.ENCODO

A fun way to get folks looking at cyberchef. 

This challenge looks quite hard at first. We wanted the text to be sort of messy but odd looking. The first thing folks should notice is that its heavly encoded, lots of repating might throw you off a bit but it was done on purpose.

There is a free hint on the ctfd that suggests looking at cyberchef. From there when you paste the text in the output should give a magic symbol the do part of the decode for you. Hitting it once will get you 3/5ths of the way there. Notice that its still there, giving it a 2nd hit will get you 4/5ths there. Now you have something look A LOT like a flag but not. ROT13 is your friend. 

```
MzEgMzQgMzUgMjAgMzEgMzEgMzQgMjAgMzEgMzQgMzcgMjAgMzEgMzQgMzUgMjAgMzEgMzEgMzMgMjAgMzEgMzYgMzMgMjAgMzEgMzQgMzUgMjAgMzEgMzQgMzUgMjAgMzYgMzcgMjAgMzEgMzYgMzUgMjAgMzcgMzAgMjAgMzEgMzAgMzMgMjAgMzEgMzMgMzIgMjAgMzYgMzQgMjAgMzEgMzAgMzQgMjAgMzEgMzcgMzIgMjAgMzEgMzQgMzIgMjAgMzEgMzIgMzUgMjAgMzEgMzIgMzQgMjAgMzEgMzYgMzIgMjAgMzEgMzYgMzAgMjAgMzEgMzIgMzYgMjAgMzEgMzQgMzcgMjAgMzEgMzAgMzEgMjAgMzEgMzYgMzAgMjAgMzEgMzcgMzIgMjAgMzEgMzUgMzIgMjAgMzEgMzQgMzYgMjAgMzEgMzYgMzQgMjAgMzEgMzYgMzIgMjAgMzEgMzUgMzYgMjAgMzEgMzMgMzAgMjAgMzEgMzYgMzAgMjAgMzEgMzMgMzAgMjAgMzEgMzQgMzQgMjAgMzEgMzYgMzUgMjAgMzEgMzQgMzMgMjAgMzEgMzEgMzYgMjAgMzEgMzYgMzQgMjAgMzEgMzEgMzUgMjAgMzEgMzAgMzYgMjAgMzYgMzQgMjAgMzEgMzQgMzIgMjAgMzEgMzQgMzcgMjAgMzEgMzAgMzcgMjAgMzEgMzUgMzMgMjAgMzcgMzEgMjAgMzEgMzMgMzAgMjAgMzEgMzQgMzMgMjAgMzYgMzcgMjAgMzEgMzQgMzQgMjAgMzYgMzYgMjAgMzEgMzIgMzIgMjAgMzEgMzYgMzEgMjAgMzEgMzMgMzEgMjAgMzYgMzUgMjAgMzEgMzEgMzYgMjAgMzEgMzEgMzMgMjAgMzEgMzUgMzMgMjAgMzEgMzQgMzUgMjAgMzEgMzUgMzEgMjAgMzYgMzIgMjAgMzEgMzYgMzQgMjAgMzEgMzYgMzQ
```

```
https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)To_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')To_Octal('Space')To_Hex('Space',0)To_Base64('A-Za-z0-9%2B/%3D')&input=WmlhQ1RGe1NsdXJwIEJsZWVwIFB1bG1vbmFyeSBSZXZlcmVuZCBSb3VuZGlzaH0
```

# TODO:
* screen shots for write-up
* Do a bit of fun automation with 