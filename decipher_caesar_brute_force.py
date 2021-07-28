secret = ".4)/C+g-;)x'i1v0k:y'2=yz')xk6z';k+{:kF`OE"


def shift_str(txt, key=0):
    chars = list(txt)

    final = []

    for char in chars:
        if ord(char)+key > ord('z'):
            final.append((chr(ord(char)+key-(ord('z')-ord('A')+5))))
        else:
            final.append((chr(ord(char)+key)))

    return ''.join(final)

if __name__ == '__main__':
    for i in range(128):
        # already found the key by observing all the results
        if i == 24:
            print(f'{i}.', shift_str(secret, i))
