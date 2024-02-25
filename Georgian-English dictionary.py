import csv

# Reads csv file and returns dictionary
def load_dictionary(file_path):
    dictionary = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:  # Ensures each row has exactly two elements
                dictionary[row[0].strip()] = row[1].strip()
    return dictionary

# Function checks if inputed letters are Georgian
def is_georgian(word):
    for char in word:
        # Georgian letters in Unicode range: U+10D0–U+10FF
        if not '\u10D0' <= char <= '\u10FF' and not char == '\u0020':
            return False
    return True

# function checks if inputed letters are English
def is_english(input_string):
    for char in input_string:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '\u0020'):
            return False
    return True

# Function translates words and considers different scenarios
def translate_word(word, dictionary, translation_direction):
    # Georgian to English translation
    if translation_direction == 'geo':
        translation = dictionary.get(word)
        # Checks if word is in dictionary and if not let's user add it
        if translation is None:
            print("Translation not found.")
            add_translation = input("\nWould you like to add it? (yes/no): ").strip().lower()
            while True:
                if add_translation == 'yes':
                    while True:
                        english_translation = input("Enter the English translation: ").strip()
                        dictionary[word] = english_translation
                        if not is_english(english_translation):
                            print("Input should contain only English letters.")
                            continue
                        print("Word added successfully.\n")
                        # Writes the updated dictionary to CSV file
                        with open(dictionary_file, 'a', newline='', encoding='utf-8') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([word, english_translation])
                        return english_translation
                elif add_translation == 'no':
                    return "Word not added.\n"
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    translation_direction == 'geo'
                    translate_word(word, dictionary, translation_direction)
                    break
        return translation
    # English to Georgian translation
    elif translation_direction == 'eng':
        # Checks if the input word exists as a value in the dictionary
        for key, value in dictionary.items():
            if value == word:
                return key
        print("Translation not found.")
        add_translation = input("\nWould you like to add it? (yes/no): ").strip().lower()
        while True:
            if add_translation == 'yes':
                while True:
                    georgian_translation = input("Enter the Georgian translation: ").strip()
                    if not is_georgian(georgian_translation):
                        print("Input should contain only Georgian letters.")
                        continue
                    dictionary[georgian_translation] = word
                    print("Word added successfully.\n")
                 # Write the updated dictionary back to the CSV file
                    with open(dictionary_file, 'a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([georgian_translation, word])
                    return word
            elif add_translation == 'no':
                return "Word not added.\n" 
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                translation_direction == 'eng'
                translate_word(word, dictionary, translation_direction)
                break


# User chooses the translation direction, 
# then program enters a loop where it repeatedly prompts the user for  input until they provide a valid word.
def main():
    global dictionary_file
    dictionary_file = 'dict.csv'
    dictionary = load_dictionary(dictionary_file)

    while True:
        translation_direction = input("\n'geo' to translate Georgian to English, \n'eng' to translate English to Georgian\n'exit' to quit\nEnter: ").strip().lower()
        if translation_direction == 'exit':
            print("Dictionary Closed |D] ")
            break
        elif translation_direction not in ['geo', 'eng']:
            print("Invalid input.")
            continue
        while True: 
            word = input("Enter the word: ").strip()

            if translation_direction == 'geo' and not is_georgian(word):
                print("Input should contain only Georgian letters.")
            elif translation_direction == 'eng' and not is_english(word):
                print("Input should contain only English letters.")
            else:
                translation = translate_word(word, dictionary, translation_direction)
                print(f"Translation: {translation}")
                break 
    

if __name__ == "__main__":
    main()


