from bs4 import BeautifulSoup

file = open("./Google.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")

# print(bs.title)

# 1. Tag: the first one eg: bs.title
# 2. NavigatableString:  eg: bs.title.string
# 3. BeautifulSoup: entire file eg: bs
# 4. Comment: without comment  eg: bs.a.string

# iteration
# print(bs.head.contents[1])

# search: in tag and its content
# (1) find_all()
# string filter: exact same content
# t_list = bs.find_all("a")

# search(): regular expression search
# import re
# t_list = bs.find_all(re.compile("a")) # include "a"


#  method: very flexible
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exist)
#
# for item in t_list:
#     print(item)
# print(t_list)

# (2) kwargs: parameter
# t_list = bs.find_all(id="hplogo")
# t_list = bs.find_all(class_=True)

# (3) text arguement
# t_list = bs.find_all(text=["Google",""])

# (4) limit
# t_list = bs.find_all(text="Google",limit=3)

# (5) CSS selector
# t_list = bs.select("title")   # by tag
# t_list = bs.select(".mnav")   # by class name
# t_list = bs.select("#u1")     # by id
# t_list = bs.select("a[class='bri']") # by attribute
# t_list = bs.select("head > title") # by children tag
t_list = bs.select(".mnav ~ .bri") # by brother tag

print(t_list[0].get_text())
for item in t_list:
    print(item)