import binascii

# Copy supplied RSA parameters
p = int("0xC5A047A7C52ED3A2875F7D76C47B555F", 16)  # First prime
q = int("0xC93268355C09197BBF1659B5522FFACD", 16)  # Second prime
e = int("0x010001", 16)  # A number that is co-prime with (p-1)*(q-1)
d = int("0x0D067636BAC6088AD2281E4BFFCACFEFEF9BC1A69FB9E701063DFBAAB436E4C1", 16)  # Decryption key
enc = int("0x50543d1e0fda637c109bb32c706dbaec8d8d20ce001cca02f8576a4852a072c9", 16)  # Encrypted message
n = p * q  # Modulus

# Print n, d and check d*e mod (p-1)*(q-1)
print("n is: " + str(n))
print("d is: " + str(d))
print("checking d*e mod (p-1)*(q-1): " + str((d * e) % ((p - 1) * (q - 1))))

# Decrypt message using private exponent d
plain = pow(enc, d, n)

# Convert plain (in int) to str byte-wise by first representing int as hex, then converting that to ascii
decrypted_message_hex = format(plain, 'x')  # Convert to hex format
decrypted_message = binascii.unhexlify(decrypted_message_hex)  # Convert hex to bytes
print("Cipher " + str(enc) + " is decrypted to: " + decrypted_message.decode())
