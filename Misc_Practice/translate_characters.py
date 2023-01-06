### Python Practice


def translate_characters(chr_var):  ## Started with chr_var variable, ended up being the necessary placeholder for the following ord() function 
    return chr(ord(chr_var) + 2) ## ord() gives us a unicode number we need and + 2 according to the key given. Return chr() converts back into the character we need to translate


def translate(phrase):   ## We have to define our translation method here
    translation = []   ## Makes a list for translation, this is necessary
    punctuation = ".()' "   ## Defines punctuations that render some pat of our input phrase unreadable
    for c in phrase:  ## "for C in" the C can mean anything. but the "in ___ " must be consistent throughout if necessary. 
        if c in punctuation:
            translation.append(c)   ## translation.append(c) appends the given C into the translation list defined in line 9 
        elif c == 'y':
            translation.append('a')
        elif c == 'z':
            translation.append('b')
        else: 
            translated_character = translate_characters(c)   ## Puts our translate_characters method into our scope now. Arshiya reminded me that I have to work "backwards" so that we define a variable FIRST and then include the function after. 
            translation.append(translated_character)   ## appends the translated_Character into our translation list.
    final_translation = "".join(translation)   ## "".join() beatuifies our list, once again we have to work backwards and write down a variable which allows our method to work properly 
    print(final_translation)   ## Final print

phrase = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(translate(phrase)) 



# from string import ascii_lowercase as al

# # Build Caesar table using a shift of 2
# table = str.maketrans(al, al[2:] + al[:2])
# hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# print(hint.translate(table))

# cypher_flag = 'map'
# answer = cypher_flag.translate(table)
# print(answer)


