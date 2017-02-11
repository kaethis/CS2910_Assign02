-----------------------------------------------------------------
          _          _                         _    __ ___ 
         /_\   _____(_)__ _ _ _  _ __  ___ _ _| |_ /  \_  )
        / _ \ (_-<_-< / _` | ' \| '  \/ -_) ' \  _| () / / 
       /_/ \_\/__/__/_\__, |_||_|_|_|_\___|_||_\__|\__/___|
                      |___/                                
-----------------------------------------------------------------

[AUTHOR]  Matt W. Martin, 4374851
          kaethis@tasmantis.net

[VERSION] 1.1

[PROJECT] CS2910, Assign02
          PSEUDO-SQL DBMS (PYTHON)

          A Python program for administrating a simple database
          using an SQL-like language.

          The program can load two types of files: comma-
          separated values (csv) and a proprietary format (db).

          Executing the program displays the menu showing the
          contents of the database.  Use the [UP] and [DOWN]
          arrow keys to navigate the menu.  Press the [ENTER] or
          [RET] key to input a command. 

          Commands are as follows:

          - 'CLOSE'  : Quits the program.

          - 'EXIT'   : See 'CLOSE'.

          - 'QUIT'   : See 'CLOSE'.

          - 'DELETE' : Deletes one or more records matching
                       requisite clause in the form:
                       'WHERE attrib==value'.

                       [Ex] 'DELETE WHERE ID==9901'

          - 'SELECT' : Selects attributes of one or more records
                       matching optional 'WHERE' clause (see
                       'DELETE').  If no attributes provided:
                       selects all attrs.  If no clause provided:
                       selects all records.

                       [Ex] 'SELECT'
                            'SELECT FNAME,LNAME'
                            'SELECT FNAME,LNAME WHERE ID==9901'

          - 'SHOW'   : See 'SELECT'

          - 'ADD'    : Takes a list of comma-separated values and
                       adds a record to the database.  Each value
                       represents an attribute described by the
                       schema, and therefore must comply with the
                       schema.

                       [Ex] 'ADD 9901,MATT,MARTIN'
                            (where schema is: [ID,4,NUM],
                                              [FNAME,10,ALPHA],
                                              [LNAME,15,ALPHA])

          When quitting the program, the user has to option to
          save.  Saving creates an instance of the database in
          the aforementioned proprietary format (db).   
      
[DATE]    11-Feb-2017

[ISSUED]  01-Feb-2017

[USAGE]   'python3 driver.py -csv filename.csv' OR
          'python3 driver.py -db filename.db'

[FILES]   ./README.txt
          ./driver.py
          ./dbmgr.py
          ./ui.py
          ./employees.csv
          ./courses.csv
          ./employees.db

[ISSUES]  - [1.1] NO ON-SCREEN MENU
            The program operates on the assumption that the user
            has read this README and has a full understanding of
            the commands listed and described above, but this is
            simply an unrealistic expectation.  I really ought to
            take the time to create a window somewhere inside the
            interface that tells the user what database commands
            are available within the program itself.  Until then,
            I'll stubbornly say to the user: RTFM!

          - [1.0] BROKEN MENU SIZING
            There's a bug in the size of the menu if the name of
            the attribute is less than the maximum length of that
            attr (in employees.csv, 'SELECT FNAME,ID' will yield
            this bug, where the value of 'ID' exceeds the size of
            the menu).  This only appears to happen if the menu
            contains more than just a single attribute.

            - [1.1] This issue has been fixed.

          - [1.0] NO ATTRIBUTE FILTER
            When selecting records, optional attributes provided
            can contain invalid attrs among valid ones.  For
            example, with employees.csv: 'SELECT ID,HELLO,FNAME'
            will yield the correct results for 'SELECT ID,FNAME'
            and ignore the invalid attribute.

            - [1.1] This issue has been fixed.

          - [1.0] SELECT NONEXISTING ATTRIBUTE (AMMEND)
            A glaring bug that went completely unnoticed occured
            when SELECTING with a WHERE clause when the attr did
            not correspond to any existing records; this caused
            the program to crash catastrophically.  To my chagrin
            I demonstrated this bug to Carlacci when showing-off 
            my program.  The following commands yielded this bug:

            1) 'DELETE WHERE DEPT==COMSCI'
               The menu shows 3 records that were deleted from
               the database with this command, as intended.
            2) 'SELECT WHERE DEPT==COMSCI'
               The program would crash, as no records exist with
               the DEPT attribute 'COMSCI'.  How awful.

            - [1.1] This issue has been fixed.
 
[REPO]    https://github.com/kaethis/CS2910_Assign02
