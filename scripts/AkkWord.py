#!/usr/bin/env python3 

CONSENANTS = {'ʾ', 'b',
        'd', 'g', 'ḫ', 
        'y', 'k', 'ḳ', 'l', 
        'm', 'n', 'p', 
        'q', 'r', 's', 
        'ṣ', 'š', 't', 
        'ṭ', 'w', 'z'}

MORPHEMIC_CONS = {'t', 'ṭ', 'd', 
        'š', 'n'}

VOWELS = {'a', 'ā', 'á', 'à', 'â',
        'e', 'ē', 'é', 'è', 'â',
        'i', 'ī', 'í', 'ì', 'î',
        'o', 'ō', 'ô', 
        'u', 'ū', 'ú', 'ù', 'û'}

VOWELDICT = {'a': ['ā', 'á', 'à', 'â'],
        'e': ['ē', 'é', 'è', 'â'],
        'i': ['ī', 'í', 'ì', 'î'],
        'o': ['ō', 'ô'],
        'u': ['ū', 'ú', 'ù', 'û']}

VOWELTRANS = vowel_translator()
VT = str.maketrans(VOWELTRANS)


def vowel_translator():
    voweltrans = {}
    for key in VOWELDICT.keys():
        voweltrans[key] = key
        for vowel in VOWELDICT[key]:
            voweltrans[vowel] = key
    return voweltrans


class AkkWord:
    def __init__(self, word):
        self.word = word
        self.signs = self.sign_split(word)
        self.syllables = self.__syllabifier(self.signs)


    def sign_split(self, word):
        return word.split('-')
    

    def __syllabifier(self, signs):
        sign_dict = {k:v.translate(VT) for k, v in enumerate(signs)}
        syllable_list = [[sign_dict[0]]]
        for i in range(1,len(signs)):
            if sign_dict[i][0] in CONSENANTS:
                syllable_list.append([sign_dict[i]])
            elif sign_dict[i][0] == sign_dict[i-1][-1]:
                syllable_list[-1].append(sign_dict[i])
            else:
                syllable_list.append(['ʾ'+sign_dict[i]])

        return syllable_list


    '''
    def extract_root(self, syllables):
        for 
    '''



