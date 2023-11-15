import os
import json
import random
import argparse

UNICODE_JSON_FILE = os.path.join(os.path.dirname(__file__), 'utf8.json')
HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'history.json')

def random_number(max):
    return random.randint(0, max - 1)


def get_random_utf8(char):
    with open(UNICODE_JSON_FILE, 'r') as f:
        char_dict = json.load(f)
        equivalent_chars = char_dict.get(char)
        random_num = random_number(len(equivalent_chars))
        return equivalent_chars[random_num]


def get_all_utf8(char):
    with open(UNICODE_JSON_FILE, 'r') as f:
        char_dict = json.load(f)
        equivalent_chars = char_dict.get(char)
        return equivalent_chars

def make_utf_sentence(sentence):
    utf_sentence = ""
    utf_sentence_url = ""
    for char in sentence:
        utf_sentence += get_random_utf8(char)[0]
        utf_sentence_url += get_random_utf8(char)[1]
    return [utf_sentence, utf_sentence_url]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts a sentence to UTF-8')
    parser.add_argument('sentence', type=str, help='The sentence to convert')
    parser.add_argument('--all', action='store_true', help='Get all UTF-8 characters for the given character')
    parser.add_argument('-u', '--url', action="store_true")
    parser.add_argument('-i', '--inline', action="store_true")
    args = parser.parse_args()

    if args.all and len(args.sentence) > 1:
        print("Only one character is allowed when using --all")
        exit()

    if args.all:
        all_chars = get_all_utf8(args.sentence)
        for char in all_chars:
            if args.url:
                if args.inline:
                    print(f"{char[0]}: {char[1]}")
                else:
                    print(char[0])
                    print(char[1])
            else:
                if args.inline:
                    print(char[0], end='')
                else:
                    print(char[0])
    else:
        sentences = make_utf_sentence(args.sentence)
        print(sentences[0])
        if args.url:
            print(sentences[1])
