# -*- coding: utf-8 -*-

import sys
script, input_encoding, error = sys.argv

#3 parameters: file, encoding and errors
def main(language_file, encoding, errors):
    #reading language file line by line
    line = language_file.readline()

    #if line is true (exists), print the the line
    if line:
        #calls on print_line function on three parameters
        print_line(line, encoding, errors)
        #returning the main function makes it a loop
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    #strip is a function that selects the first string (after removal)
    next_lang = line.strip()
    #encode is a method that can change encoding, takes two params
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decode works the opposite of encode
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #encode to decode
    print(raw_bytes, "<===>", cooked_string)

#opens the file and specifies encoding
languages = open("languages.txt", encoding="utf-8")

#runs the function
main(languages, input_encoding, error)
