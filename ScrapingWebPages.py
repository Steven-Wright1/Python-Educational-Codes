from bs4 import BeautifulSoup

# create an example html

html=['<html><heading style="font-size:20px"><i>This is the title<br><br></i></heading>',
     '<body><b>This is the body</b><p id="para1">This is para1<a href="www.google.com">Google</a></p>',
     '<p id="para2">This is para 2</p></body></html>']
#This combines all strings from the strings above into one
html=''.join(html)

#instantiate a soup object to take in the html
soup = BeautifulSoup(html)
#Allows us to print html in a comprehsive structure
print(soup.prettify())

#We can access different aspects of the html
print("The name of the html is ", soup.html.name)   #Name attribute is just the name of the tag
print("The text in the html is ", soup.body.text)
print("The contents of the html is ", soup.html.contents)

#Prints bold text
bold = soup.findAll('b')
print(bold)
#To return only the text, take each element of this list and get the text attribute
print(bold[0].text)

#If you want to get all the text in paragraphs (ie - enclosed in p tags)
paras = ' '. join([p.text for p in soup.findAll('p')])
print(paras)


# findAll can look for attributes as well. paragraph with id 'para2' can be found
soup.findAll(id="para2")[0].text

#Find any text with font size 20
font20=' '.join([p.text for p in soup.findAll(style="font-size:20px")])
print(font20)

#This is how you find links in the html
#find only picks the first hit. FindAll is used to find all hits
links = soup.find('a')  #a tags often refer to websites 
# Links are generally of the form <a href='link'>'link-text'</a>
print(links)


# To extract the url and the text separately 
print(links['href']," is the url and ",links.text," is the text")




# Let's say you want the text of the first paragraph after the first occurrence of the text "Google" 
print(soup.find(text="Google").findNext('p').text)


print(soup.body('p'))












