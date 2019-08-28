#phoneAndEmail.py - Finding emails and phones in clipboard

import pyperclip
import re

#TODO - Regex for phones

phoneRegex = re.compile('''
                        (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})''',re.VERBOSE)

#TODO - Regex for emails

emailRegex = re.compile('''(
                        [a-zA-Z0-9._%+-]+ #username
                        @                 #arroba
                        [a-zA-Z0-9.-]+    #domain name
                        (\.[a-zA-Z]{2,4}) #ponto seguido de outros caracteres
                        )''',re.VERBOSE)

#TODO - Find correspondence in the text

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TODO - Copy the results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')
