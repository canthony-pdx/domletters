#!/usr/bin/python3

import sys

def letter_count(word):
    dom_count = 0
    for letter in word:
        count = word.count(letter)
        if count > dom_count:
            dom_count = count
    return dom_count

def main():
    dom_count = 0
    for line in sys.stdin:
        wordlist = line.split()

        for word in wordlist:
            if word.isalpha() == False:
                continue
            dom_count += letter_count(word.lower())

    print('Dominant letter count: ', dom_count)

if __name__ == '__main__':
    main()
