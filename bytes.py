""""
Learn about bytes
Bytes are similar to str type, but they are a sequence of bytes instead of Unicode points.

Use for raw binary data, fixed-width, single-byte encoding: ASCII

Use the byte() constructor
"""

d = b'data'
print(d, type(d))


info = b'some bytes here'
#split the bytes using split()method for bytes
print (info.split())


# Encoding
message = "Vamos al zoológico"
print(message)
data = message.encode("utf-8")
print(data)
print(data.decode())


