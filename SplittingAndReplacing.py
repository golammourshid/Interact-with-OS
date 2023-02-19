import re

# here will split the sentence with . ? and !
# result = re.split(r"[.?!]", "this is one. Another one? No ! this is other")
# print(result)

# find an email and replace it with another string
# result = re.sub(r"[\w]+@[\w]+", "Email", "this is one. this@that Another one? No ! this is other")
# print(result)

# # find an email and replace the position of the group with another regex
# result = re.sub(r"^([\w]*), ([\w]*)$", r"\2 \1", "Loveless, Adam")
# print(result)

result = re.sub(r"(\d{3})-(\d{3})-(\d{4}[^\d.])",  r"(\1) \2-\3", "123-123-12345")
print(result)

