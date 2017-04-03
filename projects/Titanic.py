
# coding: utf-8

# # Titanic - Data Analysis
# 
# ## Introduction
# 
# As taken from Kaggle, 'The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.'
# 
# The data set used for this analysis is a subset of the complete data set and contains demographics and passenger information from 891 of the 2224 passengers and crew on board the Titanic. 
# 
# For more information on the data set, visit [Kaggle](https://www.kaggle.com/c/titanic/data).
# 

# ## Goal
# 
# The goal of this analysis is to analyze the data set and provide insights or identify patterns by investigating the data set.

# ### Import Packages

# In[1]:

#Import and load necessary packages
import re
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as pyplt
from matplotlib import figure as fig
from matplotlib.gridspec import GridSpec

#This is to plot the graphs within the same jupyter cell
get_ipython().magic(u'matplotlib inline')

#Adjusting the plot area size to accommodate bigger/wider graphs
pyplt.rcParams['figure.figsize'] = 12,6


# ### Load data

# In[2]:

#Load dataset 
#This loads the csv file to a pandas data frame
#Note that the path given below is where the csv file exists locally with in Python's current working directory
#Repoint the path as necessary to make sure the function read_csv is able to find the csv

titanic = pd.read_csv("Udacity/P2/Titanic/titanic-data.csv")


# ### Data Exploration and Processing

# In[3]:

#Exploring the dataset for available columns and type of data
titanic.head(10)


# While the field Embarked, Survived and Pclass hold abbreviations for the port of embarkation, survival indicator and travel class, having descriptive names of the same look more meaningful especially in visulaizations.
# 
# Note that the port names were taken from the [Kaggle](https://www.kaggle.com/c/titanic/data) website.

# In[4]:

ports = ["Cherbourg", "Queenstown", "Southampton"]
survival = ["Dead", "Survived"]
travelclass = ["First Class", "Second Class", "Third Class"]


# In[5]:

# Creating descriptive labels
# Survival label
titanic['Survival'] = titanic.Survived.map({0 : survival[0], 1 : survival[1]})

# Ports label
titanic['Ports'] = titanic.Embarked.map({"C" : ports[0], "Q" : ports[1], "S" : ports[2]})

# Travel class label
titanic['TravelClass'] = titanic.Pclass.map({1 : travelclass[0], 2 : travelclass[1], 3 : travelclass[2]})


# In[6]:

#Making sure the Embarked field has been updated
titanic.head()


# In[7]:

#Taking a look at the basic stats
titanic.describe()


# ### How many people were on the ship and how many survived?
# 
# There were 891 passengers on Titanic and of them only 342 survived with an overall survival rate of 38%.

# In[8]:

#Get some basic counts and stats

totalpassengers = len(set(titanic["PassengerId"]))
survived = sum(titanic["Survived"])
overallsurvivalrate = format((survived/float(totalpassengers)) * 100, '0.2f')

print "Total Passengers on Titanic", totalpassengers
print "Passengers Survived", survived
print "Overall Survival Rate", overallsurvivalrate,"%"


# ### How has the travel class on the ship and the gender of passengers affect the survival rate?
# 
# From the bar plot below, it is evident that women in the 1st class had the highest survival rate at 10% followed by women in 2nd and 3rd classes at around 8% each. While the survival rate of men in 1st and 3rd class was around 5%, men in 2nd class seem to have the lowest survival rate.

# In[9]:

#Builds a bar plot with gender and travel class on the x-axis; number of people survived on the y-axis and survival rate in %
genderplt = sns.barplot(x = "Sex", y = "Survived", hue = "TravelClass", hue_order= travelclass,                         data = titanic, estimator = np.sum, ci = None)
genderplt.set(ylabel = "People Survived", xlabel = "Gender")
for p in genderplt.patches:
    height = p.get_height()
    genderplt.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height * 100)/totalpassengers),
            ha="center") 
genderplt.get_axes().legend(title = "Travel Class")
genderplt.set(title = "Survival Rate across Gender and Travel Class")


# The plot below gives a better picture of the same. While the deaths in the first and second class were contained, third class seems to be the worst affected for both men and women.

# In[10]:

#Builds a countplot split on travel class
factorplt = sns.factorplot(x="Sex", hue="Survival", col="Pclass", data=titanic, kind="count")

factorplt.set(ylabel = "Number of People", xlabel = "Gender")

titles = travelclass

for ax, title in zip(factorplt.axes.flat, titles):
    ax.set_title(title)
    
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height + 3,
                '{:1.2f}'.format((height * 100)/totalpassengers),
                ha="center") 

    


# The travel class has had a huge impact on the survival of passengers on the Titanic, with people travelling by 1st and 2nd class having a higher probability of survival and within those classes, women having a better chance of surviving over men.

# ### How has the age of passengers affected the survival rate?
# 
# There are a lot of instances where Age is either missing values or have fractionals in them. For this particular analysis, missing ages have been filled with 0 and the fractinals have been rounded. 
# 

# In[11]:

titanic['Age'].unique()


# In[12]:

titanic['Age'].isnull().sum()


# In[13]:

# A function to clean up the age field
def cleanup(df, field, convtoint):
    
    #Check if there are any missing values (Nan and make them 0
    df[field].fillna(value = 0, inplace = True)
    
    #Check if it needs to be converted to int
    if convtoint == 1:
        df[field] = df[field].astype(int)
    
    #Round the values
    df[field].round(0)
        
    return field + " has been cleaned up"


# In[14]:

cleanup(titanic, "Age", 1)


# In[15]:

average_age_titanic    =titanic['Age'].mean()
std_age_titanic        =titanic['Age'].std()

print average_age_titanic
print std_age_titanic


# In the initial phase of analysis, filling the missing ages with 0, skewed the distribution graphs to the left and since 0 is not a valid age for those passengers and is just missing, Age 0 has been excluded from the analysis. 
# 
# Although age 0 has been excluded for the purposes of this analysis, predictions or standardizing ages of those passengers could also be made to improve the accuracy of the charts.

# In[16]:

average_age_titanic    =titanic[titanic.Age > 0]['Age'].mean()
std_age_titanic        =titanic[titanic.Age > 0]['Age'].std()

print average_age_titanic
print std_age_titanic


# In[17]:

#Builds a age distribution plot
agedist = sns.distplot(titanic[titanic.Age > 0]['Age'])
agedist.set_xlim(0, max(titanic[titanic.Age > 0]['Age'])+10)
agedist.set_title("Age distribution")
agedist.set_ylabel("Age")
agedist.set_ylabel("Density of population")


# In[18]:

#Builds a plot on age and survival
ageplt = titanic.groupby(['Survival', 'Age']).count().unstack('Survival')["PassengerId"]
ageplt[1:].plot(kind='bar', stacked=True, title = "Number of passengers over Age")
pyplt.ylabel("Number of passengers")
pyplt.xlabel("Age")


# From the above visualization, it can be noted that the highest population of passengers is of the age group 16-40 and the least survival rate of passengers is of the age group 18-30.

# ### What effect did the fare paid have on survival rate?
# 
# As it is very noticeable from the Y-axis of the visualizations below, 1st class had fares upto a little more than 500 and it looks like only 2 passengers paid more than 500. What is interesting though is that a big majority of passengers in 1st class have paid less than 100 and on an verage people who have paid more have survived. 
# 
# While in second and third classes, majority of passengers have paid fares below 30 and 20 respectively. 
# 
# On an average, older people have paid lesser fares in all the classes alike and the chances of survival also decreases as the age of passenger increases. 
# 
# Please note that the visualizations do not include passengers is age has missing values or is 0.

# In[19]:

#Builds a linear relationship between age and fare over survival 
fareplt = sns.lmplot(x="Age", y="Fare", hue = 'Survival', col="Pclass", data=titanic[titanic.Age>0], sharey = False)
fareplt.set(ylabel = "Fare", xlabel = "Age")
fareplt.axes[0,0].set_ylim(0,)
fareplt.axes[0,1].set_ylim(0,)
fareplt.axes[0,2].set_ylim(0,)
fareplt.axes[0,0].set_xlim(0,)
fareplt.axes[0,1].set_xlim(0,)
fareplt.axes[0,2].set_xlim(0,)
titles = travelclass

for ax, title in zip(fareplt.axes.flat, titles):
    ax.set_title(title)


# ### What role has the port of embarakation played?
# 
# While Southampton had the most number of passengers, it also had the least survival rate. This is probably because Southampton also had the most number of passengers in 3rd class. It can be concluded that Southampton is a really busy port.
# Queenstown probably is the least popular port with minimal passengers, especially among 1st and 2nd travel classes. 

# In[20]:

emb = titanic.groupby(['Survival', 'Ports','TravelClass']).count().unstack('Ports')['PassengerId']
emb.head(6)


# In[21]:

#Builds a bar plot betwen embarkation port and passengers survived over travel class
portplt = sns.barplot(x = "Ports", y = "Survived", hue = "TravelClass", hue_order = travelclass, data = titanic, estimator = np.sum, ci = None)
portplt.set(ylabel = "People Survived", xlabel = "Embarkation Area")
portplt.set(title = "Number of people that survived across travel class")


# In[22]:

emb = titanic.groupby(['Survival', 'Ports']).count().unstack('Ports')['PassengerId']
emb = emb/emb.sum()*100
emb.head()


# In[23]:

#Builds a function that builds a pie plot on survival/death rate
def plotpie(series):
    
    i = 2
    for c in list(series):
        pyplt.figure(i, figsize = (4,2))
        pyplt.pie(emb[c], labels=survival, colors=['red', 'green'], autopct='%1.1f%%',                   shadow=True, startangle=90)
        # View the plot drop above
        pyplt.axis('equal')
        pyplt.title("Survival Rate at " + c)

        
        i+= 1
        


# In[24]:

#To build pie plots at different embarkation ports
plotpie(emb[["Cherbourg", "Queenstown", "Southampton"]])


# ### Conclusion 
# 
# The features below were analyzed in this analysis:
# 
# * Gender
# * Travel Class
# * Age
# * Fare
# * Port of Embarkation
# 
# The most evident findings in this analysis are that: 
# 
# * passengers in the upper class had a better chance of surviving than the passengers in lower class
# * women had a better chance of surviving over men
# * passengers with ages between 18 and 30 were more and also had a very poor survival rate
# * Southamptopn port seemed busier and popular with more number of passengers and Queenstown port the least with very few passengers especially in first and second classes
# 
# ### Limitations
# 
# Some limitations of this analysis include the dataset and the missing values in Age and Cabin. This dataset contains details about less than half the passengers on Titanic within which age and cabin have more than 170 and 650 missing values respectively. 
# 
# Filling the missing values of age with 0 results in skewing the visualizations to the left and so, this analysis excludes the records with age missing or 0. 
# 
# Cabin also could be a strong indicator of survival as some survival boats could have been more accessible from some of the cabin areas and some might have very little or late access.
# 
# The precision of this analysis could be improved with more information on these fields and with a larger dataset. 

# ### References
# 
# 1. [Kaggle](https://www.kaggle.com/c/titanic)
# 2. [Seaborn](http://seaborn.pydata.org/tutorial.html)
# 3. [Matplotlib](http://matplotlib.org/)
# 4. [Pandas](http://pandas.pydata.org/)
