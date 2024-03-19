## Data Engineering Practice Problems

One of the main obstacles of Data Engineering is the large
and varied technical skills that can be required on a 
day-to-day basis.

This aim of this repository is to help us develop and 
learn those skills. Generally, here are the high level
topics that these practice problems will cover.

- Python data processing.
- csv, flat-file, parquet, json, etc.
- SQL database table design.
- Python + Postgres, data ingestion and retrieval.
- PySpark
- Data cleansing / dirty data.

### How to work on the problems.
We will need two things to work effectively on most all
of these problems. 
- `Docker`
- `docker-compose`

All the tools and technologies we will need be packaged
  into the `dockerfile` for each exercise.

For each exercise we will need to `cd` into that folder and
run the `docker build` command, that command will be listed in
the `README` for each exercise, follow those instructions.

### Beginner Exercises

#### Exercise 1 - Downloading files.
The [first exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-1) tests our ability to download a number of files
from an `HTTP` source and unzip them, storing them locally with `Python`.
`cd Exercises/Exercise-1` and see `README` in that location for instructions.

#### Exercise 2 - Web Scraping + Downloading + Pandas
The [second exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-2) 
tests our ability perform web scraping, build uris, download files, and use Pandas to
do some simple cumulative actions.
`cd Exercises/Exercise-2` and see `README` in that location for instructions.

#### Exercise 3 - Boto3 AWS + s3 + Python.
The [third exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-3) tests a few skills.
This time we will be using a popular `aws` package called `boto3` to try to perform a multi-step
actions to download some open source `s3` data files.
`cd Exercises/Exercise-3` and see `README` in that location for instructions.

#### Exercise 4 - Convert JSON to CSV + Ragged Directories.
The [fourth exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-4) 
focuses more file types `json` and `csv`, and working with them in `Python`.
We will have to traverse a ragged directory structure, finding any `json` files
and converting them to `csv`.

#### Exercise 5 - Data Modeling for Postgres + Python.
The [fifth exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-5) 
is going to be a little different than the rest. In this problem we will be given a number of
`csv` files. We must create a data model / schema to hold these data sets, including indexes,
then create all the tables inside `Postgres` by connecting to the database with `Python`.


### Intermediate Exercises

#### Exercise 6 - Ingestion and Aggregation with PySpark.
The [sixth exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-6) 
is going to step it up a little and move onto more popular tools. In this exercise we are going
to load some files using `PySpark` and then be asked to do some basic aggregation.

#### Exercise 7 - Using Various PySpark Functions
The [seventh exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-7) 
Taking a page out of the previous exercise, this one is focus on using a few of the
more common build in PySpark functions `pyspark.sql.functions` and applying their
usage to real-life problems.

#### Exercise 8 - Using DuckDB for Analytics and Transforms.
The [eighth exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-8) 
Using new tools is imperative to growing as a Data Engineer. DuckDB is one of those new tools. In this
exercise we will have to complete a number of analytical and transformation tasks using DuckDB. This
will require an understanding of the functions and documenation of DuckDB.

#### Exercise 9 - Using Polars lazy computation.
The [ninth exercise](https://github.com/DenysBosiak/data-engineering-practice/tree/master/Exercises/Exercise-9) 
Polars is a new Rust based tool with a wonderful Python package that has taken Data Engineering by
storm. It's better than Pandas because it has both SQL Context and supports Lazy evalutation 
for larger than memory data sets! It shows our Lazy skills!