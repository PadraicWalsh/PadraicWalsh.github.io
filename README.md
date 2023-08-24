# PadraicWalsh.github.io

# --Project-- In-Memory SQL Database with OpenAi API Integration
Welcome to my project focused on creating an in-memory SQL database using your computer's RAM and seamlessly integrating data from Pandas DataFrames. This project 
provides a solution for efficient data manipulation and analysis, leveraging the power of SQL queries in an in-memory environment.

# Project Goals
Creating a Temporary In-Memory Database: I developed a Python script that creates a temporary in-memory database within my own RAM. This database is designed to hold 
data for manipulation and analysis without the need for permanent storage.

Seamless Pandas Integration: You can easily push your Pandas DataFrames into the temporary in-memory database. This step ensures that data can be easily accessed and 
queried within the temporary database.

Efficient SQL Queries: One of the core functionalities of this project is the ability to perform SQL queries on the temporary in-memory database. Once the data is in 
the in-memory database, you'll have the capability to do this. I implemented a SQL querying mechanism that enables users to extract meaningful insights from the 
data stored in the database.

File-to-In-Memory Conversion: This project provides the ability to turn a file, possibly a CSV or Excel sheet, into an in-memory SQL database. This conversion 
process facilitates quick data access and reduces the need for constant file reading and parsing.

# How to Use
Clone this repository to your local machine.
Navigate to the project directory and run the necessary setup commands.
Import your data using Pandas DataFrames.
Use the provided functions to create the temporary in-memory SQL database and push your data into it.
Start executing SQL queries on the data using the integrated in-memory SQL capabilities.

#Technologies Used
Python
Pandas
Alchemy
OpenAi API
