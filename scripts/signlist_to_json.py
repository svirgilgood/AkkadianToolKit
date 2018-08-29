#!/usr/bin/env python3 

import bs4 
import re
import glob

HEADING_RE = re.compile(r'(\<a name="[^\.]*"\>\d+\w*\s*\</a\>)')


def divide_values(value_text):



def parse_html(htmltext):
    ele_dict = []
    ele_split = HEADING_RE.split(htmltext)
    for i in range(len(ele_split)):
        if i % 2 ! = 0:
            ele_dict.append({'sign': ele_split[i], 'values': ele_split[i+1]})
    return ele_dict


def main():
    # I should make this scrape the website as well
    htmlfilelist = glob.glob('../data/signlists/list*.html') 



if __name__ == '__main__':
    main()
