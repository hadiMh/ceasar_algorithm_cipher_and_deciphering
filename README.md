# Caesar Algorithm - Ciphering & Deciphering
![python version](https://img.shields.io/static/v1?label=python&message=3.8&color=2196F3)
![code size](https://img.shields.io/github/languages/code-size/hadiMh/ceasar_algorithm_cipher_and_deciphering?color=2196F3)
![license](https://img.shields.io/static/v1?label=license&message=MIT&color=green)
### by M.Hadi Hajihosseini

This is a simple program that can decode Ceasar ciphers.

You enter the cipher and it shows the potential plain texts sorted by the possibility. Almost all the time the correct answer is the first one. (See examples below)

# Usage

Just clone the code and use it :)

It is in pure python 3.8+

## Different Approaches:
Only the first approach sorts the results based on the possibility of correctness (It is almost all the time precise)

**Recommended approach: First approach**
1. decipher_caesar_with_fi.py:
    - Finds the plain text based on the entered cipher.
2. decipher_simple_26letters.py
    - Cycles through the different combinations of English 26 letters to generate all results
3. decipher_caesar_brute_force.py
    - This one is not bounded in 26 letters of English language. It is on ascii letters.

## Example

For example this is a sample cipher: ``` gzch Gzihgnrrrdhmh ```

So we run the program to find the original text:

```zsh
$ python3 decipher_caesar_with_fi.py

You can enter a custom secret or use the default ones.
Sample secrets: (enter single digit number to select these)
         1. hdxmjnjaozsxcvibznzmqzm
         2. KfpjSjykqncfuutsUqfdXytwjhfzlmymnofhpnslBmfyxFuuxjxxntsx
Or enter you own secret.
Enter the secret to decipher: Sghr hr sgd bhogdq sdws gzch Gzihgnrrrdhmh
```

Then in the prompt in the last line, enter the cipher text above (```Sghr hr sgd bhogdq sdws gzch Gzihgnrrrdhmh```).

The result would be:

### **See the first line**

```
 ------------------------------ 
key:  1 | fi: 0.0694 | decipher: This is the cipher text hadi Hajihossseini
key: 12 | fi: 0.06281 | decipher: Estd td esp ntaspc epie slot Slutszdddptyt
key: 23 | fi: 0.06201 | decipher: Pdeo eo pda yeldan patp dwze Dwfedkoooaeje
key: 13 | fi: 0.05098 | decipher: Ftue ue ftq oubtqd fqjf tmpu Tmvutaeeequzu
key: 11 | fi: 0.04891 | decipher: Drsc sc dro mszrob dohd rkns Rktsrycccosxs
key:  0 | fi: 0.04338 | decipher: Sghr hr sgd bhogdq sdws gzch Gzihgnrrrdhmh
key: 16 | fi: 0.04185 | decipher: Iwxh xh iwt rxewtg itmi wpsx Wpyxwdhhhtxcx
key: 22 | fi: 0.04172 | decipher: Ocdn dn ocz xdkczm ozso cvyd Cvedcjnnnzdid
key:  2 | fi: 0.04171 | decipher: Uijt jt uif djqifs ufyu ibej Ibkjiptttfjoj
key:  5 | fi: 0.0408 | decipher: Xlmw mw xli gmtliv xibx lehm Lenmlswwwimrm
key:  8 | fi: 0.04044 | decipher: Aopz pz aol jpwoly alea ohkp Ohqpovzzzlpup
key:  7 | fi: 0.03952 | decipher: Znoy oy znk iovnkx zkdz ngjo Ngponuyyykoto
key: 24 | fi: 0.03918 | decipher: Qefp fp qeb zfmebo qbuq exaf Exgfelpppbfkf
key: 20 | fi: 0.03666 | decipher: Mabl bl max vbiaxk mxqm atwb Atcbahlllxbgb
key:  6 | fi: 0.03595 | decipher: Ymnx nx ymj hnumjw yjcy mfin Mfonmtxxxjnsn
key: 10 | fi: 0.03389 | decipher: Cqrb rb cqn lryqna cngc qjmr Qjsrqxbbbnrwr
key: 21 | fi: 0.03285 | decipher: Nbcm cm nby wcjbyl nyrn buxc Budcbimmmychc
key: 17 | fi: 0.03188 | decipher: Jxyi yi jxu syfxuh junj xqty Xqzyxeiiiuydy
key: 14 | fi: 0.03171 | decipher: Guvf vf gur pvcure grkg unqv Unwvubfffrvav
key: 15 | fi: 0.03101 | decipher: Hvwg wg hvs qwdvsf hslh vorw Voxwvcgggswbw
key: 19 | fi: 0.03059 | decipher: Lzak ak lzw uahzwj lwpl zsva Zsbazgkkkwafa
key:  4 | fi: 0.02861 | decipher: Wklv lv wkh flskhu whaw kdgl Kdmlkrvvvhlql
key:  9 | fi: 0.02854 | decipher: Bpqa qa bpm kqxpmz bmfb pilq Pirqpwaaamqvq
key: 25 | fi: 0.02778 | decipher: Rfgq gq rfc agnfcp rcvr fybg Fyhgfmqqqcglg
key: 18 | fi: 0.02533 | decipher: Kyzj zj kyv tzgyvi kvok yruz Yrazyfjjjvzez
key:  3 | fi: 0.02147 | decipher: Vjku ku vjg ekrjgt vgzv jcfk Jclkjquuugkpk

 ------------------------------ 

Results are sorted based on the Φ value. The correct text should be in the first results.
```

You can see that the code is showing the results sorted as the most possible answer is the first one.

**You see that the first result is Correct**

So it found the plain text correctly.

## Notes:
- This code accepts lowercase, uppercase and space characters.

- This is a simple Decoder based on Caesar algorithm so it only accepts English letters and space.
- Sometimes the result is not the first one but one of the first two or three if the text is very short due to small ammount of words
- Almost all the time the correct answer is the first one.

# Some more examles to test:

```
Input cipher: Xlmw mw E WIGVIX weqtpi
First result: This is A SECRET sample
```

```
Input cipher: LBH Pna hfr guvf pvcure gb grfg guvf PbQr
First result: YOU Can use this cipher to test this CoDe
```

## Author:

### **M.Hadi Hajihosseini**

* [Github](https://github.com/hadiMh)
* [Instagram](https://instagram.com/m.hadi.hajihosseini)

### License

Copyright © 2021, [M.Hadi Hajihosseini](https://github.com/hadiMh).
Released under the [MIT License](LICENSE).