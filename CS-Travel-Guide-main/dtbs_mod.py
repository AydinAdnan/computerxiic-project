""""""

import os
import mysql.connector as mysql
import pwinput #pip install pwinput==1.0.1

def create_rev(fname, curso):  # Create Tables in Mysql from dump file
    fd = open(fname, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                curso.execute(command)
        except IOError as msg:
            print("Command skipped: ", msg)


def connectdb():              # Connect to Mysql
    usr = input("Enter Username: ")
    psw =pwinput.pwinput(prompt="Password:")
    con = mysql.connect(host='localhost', user=usr, passwd=psw)
    curs = con.cursor()
    create_dbase(curs)
    print("\nMySQL connection established ✅")
    return con


def create_dbase(curs):  # Creating database in Mysql
    curs.execute(
        "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'Review') AND (TABLE_NAME = 'Reviews')")
    c = curs.fetchone()[0]
    if c == 0:
        curs.execute("Create Database Review")
        curs.execute("Use Review")
        path = os.getcwd().replace('\\', '/') + "/review_reviews.sql"
        create_rev(path, curs)
    else:
        curs.execute("Use Review")
