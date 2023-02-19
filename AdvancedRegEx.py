import re

# create groups using () parenthesis. finding pattern that have last name, comma, space, then first name
# result = re.search(r"^(\w*), (\w*)$", "plaza, _sdf_n")
# print(result)
# here result.groups() will return the tuples, and then we can access them
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# print(result[3])


# find the first occurence of 5 consecutive letters
# result = re.search(r"[A-Za-z]{5}", "A ghoster")
# print(result)

# find the all occurence of 5 consecutive letters
# result = re.findall(r"[A-Za-z]{5}", "A ghoster god seldomBites")
# print(result)

# find the all word that have exactly 5  letters
# here \b boundary the word
# result = re.findall(r"\b[A-Za-z]{5}\b", "A ghost ,doges seldo Bites")
# print(result)

# find all the alphanumeric word of length 5 to 10
# result = re.findall(r"\w{5,10}", "A ghost doges seldomBites")
# print(result)

# find all the alphanumeric word of length 5 to infinity
# result = re.findall(r"\w{5,}", "A ghost doges seldomBites")
# print(result)

# find all the alphanumeric word of length 0 to 20
# result = re.findall(r"\w{,20}", "A ghost doges seldomBites")
# print(result)

# find the string that is starting with  square bracket and ends with square bracket and only have more than one digit
# alltime the group result will be start from index 1
# result = re.search(r"\[(\d+)\]", "A ghost doges seldomBites[123456f]")
# print(result[1])



