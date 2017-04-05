# Tournament Tracker

## About
This project provides a tournament database and the interface functions needed to interact with the database.  This project is a part of Udacity's Front-End Developer Nanodegree program.

## To Run
To run this project on your own database server, you will need Vagrant and a virtual machine.  After downloading Vagrant and a VM (I used VirtualBox), follow the steps below to ensure your environment is set up correctly:

1. Go to this project's folder in your command prompt.

2. Enter `vagrant up` in your command prompt and press enter.  This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

3. Once this completes successfully, run `vagrant ssh` in the command prompt to connect to your virtual machine.  The folders in this project will be shared with your virtual machine.

4. Enter `cd /vagrant` to get to the project folder.

5. Enter `cd tournament` to enter the tournament folder where you will set up your tournament database.

6. To create the database tables from [tournament.sql](tournament/tournament.sql) enter the command `\i tournament.sql`

7. Now you can run the test program: `python tournament_test.py`

## To Edit
If you are adding functionality to the [tournament.py](tournament/tournament.py) file, please be sure to write test cases in [tournament_test.py](tournament/tournament_test.py) to thoroughly test the additions.

Some useful commands to know:
- `drop table table_name`: deletes the table named table_name.  If deleting all tables, you must delete the tables that reference other tables first. (Delete **matches** before deleting **players**).

- `\i tournament.sql`: re-initializes the tournament database based on the [tournament.sql](tournament/tournament.sql) file.


## Future Additions
* There is currently no front-end for this project.  This may be a future endeavor.

* This project currently only supports data from one tournament.  This may be a future endeavor, which will require table restructuring and additions.
