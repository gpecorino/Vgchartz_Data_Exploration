# Video Game Data Base EDA
**Description**

This project takes a look into trends in video games sales to better understand the history of the market and the direction it may be heading in. Using python and data science principals we will visualize the data and use our findings to come to insightful conclusions about trends in the video game market. To do this we pull data from a public database at [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1). To do this the project was split into 2 parts:
1. Webscraping from the VGChartz database to a csv file so that we would have an easy to access version of our data on hand.
2. Performing EDA on the data

In this repository there is a python file containing the code for webscraping and a juypter notebook with all of the EDA work.

**About the Dataset**

This dataset was pulled from [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1) and contains the first 19000 enteries. The data after point this is missing all sales data so it was ommited from further analysis. This dataset has 12 features:
1. Rank - Order of games in list based on Global Sales in descending order
2. Name - Name of game
3. Publisher - Publisher that released game
4. Developer - Developer that created game
5. Platform - Console that the game was on
6. Release_date - Year of games release
7. Genre - Genre of game
8. Sales_NA - Sales in the North American region
9. Sales_PAL - Sales in PAL region which include Europe, New Zealand, Australia, India, Middle East and South Africa.
10. Sales_JP - Sales in Japan
11. Sales_Others - Sales from other regions not already convered
12. Sales_Globe - Total sales from all regions

**Conclusions**

**Technologies**

+ Python: Primary language used for webscrapping and data processing/analysis
+ Pandas: Used for data manipulation and analysis
+ Matplotlib: Used for data visualization
+ BeautifulSoup: Used for reading html for webscrapping

**Areas for Improvement**

There are still ways in which this project could be improved upon.

The fisrt area for improvement is the webscrapping code. When running this code over extended periods of time we run into a problem where we loose connection to the database and have to start the code again to continue scrapping. The code rarely was able to get past 3000 entereies before loosing connect, so depending on the size of the data you are scrapping through this might not be an issue. In practice the simplets solution was to add the data that had already been scrapped to our csv file then to run the code again from the last completed entery and repeat this cycle until you have all your desired data. Though this solution does work I would like to find a way to maintain a stable connection for a longer period of time and to reduce the overall runtime of the code. Doing so would allow this to be a script that you only need to run once.

The second area for improvement is that I would like to add a Machine learning section at the end of the EDA to create a model that can accurately predict total sales. This model will use the data in our 5 year window of 2014-2018 to focus on more recent trends and give our model better results. The main obsticle is figuring out how to handle the large amount of missing regional sales data we have in this window and doing further feature engeneering. 
