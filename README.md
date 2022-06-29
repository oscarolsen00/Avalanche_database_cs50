READ ME:

This is a web-app that allows you to search through a database of avalanche reports and see a simplified version of the live avalanche report in the chosen location. 

before running make sure packages are installed and up to date:
pip3 install bs4
pip3 install requests

check you are in the right directory i.e run "cd final"

run this web-app by running "flask run" and open the link in the terminal this will direct you straight to the home page. On the home page you will be given the oppurtunity to read a bit about avalanches and watch an incredibly informative video about Xavier Delerue's experience with an incredibly large avalanche. 

On the top right top right you will see 3 tabs, Home which is the page you are by default sent to; Search which takes you to the search page; and data whih retruns all the relevant data that is currently in the database through table.html

The search page- On this page you will see a search bar with a drop down list of options select one of the options to then be re-directed to a page called data.html. On this page you will see the current avalanche grade status and the type of avalanche that is likely. this information is scraped directly from the website displaying the avalanche report in that location. On this page you will also find an interactive map called FATMAP which will load the mountains in the area selected and give you recomended ski routes in that area.

the data page will show you the most recent avalanche status since the database was last updated. There is a cloumn showing the location, a column showing the grade, a column showing the type of avalanche and a column showing the time stamp of when that locations data was last updated. 

enjoy the mountains safely!

youtube video: https://youtu.be/JTKEwINvaXI 