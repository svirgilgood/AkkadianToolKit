#!/usr/bin/env python3 

CONSENANTS = {'ʾ', 'b',
        'd', 'g', 'ḫ', 
        'y', 'k', 'ḳ', 'l', 
        'm', 'n', 'p', 
        'q', 'r', 's', 
        'ṣ', 'š', 't', 
        'ṭ', 'w', 'z'}
VOWELS = {'a', 'ā', 'á', 'à', 'â',
        'e', 'ē', 'é', 'è', 'â',
        'i', 'ī', 'í', 'ì', 'î',
        'o', 'ō', 'ô', 
        'u', 'ū', 'ú', 'ù', 'û'}


class AkkWord:
    def __init__(self, word):
        self.word = word
        self.signs = self.sign_split(word)
        self.syllables = self.__syllabifier(self.signs)


    def sign_split(self, word):
        return word.split('-')
    

    def __syllabifier(self, signs):
        sign_dict = {k:v for k, v in enumerate(signs)}
        syllable_list = [[signs[0]]]
        if signs[1][0] in VOWELS:
            #and if signs[0][1] == previous vowel
                syllable_list[0].append(signs[1])
        for i in range(1,len(signs)):
            if sign_dict[i][0] in CONSENANTS:
                syllable_list.append([sign_dict[i]])
            elif sign_dict[i][0] == sign_dict[i-1][-1]:
                syllable_list[-1].append(sign_dict[i])
            else:
                syllable_list.append([sign_dict[i]])

        return syllable_list




            
        






