#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


df = pd.read_csv("2017-fordgobike-tripdata.csv")


# In[4]:


df


# # The dataset includes:
# an ID number for each bike
# 
# how long it was rented for, in seconds
# 
# the starting station and end station id's, latitude, longitude of the starting and end stations and starting and end station names
# 
# the start and end time
# 
# user type, means whether customer or subscriber
# 
# There are 519700 rows and 13 columns

# In[5]:


df.info()


# In[6]:


df.shape


# In[7]:


df.columns


# In[8]:


df.dtypes


# In[9]:


df.user_type.unique()


# ## 

# In[10]:


df.user_type.value_counts()


# In[11]:


df.columns


# In[12]:


df1=df.copy()


# In[13]:


df1


# ### Top 10 bikes details which are highest duration ?

# In[14]:


df1.sort_values('duration_sec',ascending=False).head(10)


# ### Total number of bikes used in the dataset?

# In[15]:


len(df1["bike_id"].unique())


# ### which bike is used for more number of times ?

# In[16]:


df1["bike_id"].value_counts()


# bike with id "68" used highest time compared to all the bikes, and it is used for 457

# ### What is the total number of Customer type users?

# In[17]:


print("Total number of Customer type users : ",len(df1[df1["user_type"]=="Customer"]))


# There are 110470 Customer type users

# ### What is the total number of Customer type users ?

# In[18]:


print("Total number of Subscriber type users : ",len(df1[df1["user_type"]=="Subscriber"]))


# There are 409230 Subscriber type users

# ### bikes list which have starting and end stations as same?

# In[19]:


starting_stations=set(df1["start_station_name"])
ending_stations=set(df1["end_station_name"])


# In[20]:


for i in starting_stations:
    d=df1[((df1["start_station_name"]==i) & (df1["start_station_name"]==i))]
    
d  


#   

# ### which bike is used with less duration?

# In[21]:


min_duration=df1[df1["duration_sec"]==df1["duration_sec"].min()]
min_duration


# so, there are lot of bikes with minimum duration.
# 
# we can find total number of bikes with minimum duration by using below code

# In[22]:


len(min_duration)


# there are 68 bikes with same minimum duration
# 
# in this 68 bikes, we can find how many Customer and Subscriber type users by using below code

# In[23]:


print("Total number of Customer type users whose duration time is minimum : ",len(min_duration[min_duration["user_type"]=="Customer"]))

print("Total number of Customer type users whose duration time is minimum : ",len(min_duration[min_duration["user_type"]=="Subscriber"]))


# so, there are 8 Custermers and 50 subscribers with mimimum duration speed

# ### what is the bike id which has the maximum duration time?

# In[24]:


print("bike id which has maximum duration time is : ",df1[df1["duration_sec"]==df1["duration_sec"].max()]["bike_id"])


# 

# In[25]:


df1.columns


# ### Change the duration into time minutes from seconds?

# In[28]:


df1['duration_min'] = df1['duration_sec'] / 60  
df1


# ### Change the duration into time hours from minutes?

# In[ ]:


df1['duration_hour'] = df1['duration_min'] / 60


# In[29]:


df1


# In[30]:


df1.info()


# In[33]:


df['modified_start_time'] = pd.to_datetime(df['start_time '], format = "%Y-%m-%d")


# In[34]:


df1["duration_hour"]


# In[ ]:


df1.start_time = pd.to_datetime(df1.start_time)
df1.end_time = pd.to_datetime(df1.end_time)


# In[35]:


df1


# ### Changing the change the data type for the column start_time and end_time to datetime type?

# In[36]:


df1.info()


# ### Creating the column month name,month number,day name,date and hour when started by using start_time column?

# In[37]:


df1['start_time_month_name']=df1['start_time'].dt.strftime('%B')
df1['start_time_month_number']=df1['start_time'].dt.month.astype(int)
df1['start_time_weekday']=df1['start_time'].dt.strftime('%a')
df1['start_time_day']=df1['start_time'].dt.day.astype(int)
df1['start_time_hour']=df1['start_time'].dt.hour


# 

# In[38]:


df1


# # creating the column month name,month number,day name,date and hour when ended by using end_time column

# In[ ]:


df1['end_time_month_name']=df1['end_time'].dt.strftime('%B')
df1['end_time_month_number']=df1['end_time'].dt.month.astype(int)
df1['end_time_weekday']=df1['end_time'].dt.strftime('%a')
df1['end_time_day']=df1['end_time'].dt.day.astype(int)
df1['end_time_hour']=df1['end_time'].dt.hour


# In[39]:


df1


# In[40]:


df1.info()


# In[41]:


df1.columns


# ### Extract the data of the records which have the duration moretham 15 hours?

# In[45]:


p=df1[df1["duration_sec"]>=15]
p


# ### Extracting the user_type, starting and end station name for the bike id 1729?

# In[47]:


df1.loc[1729,["user_type","start_station_name","end_station_name"]]


# In[46]:


df1.columns


# ### Between Customers and the Subscribers who are using the bike services?

# In[54]:


df[df['user_type']=='Customer']


# In[52]:





# In[ ]:




