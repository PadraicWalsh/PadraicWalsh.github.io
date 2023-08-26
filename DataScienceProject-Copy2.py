#!/usr/bin/env python
# coding: utf-8

# CONTEXT: 
#         
#          
#         The dataset for the project is based on the National Basketball Association (NBA), for the period of 1996-2022. 
#         The NBA is a professional basketball league in North America, made up of 30 teams (at present), with 29 teams 
#         from the USA, and 1 team from Canada. 
#         
#         The dataset has been scraped from Kaggle (all_seasons.csv), and It contains a broad range of players stats who were 
#         registered to a NBA team’s roster for the aforementioned time period.
#         
#         The dataset contains 12,306 rows and 22 columns. Each row corresponds to a single player's stats from the time 
#         period indicated.
#         
#         OBJECTIVES 
# 
#         -To clean the new dataframe from the all_seasons.csv
# 
#         -To explore single distribution and numerical categorical features using stats & visualizations.
# 
#         -To explore the correlation of multiple features using the players stats & to plot their findings. 
# 
# 
#         The project will be very much geared towards the Exploratory Data Analysis end of things, to better understand the         dataset, and to discover any possible trends and insights.
# 
#         
#         
#          

# In[1]:


import pandas as pd


# In[2]:


nba_stats = pd.read_csv('all_seasons.csv')


# In[3]:


nba_stats.head()


# In[4]:


#I want to look at the Dataframe's info summary and columns


# In[5]:


nba_stats.info()


# In[6]:


# After checking the info in the DF, there appears to be no null values.
# There are columns that are not needed, so they will be removed.
# Some of the columns classified as object, will also be changed to a more appropriate data type.


# In[7]:


# Looking at the info summary table above, it appears that there are no null values in the dataset. Just to be certain, the next few
# lines of code will verify that.


# In[8]:


nba_stats.dropna().info()


# In[9]:


nba_stats.isnull()


# In[10]:


nba_stats.isna().sum()


# In[11]:


# The shape method below gives us the dimensions of the dataframe i.e. the no. of rows & columns.


# In[12]:


nba_stats.shape


# In[13]:


# Create the new database with the desired columns only.


# In[14]:


nba_stats = nba_stats [['player_name','team_abbreviation', 'country', 'player_height', 'player_weight',
                       'pts', 'reb', 'ast', 'net_rating', 'ts_pct', 'season' ]]


# In[15]:


nba_stats.head()


# In[16]:


nba_stats.columns


# In[17]:


nba_stats.info()


# In[18]:


# It would be better to change 'player_name','team_abbreviation', 'season' and 'country' to a string dtype.


# In[19]:


nba_stats = nba_stats.astype({'player_name': 'string', 'team_abbreviation': 'string', 'country': 'string', 'season': 'string'})


# In[20]:


# Let's check the info summary to verify the changes made.


# In[21]:


nba_stats.info()


# In[22]:


# Some of the column names are difficult to understand. They should be renamed to make them more readable. 


# In[23]:


nba_stats = nba_stats.rename(columns = {'team_abbreviation': 'team','pts': 'points_avg','reb': 'rebound_avg',
                                    'ast': 'assist_avg', 'ts_pct': 'shooting_pct'})


# In[24]:


# Changes to column names are verified below.


# In[25]:


nba_stats.head()


# In[26]:


# Now that the dataset has been cleaned & transformed, exploratory analysis can begin.


# In[27]:


nba_stats['team'].nunique()


# In[28]:


#The value of 36 represents the total amount of teams who participated in the NBA during the period of 1996-2022.


# In[29]:


# The describe method below gives us a good insight into the central tendencies of the dataset.


# In[30]:


nba_stats.describe()


# In[31]:


nba_stats['points_avg'].describe()


# In[32]:


# We can also retrieve useful information on non numeric columns using the describe method. 


# In[33]:


nba_stats.describe(include = ['string'])


# In[34]:


# We can see there are 2,463 unique players in the dataset & Cleveland had the most players rostered (433) 
# during the time period of 1996-2022, as well as 82 countries represented across the 26 seasons for example.
# If we want to have a more indepth look at non numeric columns counts we can use a for loop.


# In[35]:


other_cols = nba_stats.select_dtypes(include= ['string']).columns
other_cols


# In[36]:


for col in other_cols:
    print(nba_stats[col].value_counts())
    print()


# In[37]:


# We can plot some of our findings, for example the count of players rostered with each of the teams


# In[38]:


nba_stats['team'].value_counts().plot(kind = 'bar')


# In[39]:


# From the chart we can see that approx 2/3 of the teams had over 400 players rostered during this time period.
# It was surprising to see that the New Orleans/Oklohoma Hornets had the fewest players (32), however, this was
# because the franchise was in existence for only 2 years, due to the devastating affects of hurricane Katrina in 2005.


# In[40]:


nba_stats[['assist_avg']].hist() # the hist function can be used to visualize various dimensions.


# In[41]:


# We can also visualize multiple dimensions to illustrarte the distrubtion to help us identify any unusual observations.


# In[42]:


nba_stats[['points_avg', 'rebound_avg', 'assist_avg', 'net_rating']].hist(figsize = (20,10), bins = 20)


# In[43]:


# On observation of the points/rebounds/assists histograms, we can see that they are right skewed. The outliers
# representing those higher stats of the more elite players, compared to the more average players stats. 
# The net rating indicates a steep kurtosis, with more values in the distribution tails and values closer to the mean,
# indicated by the peak and the sharper tails.


# In[44]:


nba_stats[['points_avg','rebound_avg', 'assist_avg']].agg(['mean', 'median', 'max'])


# In[45]:


# using the groupby method we want to get a range of all the points averages in the dataset


# In[46]:


nba_stats.groupby(by = 'points_avg').groups.keys()


# In[47]:


nba_stats.sort_values('points_avg').tail() # shows us the top 5 player's points averages.


# In[48]:


nba_stats.groupby('player_name')[['player_height', 'shooting_pct']].mean()


# In[49]:


nba_stats.groupby('season')['assist_avg'].max()


# In[50]:


nba_stats.groupby('player_name')['shooting_pct'].describe()


# In[51]:


nba_stats.groupby('player_name')[['points_avg', 'rebound_avg', 'assist_avg']].agg(['mean', 'max'])


# In[52]:


# using the pivot table function we can get a multi dimensional view of data for each season.


# In[53]:


pd.pivot_table(nba_stats,
               index = ['season'],
               values = ['points_avg', 'assist_avg', 'rebound_avg'],
               aggfunc = 'max')
               


# In[54]:


# we can then compare the max values above with the mean values for the same season


# In[55]:


pd.pivot_table(nba_stats,
               index = ['season'],
               values = ['points_avg', 'assist_avg', 'rebound_avg'],
               aggfunc = {'points_avg' : ['mean','max'],
                          'assist_avg' : ['mean','max'],
                          'rebound_avg' : ['mean','max']})


# In[56]:


# We can check for any correlation between the various columns.


# In[57]:


import seaborn as sns
# We can also use the seaborn library to visualize observations
# and the heatmap below shows us other dimensions that are/ are not strongly correlated. 
# Some of the seaborn graphs were learned from the seaborn website. See references at end.


# In[58]:


sns.heatmap(data = nba_stats.corr(), cmap = 'coolwarm', )


# In[59]:


# From the heatmap there appears to be a strong correlation between player height and player weight.


# In[60]:


# Part of this next piece of code was learned on the matplotlib website. See reference at end of project.


# In[61]:


import matplotlib.pyplot as plt
plt.figure(figsize=(4,4))
ax = plt.axes()

ax.scatter(nba_stats.player_height, nba_stats.player_weight,s=10,c='r')

ax.set(xlabel='Player Height (cm)',
       ylabel='Player Weight (kg)',
       title='Correlation between Player Height vs Weight');


# In[62]:


# The pairplot function can also be used to showcase the subset of variables, or to plot different 
# types of variables on rows and columns.


# In[63]:


sns.pairplot(nba_stats, x_vars = ['player_weight', 'player_height'],
                        y_vars = ['player_weight', 'player_height'])


# In[64]:


plt.figure(figsize=(3,3))
ax = plt.axes()

ax.scatter(nba_stats.player_height, nba_stats.points_avg,s=10,c='blue')

ax.set(xlabel='Player Height (cm)',
       ylabel='Average Points Scored',
       title= 'Player Height and Average Points Scored');


# In[65]:


# As we can see from the visual above, it's not the tallest players who have the highest points averages.


# In[66]:


# We can also explore the players physical characteristics by country


# In[67]:


country_averages = nba_stats[['country', 'player_weight', 'player_height' ]]


# In[68]:


country_averages.groupby('country').mean()


# In[69]:


sns.displot(data = nba_stats, x = 'player_height', binwidth = 5)


# In[70]:


# The catplot below shows us better any outliers that may be skewing the distribution.
sns.catplot(data = nba_stats, y = 'points_avg', kind = 'box')


# In[71]:


sns.catplot(data = nba_stats, x = 'team', kind = 'count', aspect = 3)

# The below chat visualizes graphically a count of the total players rostered for each team.


# In[72]:


nba_stats.groupby('team')['player_name'].count()
# We can get the exact count of the players using groupby.


# In[73]:


# We can use the col function to see subsets of the data i.e. each different season, 
# with its own points average, and to plot them separately.


# In[74]:


# Displot allows us to plot the distribution of the data.
sns.displot(data = nba_stats, x = 'points_avg', col = 'season', kind = 'hist') 


# In[75]:


# Using catplot again we can get a looks at the stats for each individual season. In this example the assist-avg
sns.catplot(data = nba_stats, x = 'assist_avg', y = 'season', kind = 'bar', aspect = 2)


# In[76]:


# The next few lines of code will to try to visualize the top 50 points averages in descending order.
# The drop_duplicates function was found on stack overflow, as I didn't want the players names to be
# repeated on the list. 


# In[77]:


players = nba_stats.drop_duplicates('player_name')


# In[78]:


top_points_scorer_avg = nba_stats.sort_values('points_avg', ascending = False)


# In[79]:


top_avg = top_points_scorer_avg[:50]


# In[80]:


sns.relplot(data=top_avg, x='points_avg', y='player_name', kind = 'scatter', aspect = 1.5)


# In[81]:


# We can see from the plot, that James Harden has the highest points average during the period of 1996- 2022.


# CONCLUSION: 
# 
# Overall it has been a very interesting process of analysing a dataset in-depth for the first time. Certain assumptions you
# may of had prior, particularly in relation to the players physical attributes, provides us with the factual evidence to 
# support or reject the assumptions. 
# 
# Some of the functions were a lot of fun to explore with, in particular 'group by' and 'pivot table'. Their ability to drill 
# down into the data and provide you with rapid results was fascinating.
# 
# Learning this kind of code in relation to data cleaning, transforming and EDA, gives a sense of confidence to practice these
# techniques on other datasets, and the appetite to keep learning more.
# 

# REFERENCES:
# 
# https://www.kaggle.com/datasets/justinas/nba-players-data
# 
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
# 
# https://seaborn.pydata.org/tutorial/introduction.html
# 
# https://seaborn.pydata.org/tutorial/categorical.html
# 
# https://seaborn.pydata.org/tutorial/color_palettes.html?highlight 
# 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot
# 
# 

# In[ ]:




