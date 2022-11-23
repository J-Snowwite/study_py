#python3

import os
import os.path
import sqlite3

def showSqlite():
    conn = sqlite3.connect("namelist.db") 
    db1 = conn.cursor()
    dbShow = "select * from namelist"
    showData = db1.execute(dbShow)
    for name in showData:
        print("filename is ",name[1])


def saveDB(nameList):
    conn = sqlite3.connect("namelist.db") 
    db1 = conn.cursor()
    dbCreate = "create table if not exists namelist (id integer primary key autoincrement,filename text)"
    db1.execute(dbCreate)
    conn.commit()
    for data in nameList:
        dbAdd = "insert into namelist(filename) values('%s')" % data
        db1.execute(dbAdd)
        conn.commit()
    db1.close()
    conn.close()

def getValue():
    Path1=r"D:\TestCodeFile"
    nameList = []
    for filename in os.listdir(Path1):
        nameList.append(filename)
    saveDB(nameList)

if __name__ == "__main__":
    getValue()
    showSqlite()