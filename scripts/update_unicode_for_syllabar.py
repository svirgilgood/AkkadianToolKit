#!/usr/bin/env python3

import sys
import json
import pandas as pd  # type: ignore
from typing import Union, List, Tuple


def cuneiform_seperator(cell: str) -> Tuple[str, str]:
    cunei: List[str] = []
    others: List[str] = []
    for char in cell:
        if ord(char) > 73727 and ord(char) < 75076:
            cunei.append(char)
        else:
            others.append(char)
    return "".join(cunei), "".join(others)


def main():
    xlsx: str = sys.argv[1]
    jsonfile: str = sys.argv[2]
    df = pd.read_excel(xlsx)
    with open(jsonfile) as jfp:
        syllabar = json.load(jfp)


if __name__ == "__main__":
    main()
