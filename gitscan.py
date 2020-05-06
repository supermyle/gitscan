import requests #Import python requests library
from bs4 import BeautifulSoup #Create Beatiful Soup object that takes scraped HTML content as input

username = input("Type the username of the github.com user you would like stats on : ") #Prompt user

URL = 'https://github.com/' + username
page = requests.get(URL) #Perform HTTP request
soup = BeautifulSoup(page.content, 'html.parser') #User appropriate parser

basicinfo = soup.findAll(class_='Counter hide-lg hide-md hide-sm') #Get info from HTML class
index = 0 #Index for for loop iteration
for x in basicinfo:
		info = x.get_text().strip() #Take out tags and whitespace
		overview = ["Repositories ", "Projects ", "Stars ", "Followers ", "Following "] #List of overview info
		print(overview[index] + info) #Print overview info and its statistics 
		index += 1
