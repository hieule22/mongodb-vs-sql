# MongoDB vs. SQL

## About

This project benchmarks search queries for MongoDB and MySQL for data of various
sizes in the presence - or lack thereof - of indexes.

## Content

* [`CONFERENCE_REVIEW.sql`](CONFERENCE_REVIEW.sql) contains the MySQL queries to
define our tables. Only tables relevant to this project are included in order to
expedite the creation process. In addition, I have temporarily commented out all
primary key / foreign key constraints so data could be rapidly inserted and the
tables are free of any initial index (MySQL automatically defines indexes on
key fields).

* [`DataGenerator.py`](DataGenerator.py) is the Python script used to generate
data for authors, papers, and authorships - the association between an author
and the paper he or she writes. The generated data will be output to CSV and
JSON files stored in [`genfiles`](genfiles/). Update the values of `NUM_AUTHORS`
and `NUM_PAPERS` to change the number of rows generated.

* [`genfiles`](genfiles/) stores the generated data files used to populate our
databases. JSON files are used to populate MongoDB database while CSV files are
used to populate MySQL databases. Please keep all generated data files local
since they could get rapidly large when more rows are inserted.

* [`data`](data/) contains input files taken from several sources to generate
test data for this project.

* [`MongoDBDataLoader.sh`](MongoDBDataLoader.sh) is the bash script to import
generated data to actual MongoDB collections.

* [`MySQLDataLoader.sql`](MySQLDataLoader.sql) contains the SQL commands to
import generated data to actual MySQL collections.

* [`SearchQueries.sql`](SearchQueries.sql) contains the SQL search queries for
our use cases.

## Instalation

### Requirements

* Linux/MacOS

* MongoDB

* MySQL

* Python3

### Steps

Here are the approximate steps to get everything working. There might be
variances between different operating systems so please tweak them to meet
your needs. Use the judgement of the brilliant programmer that you are :)
Reach out to me if you have problems with any of these steps.

* Create the MySQL database `CONFERENCE_REVIEW` and its constituent tables -
MySQL server must be running

```bash
mysql -u root -p < CONFERENCE_REVIEW.sql
```

* Generate test data with a specified number of rows

```bash
python DataGenerator.py <number of rows>
```

* Import test data to MySQL tables

```bash
mysql -u root -p < MySQLDataLoader.sql
```

* Import test data to MongoDB collections -- MongoDB server must be running
```bash
chmod +x MongoDBDataLoader.sh  # Do this once to make script executable
./MongoDBDataLoader.sql
```

* Connect to MySQL and MongoDB clients and execute the search queries



