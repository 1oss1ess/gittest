import sqlite3


class Person:

    def __init__(self, id, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def name(self):
        return ("%s %s %s" % (self.id, self.first_name, self.last_name))

    @classmethod
    def getAll(self):
        conn = sqlite3.connect('userdb.db')
        conn.row_factory = self.dict_factory
        c = conn.cursor()
        query = '''SELECT id, first_name, last_name FROM user'''
        c.execute(query)
        users = c.fetchall()
        result = []
        for item in users:
            # print(item.keys())
            # import pdb
            # pdb.set_trace()
            person = Person(item['id'], item['first_name'], item['last_name'])
            result.append(person)
        conn.close()
        return result

    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
