from collections import defaultdict
from spellchecker import SpellChecker
from itertools import product
spell = SpellChecker()

char_set = ["A", "B", "C", "D", "E"]
char_set_26 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
inv_freq_table = {
    "A": ["B", "N", "T", "S", "P", "X", "A", "O", ],
    "B": ["C", "O", "U", "T", "L", "Y", "B", "P", ],
    "C": ["D", "P", "Q", "U", "M", "Z", "C", "L", ],
    "D": ["E", "L", "R", "Q", "N", "V", "D", "M", ],
    "E": ["A", "M", "S", "R", "O", "W", "E", "N", ],
    "F": ["G", "S", "Y", "X", "U", "C", "F", "T", ],
    "G": ["H", "T", "Z", "Y", "Q", "D", "G", "U", ],
    "H": ["I", "J", "U", "V", "Z", "R", "E", "H", "Q", ],
    "I": ["K", "Q", "W", "V", "S", "A", "I", "J", "R", ],
    "J": [],
    "K": ["F", "R", "X", "W", "T", "B", "K", "S", ],
    "L": ["M", "X", "D", "C", "Z", "H", "L", "Y", ],
    "M": ["N", "Y", "E", "D", "V", "I", "J", "M", "Z", ],
    "N": ["O", "Z", "A", "E", "W", "K", "N", "V", ],
    "O": ["P", "V", "B", "A", "X", "F", "O", "W", ],
    "P": ["L", "W", "C", "B", "Y", "G", "P", "X", ],
    "Q": ["R", "C", "I", "J", "H", "E", "N", "Q", "D", ],
    "R": ["S", "D", "K", "I", "J", "A", "O", "R", "E", ],
    "S": ["T", "E", "F", "K", "B", "P", "S", "A", ],
    "T": ["U", "A", "G", "F", "C", "L", "T", "B", ],
    "U": ["Q", "B", "H", "G", "D", "M", "U", "C", ],
    "V": ["W", "H", "O", "N", "K", "S", "V", "I", "J", ],
    "W": ["X", "I", "J", "P", "O", "F", "T", "W", "K", ],
    "X": ["Y", "K", "L", "P", "G", "U", "X", "F", ],
    "Y": ["Z", "F", "M", "L", "H", "Q", "Y", "G", ],
    "Z": ["V", "G", "N", "M", "I", "J", "R", "Z", "H", ]
}
freq_table_alpha_26 = {
    "A": 8.167,
    "B": 1.492,
    "C": 2.782,
    "D": 4.253,
    "E": 12.702,
    "F": 2.228,
    "G": 2.015,
    "H": 6.094,
    "I": 6.966,
    "J": 0.153,
    "K": 0.772,
    "L": 4.025,
    "M": 2.406,
    "N": 6.749,
    "O": 7.507,
    "P": 1.929,
    "Q": 0.095,
    "R": 5.987,
    "S": 6.327,
    "T": 9.056,
    "U": 2.758,
    "V": 0.978,
    "W": 2.360,
    "X": 0.150,
    "Y": 1.974,
    "Z": 0.074
}


def pad(plaintext, key_size):
    len_last_block = len(plaintext) % key_size
    left = key_size - len(len_last_block)
    return plaintext + left * "A"


def char_convert(ch):
    num = ord(ch) - 65
    ch_5 = ""
    if num < 9:
        ch_5 = char_set[num // 5] + char_set[num % 5]
    else:
        num -= 1
        ch_5 = char_set[num // 5] + char_set[num % 5]
    return ch_5


def char_revert(ch):
    num_1 = (ord(ch[0]) - 65)
    num_2 = (ord(ch[1]) - 65)
    num = num_1 * 5 + num_2
    if num >= 9:
        num += 1
    return chr(num + 65)


def revert(text_5):
    text_26_list=[]
    text_5_lst = text_5.split()
    for text_5_word in text_5_lst:
        text_26_word = ""
        for i in range(0, len(text_5_word), 2):
            seq = text_5_word[i] + text_5_word[i + 1]
            text_26_word += char_revert(seq)
        text_26_list.append(text_26_word)
    text_26=' '.join(text_26_list)
    return text_26


def convert(text_26):
    text_5 = ""
    for i in text_26:
        if i == " ":
            text_5+=" "
        else:
            text_5 += char_convert(i)
    return text_5


def encrypt(plaintext, key):
    units = len(plaintext) // len(key)
    excess = len(plaintext) - len(key) * units
    if excess > 0:
        plaintext = pad(plaintext=plaintext, key_size=len(key))
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i] == " ":
            ciphertext += " "
        else:
            ciphertext += chr(((ord(plaintext[i]) - 65 + ord(key[i % len(key)]) - 65) % 5) + 65)
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
        else:
            plaintext += chr(((ord(ciphertext[i]) - 65 - ord(key[i % len(key)]) + 65) % 5) + 65)
    return plaintext


def freq_table(given_text):
    freq_table_text = defaultdict(lambda: 0, {})
    for i in range(0, len(given_text)):
        freq_table_text[given_text[i]] += 1
    max_index = given_text[0]
    for i in freq_table_text:
        if freq_table_text[i] > freq_table_text[max_index]:
            max_index = i
    return max_index


def max_freq(given_text):
    freq_table_text = defaultdict(lambda: 0)
    for i in range(0, len(given_text), 2):
        freq_table_text[given_text[i:i + 2]] += 1
    for i in freq_table_text:
        print(i, revert(i), freq_table_text[i])


def index_return(given_text):
    freq_table_text = defaultdict(lambda: 0, {})
    for i in range(0, len(given_text), 2):
        ch = char_revert(given_text[i:i + 2])
        freq_table_text[ch] += 1
    sum_coincide = 0
    n = len(given_text) / 2
    for i in freq_table_text:
        sum_coincide += (freq_table_text[i] * (freq_table_text[i] - 1)) / 2
    return sum_coincide / (n * (n - 1) / 2)


def len_analyze(ciphertext):
    index_incidence = index_return(given_text=''.join(ciphertext.split()))
    n = len(ciphertext) / 2
    l = (0.02654 * n) / ((0.065 - index_incidence) + n * (index_incidence - 0.03846))
    print(l)
    return int(l // 1)


def break_cipher(ciphertext, length):
    string_set = revert(ciphertext)
    string_set=''.join(string_set.split())
    ciphertext_words = ciphertext.split()
    string_set_length = [""] * length
    for i in range(length):
        for j in range(i, len(string_set) - i, length):
            string_set_length[i] += string_set[j]
    max_set_length = [inv_freq_table[freq_table(string_set_length[i])] for i in range(length)]
    key_set_tuple = list(product(*max_set_length))
    key_set=[]
    key_set_sieve = {}
    for i in key_set_tuple:
        key_set.append(''.join(i))
    for i in key_set:
        decrypt_set = decrypt(ciphertext=ciphertext,key=convert(i)).split()
        decrypt_lower_list = [revert(decrypt_text).lower() for decrypt_text in decrypt_set]
        decrypt_correct_set = spell.known(decrypt_lower_list)
        decrypt_lower_set = set(decrypt_lower_list)
        if len(decrypt_lower_set) == len(decrypt_correct_set):
            key_set_sieve.update({i:revert(' '.join(decrypt_set))})
    print(key_set_sieve)
    # max_freq(given_text=convert(string_set_length[1]))


plain_text = "THE TRUTH IS ALWAYS SOMETHING THAT IS TOLD NOT SOMETHING THAT IS KNOWN IF THERE WERE NO SPEAKING OR WRITING THERE WOULD BE NO TRUTH ABOUT ANYTHING THERE WOULD ONLY BE WHAT IS"
plain_text_5 = convert(plain_text)
key_26 = "OP"
key_5 = convert(key_26)
print(len(plain_text_5))
encrypt_5 = encrypt(plaintext=plain_text_5, key=key_5)
str_1 = ["E", "T", "N", "O", "R", "I", "A", "S"]
table_1 = ""
print(revert(decrypt(encrypt_5,key_5)) == plain_text)
print(len_analyze(encrypt_5))
break_cipher(ciphertext=encrypt_5,length=len_analyze(encrypt_5))


def gen_inverse_set():
    for ch in char_set_26:
        print(ch, end=": ")
        print("[", end="")
        for i in str_1:
            for j in char_set_26:
                ch_1 = convert(i)
                ch_2 = convert(j)
                ch_3 = encrypt(ch_1, ch_2)
                if revert(ch_3) == ch:
                    print('"{}"'.format(j), end=", ")
        print("],")
    # max_freq(table_1)
