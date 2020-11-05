from bs4 import BeautifulSoup
import re

html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''

soup = BeautifulSoup(html_doc, "html.parser")
# Collect everything enclosed in <head><\head>
print(soup.head)
# Collect everything enclosed in <title><\title>
print(soup.title)
# Gives the first occurrence of the bold tag in the body tags
print(soup.body.b)
# Gives the FIRST instance of what's enclosed in a tags
print(soup.a)
# Prints out EVERYTHING found between a tags. 
print(soup.find_all('a'))
#################################################################################
print("#"*70)

head_tag = soup.head
print("--head_tag",head_tag, '\n')
print("--head_tagcontents", head_tag.contents, '\n')

title_tag = head_tag.contents[0]
print("--title_tag", title_tag.contents, '\n')

print("--len(soup.contents)",len(soup.contents), '\n')

print("--Looping through the decendants in head tag")
for child in head_tag.descendants:
    print(child, '\n')

title_tag = soup.title
print("--Print title_tag and the parents of title tag")
print(title_tag.parent, '\n')

html_tag = soup.html
print("--html_tag.parents")
print(html_tag.parent, '\n')

print("--type(html_tag.parents)")
print(type(html_tag.parent), '\n')

print("--soup.parent")
print(soup.parent)

link = soup.a
print("--link")
print(link, '\n')

# Walks us up through parent tags, so will from the a tag, and move outwards towards
# The beginning of the document
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)















