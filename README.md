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

##### Installation and running instructions

 - First you will need to either download the zip/tarball [here](https://github.com/Ekultek/Inventory-Management-Framework/releases/tag/v0.1-beta)
 - Then you will need to extract that folder onto your desktop (EG: open the file and click extract to and choose desktop)
 - After this is done you will need to install Python, Mac OS, and Linux OS come pre-installed with python, so you shouldn't have to worry about that, but if you do click [here](https://www.python.org/ftp/python/2.7.12/python-2.7.12-macosx10.5.pkg)
 - Once you have installed python, you will need a terminal to run the application:
   * Go to your search menu   
![](http://blog.teamtreehouse.com/wp-content/uploads/2012/09/Screen-Shot-2012-09-25-at-12.57.00-PM.png)
   * Type in `terminal` or find the black box with the white `>_`
   * Wherever you have placed the file you will need to `cd` into that directory, for instance lets assume that your file is under `~/home/projects/Inventory-Management-Framework` you will need to type `cd ~/home/projects/Inventory-Management-Framework`
 - After you have changed into that directory, you will need to run this command: `pip install -r requirements.txt`. (*NOTE*: if this does not work, run this command: `easy_install pandas`)
 - Once those packages have been installed, you will need to run the following command: `python invm.py --help`. This will display the help menu and show you a general idea of how to use the system. If you would like you can run: `python invm.py --sql-shell` to launch the shell and run `help add`.

Here is a general idea on Linux of how to run this program:
[![instructions](https://cloud.githubusercontent.com/assets/14183473/26268816/c03cd5c4-3cb6-11e7-919b-13539837d313.PNG)](https://vimeo.com/218228182)

##### Future updates and more information

Updates that I would like to add to this:

 - A custom GUI for easier data storage (or a web application with an API)
 - Specific table creation information. edit the columns, etc..
 - All around more probable information