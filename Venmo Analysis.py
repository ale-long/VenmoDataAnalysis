#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('venmoSample.csv')


# In[3]:


df.head()


# In[4]:


df.drop('is_business', axis=1, inplace=True)


# In[5]:


df.drop('story_id', axis=1, inplace=True)


# In[6]:


df.head()


# Total Number of Transactions

# In[7]:


df['user2'].count()


# Converting Time Str to an accessible format 

# In[140]:


df['datetime'] = pd.to_datetime(df['datetime'])


# In[141]:


df['Hour'] = df['datetime'].apply(lambda time: time.hour)
df['Month'] = df['datetime'].apply(lambda time: time.month)
df['Day of Week'] = df['datetime'].apply(lambda time: time.dayofweek)
df['Year'] = df['datetime'].apply(lambda time: time.year)


# In[142]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# In[143]:


df.head()


# Insight 1 -Analyzing # of transactions with respect to time(day of week, month, and hour)

# In[144]:


day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sns.countplot(x='Day of Week',data=df,hue='transaction_type',palette='viridis', order = day_order)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Ratio of Payments to Charges per Day')


# In[145]:


sns.countplot(x='Month',data=df,hue='transaction_type',palette='viridis')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('Ratio of Payments to Charges per Month')


# In[146]:


day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
sns.countplot(x='Day of Week',data=df,palette='coolwarm', order=day_order)
plt.title('Total Number of Transactions(Days)')


# In[147]:


sns.countplot(x='Month',data=df,palette='coolwarm')
plt.title('Total Number of Transactions(Months)')


# In[148]:


sns.countplot(x='Hour',data=df,palette='coolwarm')
plt.title('Total Number of Transactions(Hours)')


# Heatmap for time vs # of transactions 

# In[149]:


Hour_day = df.groupby(by=['Day of Week','Hour']).count()['transaction_type'].unstack()
Hour_day.head(7)


# In[150]:


plt.figure(figsize=(12,6))
sns.heatmap(Hour_day,cmap='viridis')


# In[151]:


Month_day =  df.groupby(by=['Day of Week','Month']).count()['transaction_type'].unstack()
Month_day.head()


# In[152]:


plt.figure(figsize=(12,6))
sns.heatmap(Month_day,cmap='viridis')


# Confirming that we are getting the correct data for our heatmap 

# In[20]:


df[(df['Month'] == 1) & (df['Day of Week']=='Fri')].count()


# Month to hour heatmap

# In[84]:


Month_hour =  df.groupby(by=['Hour','Month']).count()['transaction_type'].unstack()
Month_hour.plot()


# In[22]:


plt.figure(figsize=(12,6))
sns.heatmap(Month_hour,cmap='viridis')


# Mutual Connections

# In[220]:


def find_connections(user_id):
    # 1st Degree Connections
    connections1 = []
    # 2nd Degree Connections
    connections2 = []
    # 3rd Degree Connections
    connections3 = []
    for(idx,row) in testing_df.iterrows():
        # Find connections in user1 column, and append to 1st degree 
        if(row.loc['user1'] == user_id):
            count = 0
            # Only append if there are no duplicates
            for check in connections1:
                if(row.loc['user2'] == check):
                    count+=1
            if(count==0):
                connections1.append(row.loc['user2'])
        # Find connections in user2 column, and append to 1st degree
        if(row.loc['user2'] == user_id):
            count = 0
            for check in connections1:
                if(row.loc['user1'] == check):
                    count+=1
            if(count==0):
                connections1.append(row.loc['user1'])
        #Find potential connections from 1st degree connections, append to 2nd degree
        for c in connections1:
            count = 0
            # Find connections in user1 column
            if(row.loc['user1'] == c):
                # Avoids adding own user as a connection
                if(row.loc['user2']!= user_id):
                    # Check for duplicate connections
                    for check in connections2:
                        if(row.loc['user2'] == check):
                            count+=1
                    for check in connections1:
                        if(row.loc['user2'] == check):
                            count+=1
                    if(count==0):        
                        connections2.append(row.loc['user2'])
            # Find connections in user2 column 
            if(row.loc['user2'] == c):
                count = 0
                # Avoids adding own user as a connection
                if(row.loc['user1']!= user_id):
                    # Check for duplicate connections
                    for check in connections2:
                        if(row.loc['user1'] == check):
                            count+=1
                    for check in connections1:
                        if(row.loc['user1'] == check):
                            count+=1
                    if(count==0):
                        connections2.append(row.loc['user1'])
        # Find connections from 2nd degree connections, appending for connection 3
        for c in connections2:
            count_dup = 0
            # Find connections in user1 column
            if(row.loc['user1'] == c):
                # Avoids adding own user as a connection
                if(row.loc['user2']!= user_id):
                    # Checks for already existing connections from 1st Degree
                    for check in connections1:
                        if(row.loc['user2'] == check):
                            count_dup+=1
                    # Check for duplicates within 3rd degree list
                    for check in connections3:
                        if(row.loc['user2'] == check):
                            count_dup+=1
                    if(count_dup==0):
                        connections3.append(row.loc['user2'])
                    
            # Find connections in user2 column 
            if(row.loc['user2'] == c):
                count = 0
                # Avoids adding own user as a connection
                if(row.loc['user1']!= user_id):
                    # Checks for duplicate connections
                    for check in connections1:
                        if(row.loc['user1'] == check):
                            count+=1  
                    # Check for duplicates within 3rd degree list
                    for check in connections3:
                        if(row.loc['user1'] == check):
                            count+=1
                    # Only append if there are no duplicates found in either list
                    #print(count)
                    if(count==0):
                        connections3.append(row.loc['user1'])
                        
    # Removing duplicate connections from all degrees
    for c1 in connections1:
        for c2 in connections2:
            if(c1 == c2):
                connections2.remove(c2)
        for c3 in connections3:
            if(c1 == c3):
                connections3.remove(c3)
    
    for c2 in connections2:
        for c3 in connections3:
            if(c2 == c3):
                connections3.remove(c3)
    
    print("User " + str(user_id) + " connections are: " + "1st Degree"+str(connections1) + ", 2nd Degree" +str(connections2)
         +", 3rd Degree" + str(connections3)) 
    


# Adding some dummy data to test connection algorithm

# In[34]:


testing_df = pd.DataFrame(df.head(30))


# In[38]:


testing_df.head()


# Inserting dummy data from above

# In[39]:


testing_df = testing_df.append(pd.DataFrame([[1218774, 1111111 , 'n','n','n','n','n','n']],columns = testing_df.columns), ignore_index=True)


# In[40]:


testing_df.head(32)


# In[49]:


testing_df = testing_df.append(pd.DataFrame([[1234567,1528945,'n','n','n','n','n','n']],columns = testing_df.columns), ignore_index=True)


# In[52]:


testing_df = testing_df.append(pd.DataFrame([[1111111,123,'n','n','n','n','n','n']],columns = testing_df.columns), ignore_index=True)


# In[42]:


testing_df = testing_df.append(pd.DataFrame([[1234567,2222222,'n','n','n','n','n','n']],columns = testing_df.columns), ignore_index=True)


# In[43]:


testing_df = testing_df.append(pd.DataFrame([[1218774,2323,'n','n','n','n','n','n']],columns = testing_df.columns), ignore_index=True)


# In[94]:


testing_df.head(40)


# In[221]:


find_connections(1218774)


# In[222]:


find_connections(1528945)


# In[76]:


testing_year_column = testing_df.head(30)


# In[77]:


testing_year_column['Year'] = pd.DatetimeIndex(testing_year_column['datetime']).year  


# In[200]:


Month_year =df.groupby(by=['Year','Month']).count()['transaction_type'].unstack()
Month_year_data = pd.DataFrame(Month_year, index=None, columns = None)


# In[201]:


Month_year_data.head()


# In[202]:


Month_year_data['Year'] = Month_year_data.index


# In[212]:


Month_year_data.drop(index=2011, axis=0, inplace = True)


# In[213]:


Month_year_data.drop(index=2012, axis=0, inplace = True)


# In[217]:


Month_year_data


# In[215]:


Month_year_data.plot()


# In[ ]:




