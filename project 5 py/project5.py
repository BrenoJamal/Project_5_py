#!/usr/bin/env python3
"""
Morse code

@author: Breno Jamal
@date: 07/12/2024
"""


def build_maps(filename: str) -> tuple[dict, dict]:
    with open(filename, 'r', encoding='utf8') as file:
        char_to_morse = {}
        morse_to_char = {}
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2 and parts[0] != "Character":
                character, morse_raw = parts
                morse = morse_raw.replace('·', '.').replace('−', '-')
                char_to_morse[character] = morse
                morse_to_char[morse] = character
                if character.islower():
                    char_to_morse[character.upper()] = morse
    return char_to_morse, morse_to_char


def encode(text: str, char_to_morse: dict) -> str:
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append(' ' * 4)
        else:
            morse_code.append(char_to_morse[char] + ' ' * 3)
    return ''.join(morse_code).strip()


def decode(morse: str, morse_to_char: dict) -> str:
    decoded_text = []
    words = morse.split('       ')
    for word in words:
        letters = word.split('   ')
        decoded_word = ''.join(morse_to_char.get(letter, '') for letter in letters)
        decoded_text.append(decoded_word)
    return ' '.join(decoded_text)


def main():
    """Main function"""
    try:
        d1, d2 = build_maps("morse.txt")
        assert (
            len(d1) == 80
        ), f"There are 80 characters in the file, but {len(d1)} mappings in your dictionary"
        assert (
            len(d2) == 54
        ), f"There are 54 codes in the file, but {len(d2)} mappings in your dictionary"
    except AssertionError as a_err:
        print(a_err)

    for phrase, expected in [
        ("SOS", "...   ---   ..."),
        ("CS-150-A", "-.-.   ...   -....-   .----   .....   -----   -....-   .-"),
        (
            "'Hello, World'",
            ".----.   ....   .   .-..   .-..   ---   --..--       .--   ---   .-.   .-..   -..   .----.",
        ),
        ("Thank you.", "-   ....   .-   -.   -.-       -.--   ---   ..-   .-.-.-"),
    ]:
        try:
            result = encode(phrase, d1)
            assert result == expected, (
                f"{phrase} is not encoded correctly."
                + "\n"
                + f"Expected: {expected}"
                + "\n"
                + f"Returned: {result}"
            )
            print(f"'{phrase}' encoded using Morse code is '{result}'")
        except AssertionError as a_err:
            print(a_err)
    for code, expected in [
        ("...   ---   ...", "sos"),
        ("-.-.   ...   -....-   .----   .....   -----   -....-   .-", "cs-150-a"),
        (
            ".----.   ....   .   .-..   .-..   ---   --..--       .--   ---   .-.   .-..   -..   .----.",
            "'hello, world'",
        ),
        ("-   ....   .-   -.   -.-       -.--   ---   ..-   .-.-.-", "thank you."),
    ]:
        try:
            result = decode(code, d2)
            assert result == expected, (
                f"{code} is not decoded correctly."
                + "\n"
                + f"Expected: {expected}"
                + "\n"
                + f"Returned: {result}"
            )
            print(f"Morse code '{code}' encodes '{result}'")
        except AssertionError as a_err:
            print(a_err)


if __name__ == "__main__":
    main()
