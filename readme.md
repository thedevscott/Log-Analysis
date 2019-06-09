# Project Description
# Scenario

You've been hired onto a team working on a newspaper site. The user-facing 
newspaper site frontend itself, and the database behind it, are already built 
and running. You've been asked to build an internal reporting tool that will 
use information from the database to discover what kind of articles the site's 
readers like.

The database contains newspaper articles, as well as the web server log for the 
site. The log has a database row for each time a reader loaded a web page. 
Using that information, your code will answer questions about the site's user 
activity.

The program you write in this project will run from the command line. It won't 
take any input from the user. Instead, it will connect to that database, use 
SQL queries to analyze the log data, and print out the answers to some 
questions.

## Why this project?

In this project, you will stretch your SQL database skills. You will get 
practice interacting with a live database both from the command line and from 
your code. You will explore a large database with over a million rows. And you 
will build and refine complex queries and use them to draw business 
conclusions from data.

### Report generation

Building an informative summary from logs is a real task that comes up very 
often in software engineering. For instance, at Udacity we collect logs to 
help us measure student progress and the success of our courses. The reporting 
tools we use to analyze those logs involve hundreds of lines of SQL.

### Database as shared resource

In this project, you'll work with data that could have come from a real-world 

web application, with fields representing information that a web server would 
record, such as HTTP status codes and URL paths. The web server and the 
reporting tool both connect to the same database, allowing information to flow 
from the web server into the report.

This shows one of the valuable roles of a database server in a real-world 
application: it's a point where different pieces of software (a web app and a 
reporting tool, for instance) can share data.

```SQL
SELECT event_day AS period,
    SUM(current_paid_students) AS "Paid Students",
    SUM(current_trial_students) AS "Free Students"
FROM analytics_tables.paid_enrollemnt
WHERE ("course_key" = {NANODEGREE})
    AND current_trial_students > 0
GROUP BY period
ORDER BY period ASC;
```
The above SQL is just one of many queries Udacity uses for log analysis

### The PostgreSQL documentation

In this project, you'll be using a PostgreSQL database. If you'd like to know 
a lot more about the kinds of queries that you can use in this dialect of SQL, 
check out the PostgreSQL documentation. It's a lot of detail, but it spells out 
all the many things the database can do.

Here are some parts that may be particularly useful to refer to:
* [The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
* [SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
* [Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)

# Setting Up
### Requirements

The following must be installed to correctly execute the analysis script:

* [Python 3.5.2](https://www.python.org/downloads/)
* [psycopg2 2.8.2](http://initd.org/psycopg/docs/install.html#binary-install-from-pypi)
* [psql (PostgreSQL) 9.5.17](https://www.postgresql.org/download/linux/ubuntu/) 
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

### Instructions

Once the above requirements are met do the following:
* Download the Virtual Machine (VM) configuration:
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
This will give you a directory called FSND-Virtual-Machine. It may be located 
inside your Downloads folder.

Note: If you are using Windows OS you will find a Time Out error, to fix it use 
the new [Vagrant file configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip)
to replace you current Vagrant file.

Alternately, you can use Github to fork and clone the repository 
https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. 
Change to this directory in your terminal with *cd*. Inside, you will find 
another directory called **vagrant**. Change directory to the **vagrant** 
directory:

* Startup & Connect to the virtual Machine (VM) by doing the following:
From your terminal, inside the vagrant subdirectory, run the command 
```shell 
vagrant up
```
This will cause Vagrant to download the Linux operating system and install 
it. This may take quite a while (many minutes) depending on how fast your 
Internet connection is.

When 
```shell 
vagrant up
```
is finished running, you will get your shell prompt 
back. At this point, you can run 
```shell 
vagrant ssh
```
 to log in to your newly installed Linux VM!

* Populate the database after installing PostgreSQL
```shell
psql -d news -f newsdata.sql
```

* Connect to the database
```shell
psql -d news
```
**NOTE:** To disconnect and get back to the linux prompt use *Ctrl+D* or *\q* 
from the 
psql prompt

* Run the Python Script
```python
python log_analysis.py
```
The output should be similiar to what is found in *log_analysis_output.txt*

# The Task

Your task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers 
given aren't the right ones, though!

**1. What are the most popular three articles of all time?** Which articles 
have 
been accessed the most? Present this information as a sorted list with the most 
popular article at the top.

**Example:**

* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

**2. Who are the most popular article authors of all time?** That is, when you 
sum up all of the articles each author has written, which authors get the most 
page views? Present this as a sorted list with the most popular author at the 
top.

**Example:**

* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views

**3. On which days did more than 1% of requests lead to errors?** The log table 
includes a column status that indicates the HTTP status code that the news site 
sent to the user's browser. (Refer to this lesson for more information about 
the idea of HTTP status codes.)

**Example:**

* July 29, 2016 — 2.5% errors

# Good coding practices
## SQL style

Each one of these questions can be answered with a single database query. Your 
code should get the database to do the heavy lifting by using joins, 
aggregations, and the where clause to extract just the information you need, 
doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. 
You are allowed and encouraged to do this! However, if you create views, make 
sure to put the create view commands you used into your lab's README file so 
your reviewer will know how to recreate them.

## Python code quality

Your code should be written with good Python style. 
The [PEP8 style](https://www.python.org/dev/peps/pep-0008/) guide is an 
excellent standard to follow. You can do a quick check using the pep8 
command-line tool.

# Project Rubric
 
## Functionality

Running the code displays the correct answers to each of the questions in the 
project description.

## Compatibility: Database

The code works with the (unchanged) database schema from the project 
description.
It is OK to add views to the database, but don't modify or rename the existing 
tables.

## Compatibility: Language

The code may be written in Python 2 or Python 3 but must be consistent. It 
should start with a correct shebang line to indicate the Python version.

## Well-formatted text output

The code presents its output in clearly formatted plain text. Imagine that you 
are looking at this text in an email message, not on a web page.

## Database queries

The code connects to and queries an SQL database. It does not use answers 
hardcoded into the application code.

## Code Quality

## No errors

The project code runs without any error messages or warnings from the language 
interpreter.

## Application code style

The code conforms to the PEP8 style recommendations.
You can install the *pycodestyle* tool to test this, with 
```shell
pip install pycodestyle 
```
or 
```shell
pip3 install pycodestyle (Python 3)
```
In order for this requirement to pass, running the *pycodestyle* tool on your 
code should produce zero warnings.

(*pycodestyle* was formerly known as *pep8*. These are the same thing.)

## SQL code quality

When the application fetches data from multiple tables, it uses a single query 
with a join, rather than multiple queries. Each of the questions must be 
answered using one SQL query.

## README File

## README file describes work

The README file includes instructions for how to run the program, as well as a 
description of the program's design.

Imagine a person who knows Python and SQL well, but has not done this project. 
If that person read the README would they know how to run this code?

## README file includes view definitions, if any

If the code relies on views created in the database, the README file includes 
the *create view* statements for these views.
(If the code does not depend on views, ignore this requirement.)

## Authors

* **Omar Scott** - *Initial Work*

## Acknowledgments

* Many thanks to the [Udacity Full Stack Web Developer](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
team for their excellent instruction, much of which was used to complete this
 project. 
