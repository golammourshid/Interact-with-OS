#!/usr/bin/env python3

def validate_user(name, min_len):
    assert type(name) == str, "Username must be a string"
    if min_len < 1:
        raise ValueError("min len must be grater than 1")
    if len(name) < min_len:
        return False
    if not name.isalnum():
        return False
    return True

import sys

for line in sys.stdin:
    print(line.strip().capitalize())

