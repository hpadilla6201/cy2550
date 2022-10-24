#!/usr/bin/env python3
import argparse
from genericpath import isfile
import random
from secrets import choice

words = open("./project4/words.txt", "r").read().split("\n")
symbols = ["!", "?", "#", "$", ">", "<", "^", "@"]

parser = argparse.ArgumentParser(
    description='Process some args for password generator.')
# parser.add_argument('-h',
#                     '--help',
#                     metavar='help',
#                     type=int,
#                     help='helper')
parser.add_argument('-w',
                    '--words',
                    metavar='include_words',
                    type=int,
                    default=4,
                    help='include WORDS words in the password')
parser.add_argument('-c',
                    '--caps',
                    metavar='capitalize',
                    type=int,
                    default=0,
                    help='capitalize the first letter of CAPS random words')
parser.add_argument('-n',
                    '--numbers',
                    metavar='insert numbers',
                    type=int,
                    default=0,
                    help='insert NUMBERS random numbers in the password')
parser.add_argument('-s',
                    '--symbols',
                    metavar='capitalize',
                    type=int,
                    default=0,
                    help='insert SYMBOLS random symbols in the password')
# def get_args():

# return parser.parse_args()


def pass_gen(num_words, num_numbers, num_symbols, num_caps):
    password = ""
    words_caps = []
    password_list = []
    len_of = len(password_list)

    for _ in range(num_words):
        password_list.append(choice(words))

    for _ in range(num_numbers):
        password_list[random.randint(0, len(password_list)) - 1] += str(
            random.randint(0, 9))

    for _ in range(num_symbols):
        password_list[random.randint(0, len(password_list)) -
                      1] += random.choice(symbols)

    for _ in range(num_caps):
        tracker = random.randint(0, len(password_list) - 1)
        password_list[tracker] = password_list[tracker].capitalize()

    return password.join(password_list)


def main():
    args = parser.parse_args()
    if args.words < args.caps:
        raise Exception("capitile letters cannot be greater than word count")

    my_wordlist = pass_gen(num_words=args.words,
                           num_numbers=args.numbers,
                           num_symbols=args.symbols,
                           num_caps=args.caps)

    print(my_wordlist)


if __name__ == "__main__":
    main()
