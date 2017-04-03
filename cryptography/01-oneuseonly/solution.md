# One Use Only

**Flag:** `CSCOSU{Hmm, maybe we shouldn't reuse one time pads}`

Nice job! Here is the python script that we used to generate the messages:

```
#!/usr/bin/env python2

# Plain text messages
a1  = bytearray("CSCOSU{Hmm, maybe we shouldn't reuse one time pads}")
a2  = bytearray("This is a secret message but it isn't the answer!!!")
a3  = bytearray("Messages like this are super cool but nt the answer")

# The one time pad we are using multiple times
otp = bytearray("ASKlkdjfs0df0a9812jl3aslkdf)(*012kl3j&(*_ALS!(*!Ljl")

# Make some result bytearrays
b1 = bytearray(len(otp))
b2 = bytearray(len(otp))
b3 = bytearray(len(otp))

# Do the xor one byte at a time
for i in range(0, len(otp)):
    b1[i] = a1[i] ^ otp[i]
    b2[i] = a2[i] ^ otp[i]
    b3[i] = a3[i] ^ otp[i]

# Convert to hex
h1 = "0x" + ', 0x'.join('{:02x}'.format(x) for x in b1)
h2 = "0x" + ', 0x'.join('{:02x}'.format(x) for x in b2)
h3 = "0x" + ', 0x'.join('{:02x}'.format(x) for x in b3)

# Print the results!
print h1
print h2
print h3
```
