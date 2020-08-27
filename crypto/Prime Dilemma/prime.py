from Crypto.Util.number import inverse
import binascii

e = 6969
c = 12541396840306196572
n = 19127742752993891878

# From factordb

p = 2
q = 9563871376496945939

phi = (p-1) * (q-1)

d = inverse(e,phi)
m = pow(c,d,n)

hex_str = hex(m)[2:] # Removing '0x'
print(binascii.unhexlify(hex_str))
