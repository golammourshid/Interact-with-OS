import re

# exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits
# result = re.search(r"[ ]+\d{5}[^\d]", 'Their address is: 123 Main Street, Anytown, AZ 785258-0001.')
# print(result)

# \S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
# result = re.search(r"\S*", "plaz(a) sdf")
# print(result)

# \S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
# result = re.search(r"am|pm|AM|PM", "am")
# print(result)

# here r means raw string. means that all special character are also included with this string
# result = re.search(r"\(.*\)", "plaz(a)")
# print(result)

# it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period,
# question mark, or exclamation point
# result = re.search(r"^[A-Z][a-z ]+[.?!]$", "Is this is a sentence?")
# print(result)
# valid variable name in python
# result = re.search(r"^[A-Za-z_]\w*$", "_HI________________90 dsaf")
# print(result)


# here \ use to search any other special character optional using question mark
# result = re.search(r"int\.com", "motionint.com")
# print(result)

# here \w means there can be any alphanumeric character like number, letter or underscore
# result = re.search(r"\w", "motionint.com")
# result = re.search(r"\w*", "motionint1_.com")
# print(result)

# here \d means there can be only number
# result = re.search(r"\d", "motionint.12com")
# print(result)
# result = re.search(r"\d*", "motionint1_.com")
# print(result)

# here \s means there can be only space, tab, newline
# result = re.search(r"\s", "motionin 12com    wsa")
# print(result)
# result = re.search(r"\s*", "  \n   motionint1_.com")
# print(result)

# text = 'shopping_list: milk bread, eggs.'
# result = re.search(r"\b\w\s+\w", text)
#
# print(result)

# here \b means word boundary
# result = re.search(r"\b", "motion int.12com")
# print(result)
# result = re.search(r"\b", "motion int our name")
# print(result)


# | means or symbol
# result = re.search(r"aza|aze", "plaza")
# print(result)

# | means or symbol
# result = re.findall(r"aza|aze", "plaza and plaz")
# print(result)

# will return none
# result = re.search(r"aza", "pa")
# print(result)
#
# result = re.search(r"a.", "plazam")
# print(result)
#
# result = re.search(r"a..m", "plaza")
# print(result)

# ^ indicates the starting of the string
# result = re.search(r"^pla", "plaza is my mom")
# print(result)
#
# result = re.search(r"goo$", "plaza is vey good")
# print(result)
#
# result = re.search(r"good$", "plaza is vey Good", re.IGNORECASE)
# print(result)

# here use one of the letter that will match with the main string
# result = re.search(r"[asddaPp]la", "plAzam is most wanted Pla")
# print(result)

# here will use any letter from a to z
# result = re.search(r"[a-z]la", "plAzam is most wanted Pla")
# print(result)

# here will use any letter from a to z or A to Z or 0 to 9
result = bool(re.search(r"[A-Za-z0-9]la", "plazam is most wanted 6lea"))
print(result)

# here will show the first occurrence of the non letter symbol
# result = re.search(r"[^A-Za-z]", "plAzam is most wanted 6la")
# print(result)

# here will show the first occurrence of the non letter symbol and that is not a space
# result = re.search(r"[^A-Za-z ]", "plAzam is most wanted 6la")
# print(result)







# .* takes as much . character as it can
# means 0 to infinity times of . will occure
# result = re.search(r"py.*n", "ghjpykl;kl;kl;n programming")
# print(result)

# means 0 to infinity times of a to z letter will occure
# result = re.search(r"py[a-z]*n", "ghjpyklklkln programming")
# print(result)

# means consecutively occurence of o and l at the very first
# result = re.search(r"o+l+", "goldfish")
# print(result)

# means consecutively occurence of o and l at the very first
# result = re.search(r"o+l+", "lolwooolyoooollllll")
# print(result)

# will return none as no consecutively occuranse here
# result = re.search(r"o+l+", "boil")
# print(result)

# here p is optional using question mark
# result = re.search(r"p?each", "To each their own")
# print(result)




