# Example Inventory Management Framework

This is an example of an inventory management system that will give you the ability to add, create, delete, or edit database tables. It will not have a graphical user interface, due to being just an example.

### How it works

This will build a SQLite database in your system memory. It will be a small database because we don't want to eat up to much RAM, but it gets the point across. Keep in mind that this is a starting framework and is nowhere near finished
 
### Possible commands

You can do the following:

  - Add columns to the existing database tables
  - Query a table for certain information
  - Show the entire database
  - Launch a shell so you can go interactive
  
##### Help menu

 - To see the help menu you can pass the `-h/--help` flag and it will display all available commands
![help](https://cloud.githubusercontent.com/assets/14183473/26263930/5575dc92-3ca0-11e7-9b9a-80bdd229dac0.PNG)

##### Adding columns

 - To add columns to an existing database table you need to provide the `-a/--add` flag to the application. this flag requires four arguments and will add to the inventory table.
![add](https://cloud.githubusercontent.com/assets/14183473/26263927/54b3a0c8-3ca0-11e7-81e2-5a728fe6bb50.PNG)

##### Creating tables

 - To create a table an add it to the in memory database you can pass the `-c/--create` flag, this flag will require the table name and the columns to be extracted into the table in quotes
![creating](https://cloud.githubusercontent.com/assets/14183473/26263928/5500f346-3ca0-11e7-8ca5-960ed31b1b43.PNG)

##### Query for a specific item

 - To query for a specific item in a table you can pass the `-q/--query` flag, this will query the given table for a specified item and will make it so that you can find what you're looking for quickly and easily
![query](https://cloud.githubusercontent.com/assets/14183473/26263931/557887d0-3ca0-11e7-99c5-4a988b2c6e2e.PNG)

##### The interactive SQL-Shell

 - To launch an interactive shell you can pass the `sql--shell` flag, this will launch an interactive shell with it's own set of commands and will allow you to create tables, delete tables, add to tables, and display all the tables
![shell](https://cloud.githubusercontent.com/assets/14183473/26263932/5578ef40-3ca0-11e7-9bcf-dadaa7daafa7.PNG)

##### Future updates and more information

Updates that I would like to add to this:

 - A custom GUI for easier data storage (or a web application with an API)
 - Specific table creation information. edit the columns, etc..
 - All around more probable information