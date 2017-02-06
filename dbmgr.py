import pickle


schema = []

db = {}


def loaddb(filename):

    global schema

    global db


    filename = filename.split('.')[0]

    filename += '.db'


    try:

        with open(filename, 'rb') as file:

            schema, db = pickle.load(file)

    except FileNotFoundError:

        return -1


def savedb(filename):

    global schema 

    global db


    filename = filename.split('.')[0]

    filename += '.db'


    data = [ schema, db ]


    with open(filename, 'wb') as file:

        pickle.dump(data, file)


def loadcsv(filename):

    global schema

    global db


    try:

        with open(filename, 'r') as file:

            attribs = file.readline().rstrip().split(',')

            lengths = file.readline().rstrip().split(',')

            typechs = file.readline().rstrip().split(',')


            for i in range(len(attribs)):

                schema.append([ attribs[i], lengths[i], typechs[i] ])


            for line in file:

                line = line.rstrip()

                if line:

                    tup = line.split(',')

                    rec = dict()


                    for i in range(len(schema)): rec[schema[i][0]] = tup[i]

                    db[rec[schema[0][0]]] = rec


    except FileNotFoundError:

        return -1


def savecsv(filename):

    global schema 

    global db


    filename = filename.split('.')[0]

    filename += '.csv'


    data = ''


    for i in range(len(schema[0])):

        for j in range(len(schema)): data += schema[j][i] + ','

        data = data[:-1] + '\n'


    for rec in db:

        for i in range(len(schema)): data += db[rec][schema[i][0]] + ','

        data = data[:-1] + '\n'


    with open(filename, 'w') as file:

        file.write(data)


def search(attrib, value):

    global db


    for rec in db:

        if attrib in db[rec]:

            if value == db[rec][attrib]: return rec

        else:

            return -1


    return -1 


def delete(attrib, value):

    global db


    return db.pop(search(attrib, value), -1)

            
def add(rec):

    global db


    db[rec[schema[0][0]]] = rec


    return rec
