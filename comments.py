def build_maps(filename: str) -> tuple[dict, dict]:
    """
    Reads a file containing character-Morse code pairs and builds two dictionaries:
    - `char_to_morse`: Maps characters to their corresponding Morse code.
    - `morse_to_char`: Maps Morse code to their corresponding characters.

    Args:
        filename (str): The name of the file containing the character-Morse code pairs.

    Returns:
        tuple[dict, dict]: A tuple containing the `char_to_morse` and `morse_to_char` dictionaries.
    """

    with open(filename, 'r', encoding='utf8') as file:
        char_to_morse = {}  # Dictionary to store character-to-Morse code mappings
        morse_to_char = {}  # Dictionary to store Morse code-to-character mappings

        for line in file:
            # Split the line into character and Morse code parts
            parts = line.strip().split('\t')

            # Check if the line is valid (has two parts and is not a header)
            if len(parts) == 2 and parts[0] != "Character":
                character, morse_raw = parts

                # Convert Morse code to standard format (dots and dashes)
                morse = morse_raw.replace('·', '.').replace('−', '-')

                # Add mappings to both dictionaries
                char_to_morse[character] = morse
                morse_to_char[morse] = character

                # Add uppercase mapping for lowercase characters
                if character.islower():
                    char_to_morse[character.upper()] = morse

    return char_to_morse, morse_to_char


def encode(text: str, char_to_morse: dict) -> str:
    """
    Encodes a given text into Morse code using the provided character-to-Morse code mapping.

    Args:
        text (str): The text to be encoded.
        char_to_morse (dict): The dictionary mapping characters to their Morse code.

    Returns:
        str: The encoded Morse code.
    """

    morse_code = []  # List to store the encoded Morse code

    for char in text:
        if char == ' ':
            # Add four spaces for a space character
            morse_code.append(' ' * 4)
        else:
            # Add the Morse code for the character and three spaces
            morse_code.append(char_to_morse[char] + ' ' * 3)

    return ''.join(morse_code).strip()  # Join the Morse code and remove trailing whitespace


def decode(morse: str, morse_to_char: dict) -> str:
    """
    Decodes a given Morse code into plain text using the provided Morse code-to-character mapping.

    Args:
        morse (str): The Morse code to be decoded.
        morse_to_char (dict): The dictionary mapping Morse code to their characters.

    Returns:
        str: The decoded plain text.
    """

    decoded_text = []  # List to store the decoded text

    # Split the Morse code into words (separated by three spaces)
    words = morse.split('   ')

    for word in words:
        # Split the word into letters (separated by one space)
        letters = word.split(' ')

        # Decode each letter and append to the decoded word
        decoded_word = ''.join(morse_to_char.get(letter, '') for letter in letters)
        decoded_text.append(decoded_word)

    return ' '.join(decoded_text)  # Join the decoded words into a sentence
