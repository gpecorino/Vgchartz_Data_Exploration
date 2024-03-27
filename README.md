# Video Game Data Base EDA
**Description**

This project takes a look into trends in video games sales to better understand the history of the market and the direction it may be heading in. Using python and data science principals we will visualize the data and use our findings to come to insightful conclusions about trends in the video game market. To do this we pull data from a public database at [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1). To do this the project was split into 2 parts:
1. Webscraping from the VGChartz database to a csv file so that we would have an easy to access version of our data on hand.
2. Performing EDA on the data

In this repository there is a python file containing the code for webscraping and a juypter notebook with all of the EDA work.

**About the Dataset**

This dataset was pulled from [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1) and contains the first 19000 enteries, the data after this is missing all sales data so it was ommited from further analysis. This dataset has 12 features:
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
