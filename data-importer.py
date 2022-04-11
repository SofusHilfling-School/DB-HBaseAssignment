import happybase
import pandas

connection = happybase.Connection('localhost', port=9090)

tables = connection.tables()
print('tables: ', tables)

if b'foods' not in tables:
    connection.create_table('foods', {'facts': dict()})

food_table = connection.table('foods')

food_data = pandas.read_excel('./Data/Food_Display_Table.xlsx')
columns = food_data.columns
print(columns)

for index, row in food_data.iterrows():
    row_key = row[columns[0]]
    food_table.put(str(row_key), { 'facts:' + col: str(row[col]) for col in columns[1:] })
    