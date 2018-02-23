# Log-analysis-tool-python
### why this project?
This project develops a log analysis tool for generating report. Building an informative summary from logs is a real task that comes up very often in software engineering.The intended tool will analyze around 50,000 log entries using comple SQL queries. This tool is designed for a particular database but it will give an idea to write complex queries and use them to any databases.
### Technologies Used
* Python
* PostgreSQL
* vagrant
### Project Description
---
The log-tool should be able to answer the following questions:
##### 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
##### 2. Who are the most popular article authors of all time?
##### 3. On which days did more than 1% of requests lead to errors?
---
# Preparing the Data
## The virtual Machine
This project makes use of the same Linux-based virtual machine (VM).The virtual machine will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory.
If you need to bring the virtual machine back online (with `vagrant up`), do so now. Then log into it with `vagrant ssh`.
## Download The Data
Next, download the data [here](). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the `psql` command in this lesson.

To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

`psql` — the PostgreSQL command line program

`-d news` — connect to the database named news which has been set up for you

`-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
## Getting an error?

If this command gives an error message, such as 
``` postgreSQL
psql: FATAL: database "news" does not exist
psql: could not connect to server: Connection refused
```
this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.
# Creating The Views
``` sql
CREATE VIEW path_hits AS 
SELECT substr(log.path, 10) AS slughit,count(path) AS hits 
FROM log
GROUP BY path 
ORDER BY hits DESC; 
```
```sql
CREATE VIEW auth_slug_hit AS SELECT author,title, hits
FROM articles,path_hits 
WHERE articles.slug=path_hits.slughit;
```
```sql
CREATE VIEW error_table AS 
SELECT date(time), count(*) AS error_hits 
FROM log WHERE status='404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```
```sql
CREATE VIEW all_views AS 
SELECT date(time), count(*) AS views 
FROM log 
GROUP BY date(time) 
ORDER BY date(time);
```
