#!/bin/sh

echo "Removing existing data from paper collection"
mongo test --eval "db.paper.remove({})"

echo "Importing data from file to paper collection"
mongoimport --db test --collection paper --file ../genfiles/papers.json

echo "Removing existing data from author collection"
mongo test --eval "db.author.remove({})"

echo "Importing data from file to author collection"
mongoimport --db test --collection author --file ../genfiles/authors.json
