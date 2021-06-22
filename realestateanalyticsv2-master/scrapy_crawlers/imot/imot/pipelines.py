import mysql.connector


class ImotPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            database='Data',
            user='root',
            password='#cp3!043',
            charset='cp1251'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS imot_tb""")
        self.curr.execute("""CREATE TABLE imot_tb(
            id BIGINT AUTO_INCREMENT,
            location VARCHAR(255),
            one_bedroom_price VARCHAR(255),
            one_bedroom_price_for_one_meter VARCHAR(255),
            two_bedroom_price VARCHAR(255),
            two_bedroom_price_for_one_meter VARCHAR(255),
            three_bedroom_price VARCHAR(255),
            three_bedroom_price_for_one_meter VARCHAR(255),
            all_price_for_one_meter VARCHAR(255),
            PRIMARY KEY (id)
        )  ENGINE=InnoDB
        DEFAULT CHARSET=cp1251
        COLLATE=cp1251_general_ci;""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        sql = f"INSERT INTO imot_tb " \
              f"(`location`, `one_bedroom_price`, `one_bedroom_price_for_one_meter`, `two_bedroom_price`, " \
              f"`two_bedroom_price_for_one_meter`, `three_bedroom_price`, `three_bedroom_price_for_one_meter`, " \
              f"`all_price_for_one_meter`) " \
              f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"

        for index in range(len(item['location'])):
            self.curr.execute(sql, (item['location'][index], 
                                    item['one_bedroom_price'][index],
                                    item['one_bedroom_price_for_one_meter'][index],
                                    item['two_bedroom_price'][index],
                                    item['two_bedroom_price_for_one_meter'][index],
                                    item['three_bedroom_price'][index],
                                    item['three_bedroom_price_for_one_meter'][index],
                                    item['all_price_for_one_meter'][index]))

        self.conn.commit()
        self.conn.close()
