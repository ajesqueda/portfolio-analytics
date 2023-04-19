#!/usr/bin/env python
# coding: utf-8

# 
# ## Alfonso Esqueda
# ### EDA on Olympics Dataset

# In[1]:


#Import pandas, numpy, and matplotlib.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


# Reading Olympics csv file
df = pd.read_csv('olympics.csv')
df


# ### 1. Impute the missing weight values. Explain your process and how you chose your imputation method.

# In[3]:


plt.scatter( df['Age'], df['Weight'], alpha = 0.4, color = "green")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.show()


# In[4]:


df["Weight"] = df["Weight"].fillna(df["Weight"].mean()).round(2)
print(df["Weight"])


# #### I chose the mean (155.89) to fill in for the missing values in the weight column because it is equally distributed and there is not significant outliers in this dataframe. 
# #### To impute I used the .fillna() function and used the aggregate function .mean()

# ### 2. Impute the missing height values. Explain your process and how you chose your imputation method. 

# In[5]:


plt.scatter( df['Age'], df['Height'], alpha = 0.4, color = "blue")
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()


# In[6]:


df["Height"] = df["Height"].fillna(df["Height"].mean()).round(2)
print(df["Height"])


# #### I chose the mean (175.34) to fill in for the missing values in the height column because it is equally distributed and there is not significant outliers in this dataframe. 
# #### To impute I used the .fillna() function and used the aggregate function .mean()

# ### 3. Impute the ‘missing’ medal values. Hint: Replace the NaN values with something that represents a non medal winner. 

# In[7]:


df["Medal"] = df["Medal"].fillna("MISSING")
df


# ### 4.	Convert height from centimeters to inches or feet/inches. Replace the current height values with these converted values. 

# In[8]:


# Multiply the column by the conversion factor
df['Height'] = df['Height'] / 2.54
df['Height'] = df['Height'] / 12
# Round the resulting values to 2 decimal places
df['Height'] = df['Height'].round(2)


# In[9]:


df['Height'].head()


# ## Using any form of EDA (unless otherwise noted), answer the following questions: 

# ### 5.	How many medals has the United States won? 

# In[10]:


usa = df[df['Country'] == 'USA']
usa.loc[0:, ["Medal"]].value_counts()


# #### The total medals for the US is 5,637 medals

# ### 6.	Select an event of your choice:  What is the average age, weight, and height of Medalists vs non-Medalists? 

# In[11]:


#Both medalists and nonmedalists are in this dataframe 
track = df[df['Event'] == "Athletics Men's 800 metres"]
track_no_medal = track[track["Medal"] == "MISSING"]
track_medal = track[track["Medal"] != "MISSING"]

print("Non-medalists Athletes")
print(track_no_medal[["Age", "Weight", "Height"]].mean().round(2))

print("-------------------------------")
print("Medalists Athletes")
print(track_medal[["Age", "Weight", "Height"]].mean().round(2))


# ### 7.	Select a country of your choice: What Olympic event do they have the most gold Medals in? 

# In[12]:


china = df[df['Country'] == 'China']
china_medal = china[china['Medal'] ==  'Gold']
china_medal.loc[0:, ["Medal", "Event"]].value_counts().head()


# ###  China has 34 Gold medals in the Volleyball Women's Volleyball. 

# ### 8.	Using a bar chart, show the top 15 countries with the most Medals won.

# In[13]:


# replace the string "MISSING" with NaN (missing value)
df['Medal'].replace('MISSING', np.nan, inplace=True)

# create a new DataFrame with the total medals won by each country (excluding missing values)
medal_counts = df.dropna(subset=['Medal']).groupby(['Country'])['Medal'].count().reset_index(name='Total Medals')

# sort the DataFrame by the total medals won in descending order and take the top 15 countries
top_15 = medal_counts.sort_values('Total Medals', ascending=False).head(15)

# create a bar chart of the top 15 countries by total medals won
plt.bar(top_15['Country'], top_15['Total Medals'])

# set the title and axis labels
plt.title('Top 15 Countries with the Most Medals (excluding missing values)')
plt.xlabel('Country')
plt.ylabel('Total Medals')

# rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# display the bar chart
plt.show()


# ### 9.	Is there a correlation between Weight and Height? Justify your answer. Hint: use a scatterplot 

# In[14]:


sns.scatterplot(data=df, x="Weight", y="Height")


# In[15]:


g = sns.jointplot(x="Weight", y="Height", data=df, kind='reg')
regline = g.ax_joint.get_lines()[0]
regline.set_color('red')
regline.set_zorder(5)


# ### The weight and height variable are highly correlated due to the linear correlation in the graph depicted above.

# ### 10.	What is the distribution of silver Medalists and Age? What is the skewness of the data? Justify your answer. Hint: use a histogram

# In[16]:


silver_medals = df[df["Medal"] == "Silver"]
# Visualize the distribution of the target variable
sns.histplot(silver_medals["Age"], kde=True)
plt.title("Distribution of Silver Medalists and Age")
plt.xlabel("Age")
plt.ylabel("Silver Medals")
plt.show()


# ### The graph above is right skewed and positive due to the long tail to the right. A skewed distribution means that the data is not symmetrical and is skewed towards one end. In the case of a right-skewed distribution, most of the data is concentrated on the left side of the histogram, and the tail extends towards the right side.

# In[ ]:




