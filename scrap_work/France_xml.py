from bs4 import BeautifulSoup
import lxml


file = open('MB.xml', 'r')
contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
rosette = soup.find_all('pente')
rosette_string = str(rosette)


north = 'n="true"'
northeast = 'ne="true"'
northwest = 'nw="true"'
east = 'e="true"' 
south = 's="true"'
southeast = 'se="true"'
southwest = 'sw="true"'
west = 'w="true"'


if west in rosette_string:
    print("found")
else:
    print("not found")




