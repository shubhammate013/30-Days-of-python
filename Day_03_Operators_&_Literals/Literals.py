## Literals

#Literal is a raw data given in a variable. In Python, there are various types of literals they are as follows:
# - Numeric Literals
# - String Literals
# - Boolean Literals
# - Special Literals


# 1. Numeric Literals

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

print(a, b, c, d)


#Float Literal
float_1 = 10.5 
float_2 = 1.5e2
float_3 = 1.5e-3

print(float_1, float_2,float_3)

#Complex Literal 
x = 3.14j

print(x, x.imag, x.real)

### 2. String Literals

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


### 3. Boolean Literal

a = True + 4
b = False + 10

print("a:", a)
print("b:", b)


### 4. Special Literal

a = None
print(a)

c = 34+45





