# Data
We'll give examples of different ways to store data.
The reason for storing data is to combine multiple pieces of data and accumulate results.

## File plantext
It's readable, but it takes a lot of resources to assemble or retrieve data.
## File json
It's readable and well-structured. However, it can become problematic when the data starts to grow, and it is also resource intensive to combine and search.
## SQLite
FileDB is a popular choice because it is lightweight and provides database-like features. However, it is **application-dependent**, meaning it works best within specific use cases rather than as a general-purpose database.
## SQLAlchemy
Let's use Mysql as an example of a package for using an independent DB.