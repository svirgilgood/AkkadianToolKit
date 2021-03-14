#!/usr/bin/env python3

import dbm
import json
import csv
import os
from typing import Dict, Union, List

DB_DICT = Dict[bytes, bytes]
SIGN_VALUES = Union[str, List[str]]


def db_searcher(value: str) -> Dict[str, SIGN_VALUES]:
    with dbm.open("../data/sign.db", "r") as db:  # type: ignore
        byte_value: bytes = str.encode(value)
        values: bytes = db[byte_value]
        value_dict = json.loads(values.decode("utf8"))
    return value_dict


def main():
    a_parser = argparse.ArgumentParser()
    a_parser.add_argument(
        "-c", "--chapter", help="chapter number to add cards to"
    )
    a_parser.add_argument(
        "sign_value", help="sign value to search in the database"
    )

    '''
    a_parser.add_argument(
        "-c",
        "--convert",
        action="store_true",
        help="convert a string of cuneiform to translate to cuneiform",
    )
    '''

    args = a_parser.parse_args()
    filename = args.chapter + ".csv"

    row_dict = db_searcher(args.sign_value)
    row_dict["old_babylonian"] = row_dict["unicode"]

    headers = [
        "unicode",
        "old_babylonian",
        "sign_num",
        "phonetic",
        "logograms",
        "chapter",
    ]
    phonetic_string = ", ".join(
        [x.replace("\n", "").replace("\t", "") for x in row_dict["phonetic"]]
    )
    logograms_string = ", ".join(row_dict["logograms"])

    row_dict["phonetic"] = phonetic_string
    row_dict["logograms"] = logograms_string
    row_dict["chapter"] = args.chapter

    with open(filename, "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter="\t")
        writer.writerow(row_dict)


if __name__ == "__main__":
    import argparse

    main()
