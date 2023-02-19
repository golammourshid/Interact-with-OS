#!/usr/bin/env python3
import re


def rearrange_name(name):
    # create groups using () parenthesis. finding pattern that have last name, comma, space, then first name
    result = re.search(r"^(\w*), (\w*)$", name)
    if result == None:
        return ""
    return "{} {}".format(result[2], result[1])
