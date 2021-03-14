#!/usr/bin/env python3

import json
import dbm


def db_adder(key_list, value_as_bytes, db):
    for key in key_list:
        key_byte = str.encode(key.replace("~", ""))
        db[key_byte] = value_as_bytes


def main():
    with open("../data/new_syllabar.json") as fp:
        syllabar = json.load(fp)
    with dbm.open("../data/sign.db", "c") as db:
        for key, value in syllabar.items():
            try:
                value_dict = {
                    "unicode": value["unicode"],
                    "sign_num": key,
                    "phonetic": [],
                    "logograms": [],
                }
            except KeyError:
                continue

            for reading in ("phonetic", "logograms"):
                try:
                    for read in value["values"][reading]:
                        value_dict[reading].append(read)
                except KeyError:
                    pass

            values_bytes = str.encode(
                json.dumps(value_dict, ensure_ascii=False)
            )

            for reading in ("phonetic", "logograms"):
                db_adder(value_dict[reading], values_bytes, db)


if __name__ == "__main__":
    main()
