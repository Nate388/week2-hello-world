# Nathan Ezra Spencer

import sys # including sys to exit the program later

print ('Hello!') # greets the user in English
print ('Please select a language:')
print ('English, German, or Russian') # my 3 favorite languages

language = input() #using input() to allow the user to choose a language
if language == 'English': # if the variable language is set to any of the strings, it prints the correct response
    print ('Hello!')
if language == 'German':
    print ('Hallo!')
if language == 'Russian':
    print('Здравствуйтe!')
    
print ('goodbye!')# saying goodbye
print ('type "exit" to leave program')# allowing the user to exit the program using sys.exit()
ext = input()
if ext == 'exit':
    sys.exit()

    # please provide feedback

    







