import sys
import sqlite3
import optparse
import pandas
import getpass
import subprocess
from cmd import Cmd

# Create the database into your RAM memory
db_con = sqlite3.connect(":memory:")
# Create the cursor so that we can execute queries
CURSOR = db_con.cursor()
# Create the inventory table and the values for it
CURSOR.execute("CREATE TABLE inventory ('date_added', 'item_name', 'in_stock', 'description')")
values_for_inventory = [
    ('05/18/2017', 'cats', '1', 'meowth'),
    ('05/17/2017', 'dogs', '3', 'uno, dose, tres'),
    ('05/16/2017', 'hamsters', 'ALOT', 'to-many-to-count'),
    ('05/15/2017', 'ostrich', '2', 'weird-running-bird')
]
CURSOR.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", values_for_inventory)
# Commit the information into memory
db_con.commit()


class InvMangShell(Cmd):

    """ Inventory management interactive shell console """

    possible_shell_commands = {
        "create": "Create a new table in the built in database",
        "add": "Add columns to a table of your choice",
        "del": "Drop a table from the database",
        "show": "Show the entire database to see your changes",
        "shell-help": "Show the help menu"
    }

    def __create_sql_command(self, full, tablename, addable):
        """ Create a SQL command and return it """
        return full.format(tablename, ', '.join(map(lambda x: "'" + x + "'", addable)))

    def shell_help_menu(self):
        """ SQL-Shell help menu """
        print("Command:       Description:")
        for data in self.possible_shell_commands.keys():
            print("{}       {}".format(data, self.possible_shell_commands[data]))

    def do_show(self, tables):
        """
        Run this to show the table that you provide. You can use it
        to show all your changes made, decide what needs to be done,
        etc..

        :param tables: table name to show

        Example:

        z-perkins-thomas@sql-shell > show inventory
           date_added item_name in_stock         description
        0  05/18/2017      cats        1              meowth
        1  05/17/2017      dogs        3     uno, dose, tres
        2  05/16/2017  hamsters     ALOT    to-many-to-count
        3  05/15/2017   ostrich        2  weird-running-bird
        z-perkins-thomas@sql-shell >
        """
        print(pandas.read_sql_query("SELECT * FROM {}".format(tables), db_con))

    def do_add(self, table, full_sql_command="INSERT INTO {} VALUES ({})"):
        """
        Add a columns to a specified table, will display the changes
        after they are made

        :param table: table to add to

        Example:

        z-perkins-thomas@sql-shell > add inventory
        INSERT INTO inventory VALUES test test test test
           date_added item_name in_stock         description
        0  05/18/2017      cats        1              meowth
        1  05/17/2017      dogs        3     uno, dose, tres
        2  05/16/2017  hamsters     ALOT    to-many-to-count
        3  05/15/2017   ostrich        2  weird-running-bird
        4        test      test     test                test
        z-perkins-thomas@sql-shell >
        """
        add_command = raw_input("INSERT INTO {} VALUES ".format(table))
        CURSOR.execute(self.__create_sql_command(full_sql_command, table, add_command.split(" ")))
        self.do_show(table)

    def do_create(self, table, full_sql_command="CREATE TABLE {} ({})"):
        """
        Create a table in the database with a specified table name and
        parameters, will show changes after they have been made

        :param table: table name to add

        Example:

        z-perkins-thomas@sql-shell > create test
        CREATE TABLE test test1 test2 test3
        Empty DataFrame
        Columns: [test1, test2, test3]
        Index: []
        z-perkins-thomas@sql-shell >
        """
        add_command = raw_input("CREATE TABLE {} ".format(table))
        CURSOR.execute(self.__create_sql_command(full_sql_command, table, add_command.split(" ")))
        self.do_show(table)

    def do_del(self, table):
        """
        Delete a table from the database, will attempt to load the table,
        if it loads it wasn't deleted. If it doesn't load, it was deleted

        :param table: table to be deleted

        Example:

        z-perkins-thomas@sql-shell > del inventory
        Table: 'inventory' deleted successfully
        z-perkins-thomas@sql-shell > show inventory
        Traceback (most recent call last):
          ...

        """
        CURSOR.execute("DROP TABLE {}".format(table))
        try:
            self.do_show(table)
            print("Database table failed to delete..")
        except pandas.io.sql.DatabaseError:
            print("Table: '{}' deleted successfully".format(table))

    def _do_help(self):
        """ help menu """
        return self.shell_help_menu()


def help_menu():
    """ Help menu that makes everything bind together an look all pretty """
    print("""
This is a basic overview of a inventory management system.
It is capable of searching the database built into your memory
once this application starts to run. After each iteration the
database will be erased from the memory and built again when run.

NOTE: Please keep in mind that this is a CLI based example and
      does not have a graphical user interface, due to, well,
      just being an example. Hope you like it.

                      Help Menu:
                    --------------

Possible Options:         What They Do:
  -q/--query              This will search the in memory
                          database for a given query

  -a/--add                This will add to the table and
                          output your changes in the DB

  --all                   This will search the in memory
                          database for everything in the
                          inventory table

  --sql-shell             Launches and interactive SQL Shell
                          that allows you to create tables,
                          drop tables, and add tables

  -h/--help               This will output all the possible
                          flags and options with a short
                          description on their usage""")


def create_sql_query(command, table, args):
    """ Create a SQL query """
    return command.format(table, ', '.join(map(lambda x: "'" + x + "'", args)))


def show_changes(table, query="SELECT * FROM {}"):
    """ Show the changes of the table """
    return pandas.read_sql_query(query.format(table), db_con)


def _search_all_inventory():
    """ Search the entire inventory table """
    for stock in CURSOR.execute("SELECT * FROM inventory"):
        print("Inventory found: {}".format(stock))


def _find_certain(what):
    """ Find a specific query in the inventory """
    data_found = CURSOR.execute("SELECT %s FROM inventory" % what)
    for stock in data_found.fetchall():
        print("Found item: {}".format(stock))


def _add_to_inventory(data_tupe, table="inventory"):
    print("Creating columns...")
    CURSOR.execute("INSERT INTO {} VALUES (?, ?, ?, ?)".format(table), data_tupe)
    print(show_changes(table))


def _create_table(tablename, column_names, create_table_command="CREATE TABLE {} ({})"):
    """ Create a database table inside of the DB """
    print("Creating table, '{}'..".format(tablename))
    command = create_sql_query(create_table_command, tablename, column_names)
    CURSOR.execute(command)
    print(show_changes(tablename))


if __name__ == '__main__':

    parser = optparse.OptionParser(usage="invm.py -[a|h|q|c] [QUERY|COLS [NAMES]]")
    parser.add_option("-q", "--query", dest="searchQuery", metavar="QUERY",
                      help="Provide a query to search for a specific item (Example: -q cats)")
    parser.add_option("-a", "--add", dest="addToInventory", metavar="DATE, ITEM, AMOUNT, DESCRIPTION", nargs=4,
                      help="Add columns to the inventory table")
    parser.add_option("-c", "--create", dest="createATable", metavar="TABLE, PARAMS",
                      help="Create a table in the existing database")
    parser.add_option("--sql-shell", dest="sqlShell", action="store_true",
                      help="Launch the SQL shell so you can add information")
    parser.add_option("--all", dest="searchEntireInventory", action="store_true",
                      help="List all items in the inventory DB table")
    opt, _ = parser.parse_args()

    if len(sys.argv) <= 1:
        help_menu()
    else:
        if opt.searchQuery is not None:
            try:
                _find_certain(opt.searchQuery)
                exit(0)
            except sqlite3.OperationalError:
                print("Query '{}' is not a valid column in table 'inventory'".format(opt.searchQuery))
                print("Possible queries include anything in the above"
                      " listed database, things like 'cats', 'dogs' 'item_names'"
                      " 'stock', etc..")
        elif opt.searchEntireInventory is True:
            try:
                _search_all_inventory()
                exit(0)
            except Exception as e:
                print("Something went wrong and the application cannot continue: '{}'".format(e))
        elif opt.addToInventory is not None:
            if len(opt.addToInventory) == 4:
                _add_to_inventory(opt.addToInventory)
                exit(0)
        elif opt.sqlShell is True:
            prompt = InvMangShell()
            prompt.prompt = "{}@sql-shell > ".format(getpass.getuser())
            try:
                prompt.cmdloop("Launching SQL-Shell...")
            except Exception as e:
                print("Failed to run due to: '{}'".format(e))
                pass
        elif opt.createATable is not None:
            args = (opt.createATable.split(" ")[0], opt.createATable.split(" ")[1::])
            _create_table(args[0], args[1])
        else:
            print("You have failed to pass a valid flag, defaulting to help menu..")
            help_menu()

    q = raw_input("\nAre you done?[y/N] ")
    if q.lower().startswith("n"):
        subprocess.call("python invm.py --sql-shell")
    else:
        db_con.close()
