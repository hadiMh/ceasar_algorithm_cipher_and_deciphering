secret = 'HdxmjnjaoZsxcvibznzmqzm'

# by observing the results you see the key is 5
for i in range(26):
    result = []
    for char in secret:
        if char.islower():
            base = ord('a')
        else:
            base = ord('A')
        result.append(chr((((ord(char)-base)+i) % 26)+base))

    print(f'key={i:3} plaintext=', ''.join(result))