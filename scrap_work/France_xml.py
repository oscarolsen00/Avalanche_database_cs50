from bs4 import BeautifulSoup
import lxml



file = open('MB2.xml', 'r')
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

for link in soup.find_all('bulletins_neige_avalanche'):
    print(link.get('massif'))
    print(link.get('datebulletin'))
   

for link2 in soup.find_all('risque'):
    print(link2.get('risque1'))
    print(link2.get('altitude'))
    print(link2.get('risque2'))

# print(soup.find_all('risque'))

# # right now the for loop in the function is run multiple times need to figure out where the other risques are coming from
# def risk_fun():
#     for link2 in soup.find_all('risque'):
#         risk1 = str(link2.get('risque1'))
#         altitude = str(link2.get('altitude'))
#         risk2 = str(link2.get('risque2'))
#     return risk1, risk2, altitude



#want to get date
#want to get elevation
#want to get risk level
#location



