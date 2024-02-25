# -*- coding = utf-8 -*-
# @Time : 1/20/2024 11:25 PM
# @Author : Lauren
# @File : dataannotation.py
# @Software : PyCharm
'''
The decode function works by reading an input file containing lines with
a number and a word. It creates a dictionary called words_dict to store
these words along with their corresponding positions. The function then
determines the height of the pyramid by finding the maximum position in
the dictionary. Next, it iterates through each level of the pyramid and
calculates the position of the word at the end of the current level
using the formula end_position = i * (i + 1) // 2. It then checks if this
position exists in the dictionary (words_dict) before accessing it.
If the position is found, the corresponding word is added to the
message_words list. Finally, the function concatenates the words from
message_words into a string, forming the decoded message.
'''
def decode(message_file):
    # Initialize a dictionary to store words and their corresponding positions
    words_dict = {}

    # Read the input file and store each word in the dictionary
    with open(message_file, 'r') as file:
        for line in file:
            position, word = line.split()
            words_dict[int(position)] = word

    # Find the maximum position to determine the pyramid height
    max_position = max(words_dict.keys())

    # Initialize an empty list to store the message words
    message_words = []

    # Iterate through each level of the pyramid
    for i in range(1, max_position + 1):
        # Calculate the position of the word at the end of the current level
        end_position = i * (i + 1) // 2
        # Check if the key exists in the dictionary before accessing it
        if end_position in words_dict:
            # Add the corresponding word to the message words list
            message_words.append(words_dict[end_position])

    # Concatenate the message words into a string
    decoded_message = ' '.join(message_words)

    return decoded_message

# Example usage
def main():
    message_file_path = 'coding_qual_input.txt'
    result = decode(message_file_path)
    print(result)

if __name__ == "__main__":
    main()
