# Video Game Database EDA
## Description

This project dives into trends in video game sales to better understand the history of the market and help predict future trends. Using python and data science principals I will visualize the data and use our findings to develop insightful conclusions about trends in the video game market. To do this we pull data from a public database at [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1). The project will be split into 3 parts:
1. Webscraping from the VGChartz database to a csv file so that we would have an easy to access version of our data on hand.
2. Performing EDA on the data
3. Creating a Machine Learning Model to predict sales

This repository contains a Python file containg the code for web scraping and a Jupyter Notebook with all of the EDA work.

## About the Dataset

The dataset was pulled from [VGChartz.com](https://www.vgchartz.com/games/games.php?page=1&results=1000&order=TotalSales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=0&showvgchartzscore=0&showcriticscore=1&showuserscore=1) contains the first 19000 enteries. All data after this point is missing sales data thus it was ommited from further analysis. This dataset has 12 features:
1. Rank - Order of games in list based on Global Sales in descending order
2. Name - Name of game
3. Publisher - Publisher that released game
4. Developer - Developer that created game
5. Platform - Console that the game was on
6. Release_date - Year of games release
7. Genre - Genre of game
8. Sales_NA - Sales in the North American region
9. Sales_PAL - Sales the in PAL region which include Europe, New Zealand, Australia, India, Middle East and South Africa.
10. Sales_JP - Sales in Japan
11. Sales_Others - Sales from other regions not already covered
12. Sales_Globe - Total sales from all regions

## Conclusions

Like many industries based on artistic choice certain trends emerge that shape consumer preferences and drive sales. Games with faster-paced mechanics often garner more attention and enjoy higher sales figures. This is evident in the market dominance of genres such as sports, shooters, action, platformer, and racing. Moreover, Nintendo stands out as a powerhouse in the industry, consistently outperforming all other publishers in sales. Nintendo's succesful titles and long running franchise underscores the importance of brand recognition and consumer loyalty. Similarly, games from well-established franchises exhibit remarkable sales performance and longevity, showcasing the influence of brand identity on consumer behavior. Notably, Sony PlayStation platforms emerged as frontrunners in overall video game sales, highlighting their strong market presence and appeal among gamers compared to competitors.

My machine learning model uses data from 2013-2017, the last 5 years of available data. I limit it to this window to isolate recent trends and avoid being influenced by older ones. The model captures some of the trends present in the data, as illustrated in the graph below. Although the R-squared value for this model is low, this model serves as a solid starting point. While there are potential improvements, the model's performance is constrained by the limitations of the data. The dataset contains only a few usable variables, which makes it challenging to capture more nuanced trends. I further discuss ways in which this model could be improved in the **Area for Improvement** section. 

![](images/ml_result.png)

## Technologies

+ Python: Primary language used for webscrapping and data processing/analysis
+ Pandas: Used for data manipulation and analysis
+ Matplotlib: Used for data visualization
+ BeautifulSoup: Used for reading html for webscrapping

## Areas for Improvement

There are still ways in which this project could be improved upon.

The first area for improvement is the webscrapping code. When running this code over extended periods of time loosing connection to the database became an issue. However, depending on the data's size, this might not be an issue. The simplest solution was to add the data that had already been scrapped to our csv file then to run the code again from the last completed entry and repeat this cycle until you have all your desired data. Though this solution does work, I would like to find a way to maintain a stable connection for a longer period of time and to reduce the overall runtime of the code. Doing so would allow this to be a script that you only need to run once.

The second area for improvement is my machine learning model. Several strategies could potentially enhance its performance:
1. **Increase the Amount of Data**: Including data from additional years could provide the model with more information, enhancing its ability to identify trends. However, this approach risks incorporating outdated trends that may not be relevant today, potentially biasing the model and decreasing its performance.
2. **Better Handling of Missing Data**: In this analysis, I dropped all rows with missing data, which reduced the dataset's size. Developing a method to impute these missing values with reasonable estimates could increase efficiency. Relying too heavily on imputed data might lead the model to detect false trends.
3. **Feature Engineering**: Creating new features from the existing data could enrich the dataset without depending on speculative values. Despite this potential, the limited number of original variables poses a challenge in generating additional meaningful features.

While there are various approaches to enhance the model, careful implementation is crucial. Each method comes with its own set of risks, and improper application could inadvertently degrade the model's performance.
