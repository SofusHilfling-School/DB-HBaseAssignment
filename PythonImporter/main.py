import happybase

connection = happybase.Connection('localhost', port=16020, protocol="compact")

table = connection.table('foods')

table.put("rowkey", "data")