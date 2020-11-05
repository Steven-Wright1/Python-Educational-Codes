from bs4 import BeautifulSoup
import re

input = ('<html>'
'<head><title>Page title</title></head>'
'<p id = "firstpara" align = "center">This is a paragraph<b>one<\b>.'
'<p id = "secondpara" align = "blah">This is a paragraph<b>two<\b>.'
'<\html>')

soup = BeautifulSoup(input,"lxml")

titleTag = soup.html.head.title
# This prints the title, but still bound within the html code
print(titleTag)
# Printing this as a string omits the html code
print(titleTag.string)

# To print out the number of paragraphs
print(len(soup('p')))

# Retrives all the text and html involved in the first para
print(soup('p',{'align':'center'}))
# Reduces this by accessing the ID tag
print(soup('p',{'align':'center'})[0]['id'])

# Acesses the next para
print(soup('p')[1].b.string)

# Assigns an ID to the title tag
titleTag['id'] = 'theTitle'
# Changes the title
titleTag.string = 'NewTitle'
print(soup.html.head.title)
print(soup.html.head.title.contents)


