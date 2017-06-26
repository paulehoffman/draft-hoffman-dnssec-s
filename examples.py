#!/usr/bin/env python3

import hashlib, base64

def HexOfByteString(ByteString):
	return("".join([ "%02x" % (int(x)) for x in bytearray(ByteString) ]))

thash = hashlib.sha256()
thash.update(bytes())  # Yes, that's a boring string

print("The hex of the hash is {}".format(HexOfByteString(thash.digest())))

print("The base32 of the hash is {}".format((base64.b32encode(thash.digest())).decode("latin-1")))

