import sys

number_of_alphabets = 26

min_allies_support = 3


kingdoms = {
    'SPACE':'GORILLA',
    'LAND':'PANDA',
    'WATER':'OCTOPUS',
    'ICE':'MAMMOTH',
    'AIR':'OWL',
    'FIRE':'DRAGON'
}

input_file = sys.argv[1]
file1 = open(input_file, 'r')
Lines = file1.readlines()
allies = []
for line in Lines:
    linestr = line.strip()
    #kingdom name and secret message
    split_text = linestr.split()
    first_text = split_text[0]
    second_text = ''.join(split_text[1::])
    cipher_key = len(kingdoms[first_text])

    secret_message = second_text; 

    decrypted_message = [] 
    for i in range(len(secret_message)):
        if secret_message[i] >= 'A' and secret_message[i] <= 'Z':
            secret_char = secret_message[i]  
            secret_char = ord(secret_char)
           
            new_char = chr(secret_char-cipher_key)

            if new_char < 'A':
                new_char = chr(ord(new_char)+number_of_alphabets)
            elif new_char > 'Z':
                new_char = chr(ord(new_char)-number_of_alphabets)     

            decrypted_message.append(new_char)

    emblem = kingdoms[first_text]

    emblem = list(emblem)

    is_won_kingdom = True

    match_char = []

    char_index = 0

    for i in range(len(emblem)):
        if not emblem[i] in decrypted_message:
            char_index = -1
        else:
            match_char.append(emblem[i])
            decrypted_message.remove(emblem[i])    

    if char_index != -1:        
        allies.append(first_text)


new_allies = []  

for item in allies:
    if item not in new_allies:
        new_allies.append(item)


if len(new_allies) < min_allies_support:
    print("NONE")
else:
    result = ["SPACE"]
    for i in new_allies:
        result.append(i)
    print(' '.join(result))


