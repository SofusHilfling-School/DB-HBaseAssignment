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
