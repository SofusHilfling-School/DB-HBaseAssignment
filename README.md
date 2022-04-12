# DB-HBaseAssignment



TODO list:
- [ ] Find and explain alternative column family options that would make sense for this data.
- [ ] Argument for why we use food code as our row key.
- [ ] Show diffrent ways of querying the database with the HBase shell.
- [x] Create data import script.
- [x] Create docker compose file for running HBase.
- [x] Write how to run section.

# How to run
## Starting the hbase server with docker
Run the following commands:
```
$ docker compose up -d
$ python ./data-importer.py
```
## Entering the hbase shell with docker compose
```
docker-compose exec hbase-master hbase shell
```

# Assignment questions
## Argument your choice of row key
Standard row key, as we only have a single node which is used to a single column family to store
the facts about the food in the data sheet. We could've customized a row key, but there's simply
no need for it in this scenario.

## Sugggest some alternative column family options
A lot of the column family options that exist are simply just specific data about the given foods.
It is all the information given when you buy a food product in a super market for example.
However we could group the data in families that would make sense, for example like this:
* **Food_Info** - Food_Code, Display_Name
* **Portion_Info** - Portion_Default, Portion_Amount, Portion_Display_Name, Factor, Increment, Multiplier
* **Ingredient_Info** - Grains, Whole_Grain, Vegetables, Orange_Vegetables, Drkgreen_Vegetables, Starchy_vegetables,
                        Other_Vegetables, Fruits, Milk, Meats, Soy, Drybeans_Peas, Oils
* **Macronutrions_Info** - Solid_Fats, Added_Sugar, Alcohol, Calories, Saturated_Fats

## Querying to HBase
### Get command
To retrieve data/get data from HBASE Shell, you can use the command **'get'**.
The get command has 2 arguments, the first being column family, and the second is the key of the item.

For example, if we choose to get the info of the first item; *Sour Cream dip* with the food_code (the key); 12350000
the input would look like this:
```
get 'foods', '12350000'
```
to which the output will be:
```
COLUMN                                  CELL
 facts:Added_Sugars                     timestamp=1649767080819, value=1.57001
 facts:Alcohol                          timestamp=1649767080819, value=0.0
 facts:Calories                         timestamp=1649767080819, value=133.65
 facts:Display_Name                     timestamp=1649767080819, value=Sour cream dip
 facts:Drkgreen_Vegetables              timestamp=1649767080819, value=0.0
 facts:Drybeans_Peas                    timestamp=1649767080819, value=0.0
 facts:Factor                           timestamp=1649767080819, value=0.25
 facts:Fruits                           timestamp=1649767080819, value=0.0
 facts:Grains                           timestamp=1649767080819, value=0.04799
 facts:Increment                        timestamp=1649767080819, value=0.25
 facts:Meats                            timestamp=1649767080819, value=0.0
 facts:Milk                             timestamp=1649767080819, value=0.0
 facts:Multiplier                       timestamp=1649767080819, value=1.0
 facts:Oils                             timestamp=1649767080819, value=0.0
 facts:Orange_Vegetables                timestamp=1649767080819, value=0.0
 facts:Other_Vegetables                 timestamp=1649767080819, value=0.0407
 facts:Portion_Amount                   timestamp=1649767080819, value=0.25
 facts:Portion_Default                  timestamp=1649767080819, value=1
 facts:Portion_Display_Name             timestamp=1649767080819, value=cup
 facts:Saturated_Fats                   timestamp=1649767080819, value=7.36898
 facts:Solid_Fats                       timestamp=1649767080819, value=105.6485
 facts:Soy                              timestamp=1649767080819, value=0.0
 facts:Starchy_vegetables               timestamp=1649767080819, value=0.0
 facts:Vegetables                       timestamp=1649767080819, value=0.0407
 facts:Whole_Grains                     timestamp=1649767080819, value=0.0
1 row(s)
```

We can then chose to retrieve a specific column, to which we can add another argument:
```
get 'foods', '12350000', {COLUMN => ['facts:Calories']}
```
This specifies that we would only like to retrieve the Calorie value of the item.
The output is as follows:
```
COLUMN                                  CELL
 facts:Calories                         timestamp=1649767080819, value=133.65
1 row(s)
```

### Scan command
The **'scan'*** command Scans and returns all of the table data.
If we simply use scan on a column family, it will return all of the data, which would look like this.
```
scan 'foods', '12350000'
...
 94210100                               column=facts:Whole_Grains, timestamp=1649767082830, value=0.0
1013 row(s)
Took 10.4124 seconds
```
This is of course not all of the data, as the query took 10,4 seconds to fulfill.
However, we can filter with scans and put limits on it:
```
scan 'foods', '12350000', { FILTER => “FirstKeyOnlyFilter()”}
```
