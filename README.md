# ECE444-F2020-Lab3
# Sophia Ryoo
# this repo is a clone of https://github.com/miguelgrinberg/flasky.

## Activity 1
![Activity 1](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity1.png?raw=true)

## Activity 2
#### First page with name and email
![First Page with Name and Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_1.png?raw=true)

#### Valid first name and email
![Valid First Name and Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_2.png?raw=true)

#### Invalid email without @ sign
![Invalid Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_3.png?raw=true)

#### Non-UofT email
![Non-UofT Email](https://github.com/honeyjoo/ECE444-F2020-Lab3/blob/master/activity2_4.png?raw=true)

## Activity 3
SQL databases are relational databases, and relations are stored in tables called relations. These databases use SQL for queries, and you need to define a schema(fixed number of columns) for a pre-determined structure before running queries although the number of rows is flexible. Tables have primary keys which are like a unique identifier for each row, and the foreign keys that are the reference of primary key that corresponds to a row in another table, thereby named relational databases. The pros of SQL database is that you can manage complex queries and that SQl DB is more efficient and compact in regard to storing structured data, yet the con is the users are restricted by schemas. They are vertically scalable, meaning you can add virtual or physical resources to the server that hosts the DB.

NoSQL databases don't follow the relational model - it does not need fixed schemas but can use dynamic schema such as collections and documents, instead of tables and rows in SQL DB. The pros of NOSQL DB is that they have duplicated data which allows faster querying, and listing users and their roles is straightforward because no joins are needed. The cons is that joins are dificult and renaming a role is expensive. NoSQL DB is horizontally scalable, meaning you need to add servers to increase traffic. This makes NoSQl DB used in storing distributed data when one needs a large storage.
