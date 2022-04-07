import os
import sqlite3 as sql
from sqlite3 import Error
import csv
def generate_csv():
    try:
        conn = sql.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("select user_id, ad_id, review_rating from ads_adreview")
        with open('ratings.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + '/ratings.csv'
        print ("Data exported Successfully into {}".format(dirpath))

    except Error as e:
        print(e)
    
    finally:
        conn.close()