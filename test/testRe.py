# regular expression

import re
# create pattern object

pat = re.compile("AA")  # this AA is a RE to check other strings
# m = pat.search("CBA")  # this string is the one being checked

# m = pat.search("ABCAA")
# m = pat.search("ACAADDCCAAA")   # search() to compare and find

# without pattern object
# m = re.search("asd","Aasd") # first is pattern, last is string
# print(m)

# print(re.findall("a","ASDaDFGAa"))  # like search() first is pattern, last is the string

# print(re.findall("[A-Z]","ASDaDFGAa"))

# print(re.findall("[A-Z]+","ASDaDFGAa"))

# re.sub()
# print(re.sub("a","A","abcdefg")) # find "a", replace by "A"

# use r to ignore escape characters
a = r"\abcd-\'"
print(a)