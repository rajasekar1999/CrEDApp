import sqlite3
from flask import Flask, render_template, request, url_for

con="content.db"

def ListContent(form):
    conn = sqlite3.connect(con)
    conn.execute(f"INSERT INTO CONTENT (TITLE,CONTENT,CITATION) VALUES ('{form[0]}','{form[1]}','{form[2]}')")
    conn.commit()
    return 'Content Listed'

def getList():
    conn = sqlite3.connect(con)
    cursor = conn.execute(f"SELECT TITLE from CONTENT")
    lis = list()
    for row in cursor:
        lis.append(row)
    return lis

def FetchEdit(tit):
    conn = sqlite3.connect(con)
    cursor = conn.execute(f"SELECT TITLE,CONTENT,CITATION from CONTENT WHERE TITLE == '{ tit }'")
    cursor = list(cursor)
    lis = [cursor[0][0],cursor[0][1],cursor[0][2]]
    print(lis)
    return lis

def UpdateContent(tit):
    conn = sqlite3.connect(con)
    conn.execute(f"UPDATE CONTENT SET CONTENT = '{ tit[1] }',CITATION = '{ tit[2] }' where TITLE = '{ tit[0] }'")
    conn.commit()
    return 'Content Updated'

def DeleteContent(tit):
    conn = sqlite3.connect(con)
    conn.execute(f"DELETE from CONTENT where TITLE = '{ tit }'")
    conn.commit()
    return 'Content Updated'

def FetchArticle(tit):
    conn = sqlite3.connect(con)
    cursor = conn.execute(f"SELECT TITLE,CONTENT,CITATION from CONTENT WHERE TITLE == '{ tit }'")
    cursor = list(cursor)
    lis = [cursor[0][0],cursor[0][1],cursor[0][2]]
    print(lis)
    return lis

def DeleteAll():
    conn = sqlite3.connect(con)
    conn.execute(f"DELETE FROM CONTENT")
    conn.commit()