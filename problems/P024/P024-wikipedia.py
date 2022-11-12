a = str(input("Enter the link address: "))

import urllib 
from bs4 import BeautifulSoup
b = urllib.urlopen(a) 
soup = BeautifulSoup(b.content , "html.parser") 
print(soup.prettify)