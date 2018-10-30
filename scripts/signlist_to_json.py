#!/usr/bin/env python3 
'''

'''

from lxml import etree as et
import re
from bs4 import BeautifulSoup
import glob
import json 

HEADING_RE = re.compile(r'(\<a name="[^"\.]*"\>\d+\w*\s*\</a\>)')
LOWER_SHIN = re.compile(r'<img[^>\.]* src="..\/cf\/sj.gif">')
CAP_SHIN = re.compile(r'<img[^>\.]* src="..\/cf/Sj.gif">')
SUB_RPL = re.compile(r'<\/?sub>')
SUPER_RPL = re.compile(r'<\/?sup>')

EMPHATICS = {'T': 'ṭ',
        'S': 'ṣ',
        'h': 'ḫ', 
        'H': 'Ḫ'} 


def divide_sign_name(name_num):
    sign_parse = et.fromstring(name_num)
    name = sign_parse.attrib['name'] 
    num = sign_parse.text.strip()
    if num.isnumeric():
        num = num.zfill(3)
    else:
        num = num.zfill(4)
    return name, num
    

def clean_li(liele):
    li_text = liele.text 
    try:
        heading, li_list = li_text.strip().split(':')
    except ValueError:
        heading = 'Additional'
        li_list = li_text.strip()
    li_list = [x.strip() for x in li_list.split(',')]
    return {heading: li_list}


def divide_values(value_text):
    soup = BeautifulSoup(value_text, 'html5lib')
    table = soup.find_all('table')
    try:
        table = table.pop()
        table.extract()
    except (AttributeError, IndexError, TypeError) as e:
        pass
    li_list = soup.find_all('li')
    values_dict = {}
    for li in li_list:
        values_dict.update(clean_li(li))
    return values_dict 
    

def parse_html(htmltext, ele_dict):
    htmltext = LOWER_SHIN.sub('š', htmltext)
    htmltext = CAP_SHIN.sub('Š', htmltext)
    htmltext = SUB_RPL.sub('~', htmltext) 
    htmltext = SUPER_RPL.sub('^', htmltext)
    ele_split = HEADING_RE.split(htmltext)
    for i in range(len(ele_split)):
        if i % 2 != 0:
            sign_name, sign_number = divide_sign_name(ele_split[i])
            value_dict = divide_values(ele_split[i+1])
            sign_dict = {'sign': 
                    {'name': sign_name, 
                    'sign_number': sign_number}, 
                    'values': value_dict}
            ele_dict[sign_number] = sign_dict
    return ele_dict


def main():
    # I should make this scrape the website as well
    htmlfilelist = glob.glob('../data/signlists/list*.html') 
    ele_dict = {}
    for h in htmlfilelist:
        with open(h) as htm:
            html = htm.read()
        ele_dict = parse_html(html, ele_dict)
        #ele_dict.extend(ele_list)
    with open('data.json', 'w') as outfile:
        json.dump(ele_dict, outfile, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    main()
