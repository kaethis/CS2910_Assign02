#!/usr/bin/env python3

import sys

import dbmgr

import ui


filename = ''

errors = { 'INVSYN' : 'INVALID SYNTAX!',
           'INVLEN' : 'INVALID LENGTH!',
           'INVTYP' : 'INVALID TYPECH!',
           'INVFRM' : 'INVALID FORMAT!',
           'NOREC'  : 'RECORD(S) NOT FOUND!',
           'NOATTR' : 'ATTRIBUTE(S) NOT FOUND!',
           'NOFILE' : 'FILE NOT FOUND!' }


def add(args):

    collect = []


    if len(args) == 1 and len(args[0].split(',')) == len(dbmgr.schema):

        args = args[0].split(',')


        rec = {}

        for i in range(len(dbmgr.schema)): rec[dbmgr.schema[i][0]] = args[i]


        for i in range(len(dbmgr.schema)):

            if not len(rec[dbmgr.schema[i][0]]) <= int(dbmgr.schema[i][1]):

                return 'INVLEN'


        for i in range(len(dbmgr.schema)):

            if not ui.regex[dbmgr.schema[i][2]].match(rec[dbmgr.schema[i][0]]):

                return 'INVTYP'

        
        collect.append(dbmgr.add(rec))

        return [dbmgr.schema, collect]

    else: return 'INVSYN' 


def delete(args):

    collect = []


    if len(args) == 2 and args[0] == 'WHERE':

        args = args[1].split('==')

        if len(args) == 2:

            if not dbmgr.search(args[0], args[1]) == -1:

                rec = dbmgr.delete(args[0], args[1])

                while not rec == -1:

                    collect.append(rec)

                    rec = dbmgr.delete(args[0], args[1])

                return [dbmgr.schema, collect]

            else: return 'NOREC'

        else: return 'INVSYN'

    else: return 'INVSYN'


def select(args):

    collect = []

    schema = []


    if len(args) == 0:

        for key in dbmgr.db.keys(): collect.append(dbmgr.db[key])

        return [dbmgr.schema, collect]

    elif len(args) == 2 and args[0] == 'WHERE':

        ret = delete(args)

        if not str(ret) in errors:

            for rec in ret[1]: dbmgr.add(rec)

            return [dbmgr.schema, ret[1]] 

    elif len(args) == 1:

        args = args[0].split(',')

        if not len(args) == 0:

            for i in range(len(args)):

                for j in range(len(dbmgr.schema)):

                    if args[i] == dbmgr.schema[j][0]: schema.append(dbmgr.schema[j])

            if len(schema) == 0: return 'NOATTR'


            for key in dbmgr.db.keys(): collect.append(dbmgr.db[key])

            return [schema, collect]

        else: return 'INVSYN'

    else:

        attrs = args[0].split(',')

        if not len(attrs) == 0:

            for i in range(len(attrs)):

                for j in range(len(dbmgr.schema)):

                    if attrs[i] == dbmgr.schema[j][0]: schema.append(dbmgr.schema[j])

            if len(schema) == 0: return 'NOATTR'


            ret = delete(args[1:])

            if not str(ret) in errors:

                for rec in ret[1]: dbmgr.add(rec)

                return [schema, ret[1]] 

            else:

                return ret # as error key.


def exit(args):

    global filename


    y, x = 1, 2

    msg = 'SAVE?'

    if ui.confirm(y, x, msg) == 0: dbmgr.savedb(filename)


    ui.exit()

    quit();


def main():

    cmds = { 'ADD'    : add,
             'DELETE' : delete,
             'SELECT' : select,
             'SHOW'   : select,
             'EXIT'   : exit,
             'QUIT'   : exit,
             'CLOSE'  : exit }

    args = []


    y, x = 1, 2

    height = 10

    ret = select(args)

    ret = ui.menuwin(y, x, height, 0, ret[0], ret[1])

    if ret == ui.keyboard['ESC']: exit(args)


    while True:

        y, x = 1, 2

        typech = 'VARCHAR'

        length = 50

        title = 'INPUT'

        buffer = ui.textwin(y, x, typech, length, title)


        if not buffer == ui.keyboard['ESC']:

            args = buffer.split(' ');

            if args[0] in cmds:

                ret = cmds[args[0]](args[1:])

                if str(ret) in errors:

                    y, x = 2, 3

                    ui.alert(y, x, errors[ret])

                else:

                    y, x = 1, 2

                    ret = ui.menuwin(y, x, height, 0, ret[0], ret[1])

                    if ret == ui.keyboard['ESC']: exit(args)
            else:

                y, x = 2, 3

                ui.alert(y, x, errors['INVSYN'])

        else:
        
            exit(args)

 
if __name__ == '__main__':

    if not len(sys.argv) == 3:

        ui.exit();

        print('[ERROR] '+errors['INVSYN']+'\n')

        print('[USAGE] \''+sys.argv[0]+' -csv '+'filename.csv\' OR')

        print('        \''+sys.argv[0]+' -db '+'filename.db\'\n')

        quit();

    if sys.argv[1] == '-csv':

        filename = sys.argv[2]

        if dbmgr.loadcsv(filename) == -1:

            ui.exit();

            print('[ERROR] \''+filename+'\' '+errors['NOFILE']+'\n');

            quit();

    elif sys.argv[1] == '-db':

        filename = sys.argv[2]

        if dbmgr.loaddb(filename) == -1:

            ui.exit();

            print('[ERROR] \''+filename+'\' '+errors['NOFILE']+'\n');

            quit();
    else:

        ui.exit();

        print('ERROR] '+errors['INVFRM']+'\n');

        quit();


    main();
