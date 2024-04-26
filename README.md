# README.md

In this project we are building an API using flask-smorest.

The database is populated by our scrapy spiders, Check the repo: <https://github.com/danielarroyave28/real_estate_webscraping_colombia>

We create the database from flask and use flask-migrate to track schema changes. Scrapy pipelines are modified according to the last updated schema
in order to insert the required values for each column without issues. FInally, with flask we develop an API to extract valuable information from this data
