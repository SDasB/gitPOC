from bs4 import BeautifulSoup

# reading content
file = open("data.xml", "r")
contents = file.read()

# parsing
soup = BeautifulSoup(contents, 'xml')
names = soup.find_all('name')

# display content
for data in names:
    print(data.get_text())