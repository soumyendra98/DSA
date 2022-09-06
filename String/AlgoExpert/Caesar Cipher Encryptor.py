# ASCII | O(N) and O(N)
def caesarCipherEncryptor(string, key):
    # Write your code here.hgh
    output = ''
    for i in string:
        if ord(i) < 97:
            ascii_val = (ord(i) + key - 65) % 26
            output += chr(65 + ascii_val)
        else:
            ascii_val = (ord(i) + key - 97) % 26
            output += chr(97 + ascii_val)
    return output


str1 = 'zab'
key = 2
print(caesarCipherEncryptor(str1, key))
