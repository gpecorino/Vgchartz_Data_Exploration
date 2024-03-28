#libraries
from bs4 import BeautifulSoup, element
import urllib
import requests
import pandas as pd
import numpy as np

#Set variables
start_row = 27
end_row = 1026

#Set arrays for values
rank = []
name = []
publisher = []
developer = []
platform = []
release_date = []
genre = []
# c_score = [] there are very few data entereies for crtic scores. Not worth including in final data set
#u_score = [] there are very few data entereies for user scores. Not worth including in final data set
sales_na = []
sales_pal = []
sales_jp = []
sales_other = []
sales_globe = []

#URL info
last_page = 19 #only take first 19 pages bc after that sales information becomes minimal
rec_count = 0
urlhead = 'https://www.vgchartz.com/games/games.php?page='
urltail = '&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1'

#Loops through scraping for every entry 
for page_number in range(1,last_page+1):
    url = urlhead + str(page_number) + urltail


    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, 'html')
    print('Started scraping page ',page_number)

    #Picks out table elements from webpage
    table = soup.find_all('table')

    #Pull all columns of data
    all_data = table[0].find_all('tr') #first element in list contains data we need

    #Loop to run code for a whole page
    for row in range(start_row, end_row+1):
        #Pulls individual row of data
        row_data = all_data[row].find_all('td') 

        #Parses the data and outputs an array
        individual_row_data = [data.text.strip() for data in row_data]
        individual_row_data[3] = row_data[3].find('img').attrs['alt'] #this pulls out the information about console and puts into array
        individual_row_data[2] = (row_data[2].find('a')).text.strip() #this isolates just the name of the game
        year_release = individual_row_data[13].split()[-1] #pull just year info from release date

        #get game genre
        #have to pull url for game to go to individual page to get that information
        a_data = all_data[row].find_all('a') #starts at 27
        game_url = a_data[1].attrs['href']

        #loading game page
        game_page = requests.get(game_url)

        game_soup = BeautifulSoup(game_page.text, 'html')

        #Pull Genre tag and use this to locate where genre data is, placement is different for each games webpage
        game_h2 = game_soup.find('div', {'id' : 'gameGenInfoBox'}).find_all('h2')

        #create temporary element to store location of Genre in html for conistent method to locate genre data we want
        temp_tag = element.Tag

        for h2 in game_h2:
            if h2.string == 'Genre':
                temp_tag = h2

        game_genre = temp_tag.next_sibling.string

        #Adds our data to our lists
        rank.append(np.int64(individual_row_data[0]))
        name.append(individual_row_data[2])
        platform.append(individual_row_data[3])
        publisher.append(individual_row_data[4])
        developer.append(individual_row_data[5])
        genre.append(game_genre)

        #need "if conditions" to add first 2 digits to our year since release date only includes last 2 numbers of year.
        #1970 seems to be oldest year in database
        if year_release.startswith('N/A'):
            release_date.append('N/A')
        else:
            if int(year_release) >= 69:
                full_year = '19' + year_release
            else:
                full_year = '20' + year_release
            release_date.append(np.int32(full_year))

        sales_na.append(float(individual_row_data[9][:-1]) if not individual_row_data[9].startswith('N/A') else np.nan)
        sales_pal.append(float(individual_row_data[10][:-1]) if not individual_row_data[10].startswith('N/A') else np.nan)
        sales_jp.append(float(individual_row_data[11][:-1]) if not individual_row_data[11].startswith('N/A') else np.nan)
        sales_other.append(float(individual_row_data[12][:-1]) if not individual_row_data[12].startswith('N/A') else np.nan)
        sales_globe.append(float(individual_row_data[8][:-1]) if not individual_row_data[8].startswith('N/A') else np.nan)
        
    print('Completed scraping page ',page_number)

#store data in dictionary
cols = {
    'Rank' : rank,
    'Name' : name,
    'Publisher' : publisher,
    'Developer' : developer,
    'Platform' : platform,
    'Release_date' : release_date,
    'Genre' : genre,
    # 'Critical_Score' : c_score,
    #'User_Score' : u_score,
    'Sales_NA' : sales_na,
    'Sales_PAL' : sales_pal,
    'Sales_JP' : sales_jp,
    'Sales_Other' : sales_other,
    'Sales_Globe' : sales_globe,
}

#put data in dataframe
df = pd.DataFrame(cols)

#store dataframe in csv file
df.to_csv('video_game_full.csv', index = False)
