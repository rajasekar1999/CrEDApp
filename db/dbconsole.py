import sqlite3

conn = sqlite3.connect('content.db')

conn.execute('''CREATE TABLE CONTENT
         (TITLE TEXT    NOT NULL,
         CONTENT  TEXT    NOT NULL,
         CITATION  TEXT    NOT NULL);''')


# conn.execute('''Drop table CONTENT''')
conn.commit()

# # print("Schedule table created successfully")

# # title = 'Classically Unorthodox'

# # content = 'Eleventh Perspective'

# # citation = 'eleventhperspective.wordpress.com'

# # conn.execute('''DELETE FROM CONTENT''')

# cursor = conn.execute("SELECT * from CONTENT")

# tit = ['Hey','Poda','Aandavane Namma Pakkam Irukkaan']

# conn.execute(f"UPDATE CONTENT SET CONTENT = '{ tit[1] }', CITATION = '{ tit[2] }' where TITLE = '{ tit[0] }'")
# conn.commit()

# if cursor == None:
#     print('The table is empty')
# else:
#     for row in cursor:
#         print("TITLE = ", row[0])
#         print()
#         print("CONTENT = ", row[1])
#         print()
#         print("CITATION = ", row[2])
#         print()

# conn.commit()

# # conn = sqlite3.connect(con)
# # tit = 'Hey'
# # cursor = conn.execute(f"SELECT TITLE,CONTENT,CITATION from CONTENT WHERE TITLE = 'Hey Hey'")
# # print(list(cursor))
