import string
from collections import Counter
import os

# Clear screen based on windows, linux and mac
os.system('cls' if os.name=='nt' else 'clear')

# Frequencies of english letters to use for calculating Φ
english_letters_frequency = {
    'a': 0.08,
    'b': 0.015,
    'c': 0.03,
    'd': 0.04,
    'e': 0.13,
    'f': 0.02,
    'g': 0.015,
    'h': 0.06,
    'i': 0.065,
    'j': 0.005,
    'k': 0.005,
    'l': 0.035,
    'm': 0.03,
    'n': 0.07,
    'o': 0.08,
    'p': 0.02,
    'q': 0.002,
    'r': 0.065,
    's': 0.06,
    't': 0.09,
    'u': 0.03,
    'v': 0.01,
    'w': 0.015,
    'x': 0.005,
    'y': 0.02,
    'z': 0.002
}

# Secrets to decode.
secret1 = 'HdxmjnjaoZsxcvibznzmqzm'.lower()
secret2 = 'KfpjSjykqncfuutsUqfdXytwjhfzlmymnofhpnslBmfyxFuuxjxxntsx'

# Choose which secret you want to decipher
# secret = secret2

def plain_text_by_key(secret, key):
    """
    Decipher secret base on the given key by Caesar Algorithm
    """
    result = []
    for char in secret:
        if char.islower():
            base = ord('a')
        else:
            base = ord('A')
        result.append(chr((((ord(char)-base)+key) % 26)+base))

    return ''.join(result)

def get_frequencies_sorted(text):
    """
    Calculate frequencies and sort the results based on the frequencies found to disply better
    """
    text = text.lower()
    text_freq = list(map(lambda item: (item[0], round(
        item[1]/len(text), 2)), Counter(text).items()))
    text_freq_dict = dict(text_freq)

    text_freq_dict_all_chars = list()
    for char in string.ascii_lowercase:
        text_freq_dict_all_chars.append(
            (char, text_freq_dict[char] if char in text_freq_dict else 0))

    return sorted(text_freq_dict_all_chars, key=lambda item: item[1], reverse=True)


secret1_letters_freq_sorted = get_frequencies_sorted(secret1)


def calc_fi(secret_text, key):
    """
    Calculate Φ based on the given secret and key.
    """
    secret_text_freq_dict = dict(get_frequencies_sorted(secret_text))
    plain_text_moved_by_key = plain_text_by_key(secret_text, key)

    letter_decipher_counterpart = dict(zip(secret_text.lower(), plain_text_moved_by_key.lower()))

    fi = 0
    for i, (eng_letter, eng_letter_freq) in enumerate(english_letters_frequency.items()):
        if eng_letter in secret_text.lower():
            fi += secret_text_freq_dict[eng_letter] * \
                english_letters_frequency[letter_decipher_counterpart[eng_letter].lower()]

    return fi

def choose_secret():
    print('---Decipher with Caesar algorithm.---\n')
    print('You can enter a custom secret or use the default ones.')
    print('Sample secrets: (enter single digit number to select these)')
    print('\t', '1.', secret1)
    print('\t', '2.', secret2)
    print('Or enter you own secret.')
    user_secret = input('Enter the secret to decipher:')

    if len(user_secret) == 1:
        if user_secret == '1':
            return secret1
        if user_secret == '2':
            return secret2
    return user_secret


def get_spaces_index_and_remove(secret):
    return list(map(lambda x: x[0], filter(lambda item: item[1]==' ',  enumerate(list(secret)))))

def insert_spaces_into_result(text, spaces_indexes):
    text_letters = list(text)

    for index in spaces_indexes:
        text_letters.insert(index, ' ')

    return ''.join(text_letters)


if __name__ == '__main__':
    secret = choose_secret()
    # secret = secret.lower()

    spaces_indexes = get_spaces_index_and_remove(secret)
    secret = secret.replace(' ', '')

    print('\n', '-'*30, '\n')
    deciphers_with_fi_numbers = list()

    for i in range(26):
        decipher_text = plain_text_by_key(secret, i)
        fi = calc_fi(secret, i)
        deciphers_with_fi_numbers.append((i, fi, decipher_text))

    for key, fi, decipher in sorted(deciphers_with_fi_numbers, key=lambda x: x[1], reverse=True):
        print(f'key: {key:2} | fi: {fi:5.4} | decipher: {insert_spaces_into_result(decipher, spaces_indexes)}')

    print('\n', '-'*30, '\n')

    print('Results are sorted based on the Φ value. The correct text should be in the first results.')
