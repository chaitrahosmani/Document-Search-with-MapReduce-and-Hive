# Document-Search-with-MapReduce-and-Hive
As we store clusters of document, it's tedious to get relavant documents when needed. This project aims to build a document search engine where one can find most relavent files based input of keywords.
Documents are also distributed in hadoop filesystem, hence I use map reduce to create TF-IDF for all the documents and store the results of TF-IDF into HIVE table.
The detail methodology is explained in the report
