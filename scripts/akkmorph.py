#!/usr/bin/env python3 

CONSONANTS = {'ʾ', 'b',
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

DENTALS = {'d', 't', 'ṭ'}

SIBILANTS = {'s', 'ṣ', 'š', 'z'}


def vowel_translator():
    voweltrans = {}
    for key in VOWELDICT.keys():
        voweltrans[key] = key
        for vowel in VOWELDICT[key]:
            voweltrans[vowel] = key
    return voweltrans


VOWELTRANS = vowel_translator()
VT = str.maketrans(VOWELTRANS)
'''
#Possible Replacement:
import unicodedata as ud
VOWELS = set('aeiou')
'''


def remove_vowel_diacritics(string):
    stripped = ''
    for c in string:
        decomp = ud.normalize('NFD', c)
        if decomp[0] in VOWELS:
            stripped += decomp[0]
        else:
            stripped += c
    return stripped 


class AkkWord:
    def __init__(self, word):
        self.word = word

    @property
    def signs(self):
        return self.word.split('-')
    
    @property
    def syllables(self):
        #sign_dict = {k:v.translate(VT) for k, v in enumerate(signs)}
        #syllable_list = [[sign_dict[0]]]
        '''
        for i in range(1,len(signs)):
            if sign_dict[i][0] in CONSONANTS:
                syllable_list.append([sign_dict[i]])
            elif sign_dict[i][0] == sign_dict[i-1][-1]:
                syllable_list[-1].append(sign_dict[i])
            else:
                syllable_list.append(['ʾ'+sign_dict[i]])
        '''
        signs = [x.translate(VT) for x in self.signs]
        syllable_list = [[signs[0].translate(VT)]]
        for i in range(1,len(signs)):
            sign = signs[i].translate(VT)
            if sign[0] in CONSONANTS:
                syllable_list.append([sign])
            elif sign[0] == signs[i-1][-1]:
                syllable_list[-1].append(sign)
            else:
                syllable_list.append(['ʾ'+sign])

        return syllable_list

    '''
    @property 
    def parsings(self):

    @property 
    def 
    def extract_root(self, syllables):
        for 
    '''

