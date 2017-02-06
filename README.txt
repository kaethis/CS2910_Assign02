-----------------------------------------------------------------
          _          _                         _    __ ___ 
         /_\   _____(_)__ _ _ _  _ __  ___ _ _| |_ /  \_  )
        / _ \ (_-<_-< / _` | ' \| '  \/ -_) ' \  _| () / / 
       /_/ \_\/__/__/_\__, |_||_|_|_|_\___|_||_\__|\__/___|
                      |___/                                
-----------------------------------------------------------------

[AUTHOR]  Matt W. Martin, 4374851
          kaethis@tasmantis.net

[VERSION] 1.0

[PROJECT] CS2910, Assign02
          PSEUDO-SQL DBMS (PYTHON)

          A Python program for administering a simple database
          using an SQL-like language.

          The program can load two types of files: comma-
          separated values (csv) and a proprietary format (db).

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
      
[DATE]    06-Feb-2017

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

[ISSUES]  - BROKEN MENU SIZING
            There's a bug in the size of the menu if the name of
            the attribute is less than the maximum length of that
            attr (in employees.csv, 'SELECT FNAME,ID' will yield
            this bug, where the value of 'ID' exceeds the size of
            the menu).  This only appears to happen if the menu
            contains more than just a single attribute.

          - NO ATTRIBUTE FILTER
            When selecting records, optional attributes provided
            can contain invalid attrs among valid ones.  For
            example, with employees.csv: 'SELECT ID,HELLO,FNAME'
            will yield the correct results for 'SELECT ID,FNAME'
            and ignore the invalid attribute.
 
[REPO]    https://github.com/kaethis/CS2910_Assign02
