
## OpenStreetMap Data Case Study

### Map Area
#### [Bengaluru, Karnataka, India](https://www.openstreetmap.org/search?query=bengaluru#map=12/12.9719/77.5937)

As a kid, I lived close to Bengaluru in India and have been away for more than 10 years now. I want to take this opportunity to explore how the city has grown and also contribute by cleaning up the data in Open Street Map and provide some insights on the 'Garden City', Bengaluru.


### Problems encountered in the map

Applying the code from the case study worked on earlier for Data Wrangling, I wrote a subset of data to csv and SQL relational tables. I used SQL queries to explore the data and problem areas. 

Below are some of the problems I encountered:

* Street names with the entire address  
    *Ex: Survey 5/2, Whitefield Main Rd, SH 35, Sathya Sai Layout, Whitefield, Sathya Sai Layout, Whitefield, Bengaluru, India*
* Area names in the city field  
    *Ex: K.R Puram*
* Inconsistent and multiple phone numbers with different formats   
    *Ex: +918022382894/96*
* Incorrect postal codes  
    *Ex: 600005


### Resolving those problems

###### Street names
As the city, state, country or postal code doesn't belong in the street field, all those names have been removed from the street field so that it contains details about the street address alone. 

Using the above example, the cleaned street field would contain - *Survey 5/2, Whitefield Main Rd, SH 35, Sathya Sai Layout, Whitefield, Sathya Sai Layout, Whitefield*

Besides street names, house number field also had details on street address in the data set. However, I noticed that in those cases, those particular details were missing from the street field. To maintain data integrity and continuity, they were left untouched.

All the abbreviations in the street fields have been mapped to their corresponding full forms as well.

###### City
The name of the city has officially changed to Bengaluru. Due to this there is a nice mix of both the old and the new name in the city field. However, looking at the numbers, 'Bangalore' stood out as the clear winner and hence I've continued to use the same in my process.

I've also noticed that an area or a locality's name gets used in that field as the city. In most cases, since this doesn't exist on the street name, I've continued to use the area name and appended the city name to it. 

Using the above example, the cleaned city name would be - *K.R Puram, Bangalore*

###### Phone numbers
Out of all the fields explored, phone numbers was the most inconsistent both in terms of format and listing multiple phone numbers. Different kinds of characters (/.,&) were used to separate each phone number. 

I've used the standard below while cleaning up this field

* Fixed lines - +91-80-xxxx xxxx
* Mobile/Cell - +91-xxxxxxxxxx

Multiple phone numbers will be listed as comma separated values in phone number field.

Using the above example, the cleaned phone number field would contain - *+91-80-2238 2894, +91-80-2238 2896*

###### Postal Code
While there were only two formats in the postal code field, what I found interesting later on was that there were valid postal codes that do not belong to Bangalore. I cleaned them up as well so that only valid postal codes for Bangalore city would get populated.


### Overview of the data

This provides some statistics of the data, right from the size of the raw XML data set to the finished tables and dives into the data to explore some basic data distribution and statistics.

##### File Sizes


```
Bangalore OSM - 614MB
nodes.csv - 231MB
nodes_tags.csv - 3.16MB
ways.csv - 38.7MB
ways_nodes.csv - 84.6MB
ways_tags.csv - 22.8MB
```

##### Number of Unique Users

There are 1855 unique users in nodes and ways. 

```SQL
select count(distinct [user]) AS Users
from (
select [user]
from [Udacity].[dbo].nodes
union 
select [user]
from [Udacity].[dbo].ways)u
```

|Users
|--- 
|1855

##### Number of Unique Users who contributed towards tags

Out of which, 1700 have contributed towards node and way tags.

```SQL
select count(distinct [user]) AS Users
from (
select [user]
from [Udacity].[dbo].nodes n inner join
dbo.nodes_tags nt on n.id = nt.id
UNION 
select [user]
from [Udacity].[dbo].ways w inner join
dbo.ways_tags wt on w.id = wt.id)u
```

|Users
|---
|1700

##### Contributor Statistics

It looks like the top 10 contributors account for only about 30% of the total contributions. That shows how diverse the contributions are from varios users. 

```SQL
select count(distinct id) AS Contributions, [user]
from (
select nt.id, [user]
from dbo.nodes n inner join
dbo.nodes_tags nt on n.id = nt.id
UNION 
select wt.id, [user]
from dbo.ways w inner join
dbo.ways_tags wt on w.id = wt.id)u
group by [user] with rollup
order by Contributions DESC 
```

Contributions |	User
--- | ---
684838 | NULL
24351 | premkumar
23890 | jasvinderkaur
23451 | akhilsai
23046 | saikumar
20588 | vamshikrishna
19569 | shekarn
17434 | himalay
17334 | PlaneMad
17276 | hareesh11
17221 | himabindhu

##### User Distribution (Top 10)

This shows the top 10 areas in which most number of users have contributed towards in descending order.

```SQL
select TOP 10 count(distinct [user]) AS Users, Value AS Postalcode
from (
select [user],value
from dbo.nodes n 
inner join dbo.nodes_tags nt on n.id = nt.id
where nt.[key] = 'postcode'
UNION 
select [user],value
from [Udacity].[dbo].ways w 
inner join dbo.ways_tags wt on w.id = wt.id
where wt.[key] = 'postcode')u
group by Value 
order by Users DESC
  
```

Users |	Postalcode
--- | ---
56  |560037
45  |560076
42  |560066
42	|560102
42	|560001
40	|560068
40	|560095
38	|560038
38	|560043
38	|560078


##### Number of Nodes

```SQL
select count(*) AS Nodes from dbo.nodes
```

|Nodes
|---
|2864255


##### Number of Ways

```SQL
select count(*) AS Ways from dbo.ways
```

|Ways
|---
|656294


##### Most contributed to areas

```SQL
select tags.value, count(*) as count 
from (select * FROM nodes_tags UNION ALL 
      select * FROM ways_tags) tags
where tags.[key] = 'city'
group by tags.value
order by count DESC
```

Area | Count
--- | ---
Banashankari,Bangalore | 29
Marathahalli, Bangalore | 29
Whitefield, Bangalore |20
Whitefield,Bangalore|17
Basaveshwara Nagar, Bangalore|17
Gandhi Nagar, Bangalore |15
Hoodi, Mahadevapura, Bangalore |10
Koramangala, Bangalore | 10
Mathikere, Bangalore | 9
Mahadevapura, Bangalore |9
Indira Nagar, Bangalore |8

##### Walkability

By looking at the number of sidewalks available, I wanted to see how walk friendly the city is. Below are some statistics grouped on the sides on which the walk ways are available on.

```SQL
select count(distinct  id) AS Sidewalks, value AS Value from dbo.ways_tags 
where  [key] = 'sidewalk' and value != 'none' and value != 'no' 
group by value
order by Sidewalks DESC
```


|Sidewalks |	Value|
| -------- | ------- |
|       117|both     |
|        76|left     |
|        26|right    |
|         5|separate |

Given the size of the city, I believe the number of walk ways could be improved.

##### Bike lanes

I was surprised to find tags for bike lanes and I had to pull some statistics for this as well. Unsurprisingly, there are very few bike lanes in the city and a lot could be improved.

```SQL
select  count(*) as Bikelanes, value 
from (
select * from dbo.nodes_tags
where [KEY] = 'cycleway'
UNION
select * from dbo.ways_tags
where [KEY] = 'cycleway'
)b
group by value
order by Bikelanes desc
```

Bikelanes |	value
----- | ----
437 |	no
21	| lane
10	| shared_lane
1	| track

##### Top 10 Amenities

Below are the top 10 amenities in the nodes and ways for the city of Bangalore. It is no surprise that restaurants top the list of amenities in the city. 

```SQL
SELECT  top 10 COUNT(*) as count, value 
from (
select * from dbo.nodes_tags
where [KEY] = 'amenity'
UNION
select * from dbo.ways_tags
where [KEY] = 'amenity'
)q
group by value
order by count desc
```


Count |	Value
---- | ---
1665  |	restaurant
1040  |	place_of_worship
773 |	atm
732	| bank
691	| school
571	| hospital
521	| pharmacy
491	| fast_food
350	| cafe
317	| fuel

##### Health & Security


```SQL
select count(*) as num,value from (
select nt2.value from dbo.nodes_tags nt1
inner join dbo.nodes_tags nt2 on nt1.id=nt2.id
where nt1.value IN ('police', 'hospital') and nt2.[key] = 'amenity'
UNION ALL
select wt2.value from dbo.ways_tags wt1
inner join dbo.ways_tags wt2 on wt1.id = wt2.id
where wt1. value IN ('police', 'hospital') and wt2.[key] = 'amenity'
)q
group by value
order by num DESC
```

count |	value
--- | ---
580 | hospital
111	| police

It is also a good idea to find out how the police stations and hospitals are distributed around the city. 

##### Leisure

Lastly, since Bangalore gets tagged as the 'Garden city', I wanted to look at the number of parks and gardens available in the city.

```SQL
SELECT  top 10 count(*) as count, value 
from (
select * from dbo.nodes_tags
where [KEY] = 'leisure'
UNION
select * from dbo.ways_tags
where [KEY] = 'leisure'
)q
group by value
order by count desc
```

count |	value
--- | ---
729	| park
282	| sports_centre
275	| pitch
157	| playground
131	| garden
80	| swimming_pool
49	| common
23	| fitness_centre
18	| track
18	| stadium

As you can see, there are a lot of leisure activities and parks top the list. I also looked for any references to trees in the dataset and just found two instances in nodes_tages where trees where referred to but I have to conclude that the information at this point is inadequate. 

### Additional Ideas

There is still a lot that could be done statistically by looking at different levels of data in the nodes and ways. Below are some of the ideas that I had but didn't want to elaborate as the answers to these questions have no element of surprise with this data set (although these might be useful for other cities). 

* Different cuisines of restaurants could be explored. In the case of Bangalore, the most prevalent cuisine is still different Indian cuisines and the rest lag way behind them. 

* Different religions and their places of worship.

* Amenities were not included in the data analysis and I noticed that most of the amenities like restaurants and their cuisines, cafes could use some clean up from what I noticed.

Below is a sample SQL query that could be used to get to the above questions simply by swapping the 'value' and 'key' in the query.

```SQL
select count(*) as num, Value from (
select nt2.value from dbo.nodes_tags nt1
inner join dbo.nodes_tags nt2 on nt1.id=nt2.id
where nt1.value = 'place_of_worship' and nt2.[key] = 'religion'
UNION ALL
select wt2.value from dbo.ways_tags wt1
inner join dbo.ways_tags wt2 on wt1.id = wt2.id
where wt1. value = 'place_of_worship' and wt2.[key] = 'religion'
)q
group by value
order by num DESC
```

* The distribution of schools, hospitals and police stations in the city could be analyzed to provide some insights on how accessible education, health and security is in the city.

Below is a sample query and resultset that provides distance from the city center.

```SQL
--POINT(12.9716 77.5946) Bangalore city center taken from Google 
DECLARE @citycenter geography = 'POINT(12.9716 77.5946)'
select distinct n.id, round(@citycenter.STDistance('POINT('+lat+' '+ lon+')')/1000,2) AS 'Distance from the city center(in kms)' from dbo.nodes_tags nt
inner join dbo.nodes n on nt.id = n.id 
where  nt.value like '%police%'
order by [Distance from the city center(in kms)] ASC
```

id	|  Distance from the city center(in kms)
--- | ---
263155937	| 0.25
4489908738	| 0.31
660666061	| 0.32
2577231853	| 0.35
428843493	| 0.43

* I also noticed that the accuracy of some of the data is questionable and an option for users to 'Report a Problem' which would inactivate a particular tag for example would make the data more reliable and accurate.

In addition to benefits, these additional ideas could bring in some problems as well. Below are some benefits and anticipated problems by following these ideas, in my opinion.

##### Benefits

* The data would be more cleaner and readable

* Better and moer accurate analysis

##### Anticipated problems

* Cleaning the data of lesser known or recognized amenities like cafes or restaurants could be a challenge as their data cannot be verified easily

* 'Report a problem' feature or anything similar takes time to receive feedback and ultimately clean data

### Conclusion

After looking at data for the city of Bangalore, I believe it could use a lot more contributions from users. For the purposes of this exercise, I believe the data set has been cleaned. Although, I've added a few more ideas for cleaning and analyzing. Building up on these ideas will make for a more complete data cleanser, which will ultimately make the data on OpenStreetMap.org more accurate and readable for the city of Bangalore. 

While cleaning up the postal codes and phone numbers of the city, I used a national standard website as a resource to clean and standardize data. Such sources would work out to be more reliable and readable for users and could be used in cleaning up more of OpenStreetMap data.
