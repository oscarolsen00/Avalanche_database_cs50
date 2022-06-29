# import library
from bs4 import BeautifulSoup
import requests

url="https://www.varsom.no/en/avalanche-bulletins/forecast/Indre%20Troms/"
url2="https://www.varsom.no/en/avalanche-bulletins/forecast/Trollheimen/"
req=requests.get(url2)
content=req.text

soup=BeautifulSoup(content,'html.parser')
risk_block =soup.find("div", {"class" : "description"}).h2
risk_block_text = risk_block.text
print(risk_block.text)


