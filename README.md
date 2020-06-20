# VenmoDataAnalysis
After finishing a data science course on Udemy, I decided to apply the knowledge I have gained to a real world scenario. I mainly focused on exploratory analysis, feature engineering, and visualization of data to find trends that would generate useful insights for Venmo. All of the work is done through Jupyter Notebook and visualizations are included in the .ipynb file 

# Analysis 
I created multiple graphs(countplot, heatmap, line graph) visualizing the trends of # of transactions to a specific time measurement(hours, month, day of the week). These graphs contain data from all the years ranging from 2013 to 2016. A common pattern I noticed is that most transactions occur during April and May, which was interesting to see, as I originally thought that the highest usage would be during the holiday seasons in November and December. 

When we look at usage during days of the week, we can see that the higest number of transactions occur during the weekends throughout all the years. This is expected because people would have more time to spend money on different types of items and services. 

Now, lets look even closer and find the trends in usage by the hours. We can see a high amount of transactions starting at hour 0(midnight), in which it gradually decreases as we approach 9-10 AM. There is a gradual increase from 10 AM to 11 PM, and the number of transactions peak at 11 PM. The high number of transactions during hour 16 - 19 may be correlated with busy commuting hours and paying Uber or Lyft drivers. 

# Insights
From our data, I have developed a few insights that could possibly help Venmo save money or even profit. 
- Hold promotional events during time frames were there is the least amount of transactions to boost up usage, or during rush hour to attract even more users to use the platform. 
- During times where there is low activity, we could reduce some of the company's services to save money. It would not be necessary to have all the servers running during periods of low usage. 
- Creating a rewards program would be a strong incentive to preserve usage. During rush hour, there could be a double rewards time frame, which may boost profits even more. 

# Mutual Connections Feature
I implemented a function that displays a user's connections based on their user id and who they interacted with. The connections are separated by 1st, 2nd, and 3rd degree connections. This feature may be useful if a user might have forgotten to pay someone and did not know their name, and it so happens that one of the user's friend knows that person as well. This would pop up in the mutual connections feature and allow the user to successfully make the payment, saving time and stress. There are limitations to this feature, because if a user does not have a profile picture that shows their face, the scenario I described above would not work. However, there is certainly no harm in implementing an additional feature. The code for this function has been noted in the Jupyter Notebook. 

# Credits
Udemy Course: https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/ by Jose Portilla 
Venmo Dataset Download: https://www.dropbox.com/s/izchy7841iuusz5/venmoSample.csv?dl=0&fbclid=IwAR2OrqXh6W0eMzyGCPmNmXfG4U4zyL-ezKq3Ym2sekuHU4laSQZNEqOVls0

# Thank You! 
