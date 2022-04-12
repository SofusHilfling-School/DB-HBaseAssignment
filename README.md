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