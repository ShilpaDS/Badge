#covert a number in to str type
x = 10
print(type(x))
y = str(x)
print(type(y))


#print Unicode of the character 'm'
print(ord('m'))

# print character representation of given unicode 100
print(chr(100))

# print any number and its binary equivalent
print(bin(15))

# print any number and its octal equivalent
print(oct(15))

# print any number and its hexadecimal equivalent
print(hex(12))

# store a binary number 1100101 in a variable and print it in decimal format
b = 0b1100101
print(b)

# store a hexadecimal number 2F in a variable and print it in octal format
h = 0x2F
print(oct(h))

# store a octal number 125 in a variable and print it in binary format
o = 0o125
print(bin(o))

# add two numbers 25(in octal) and 39(in hexadecimal) and print result in binary format
print(bin((0o25) + (0x39)))
