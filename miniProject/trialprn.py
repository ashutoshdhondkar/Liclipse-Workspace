import MySQLdb

db=MySQLdb.connect('localhost','root','','ostl')
cur=db.cursor()

print("Enter prn :")

prn=input("")
sql="INSERT INTO moodle(PRN) VALUES('%s');"%(prn)
try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()

'''
prn='116A1018'
sql1="SELECT * FROM moodle WHERE PRN='%s'"%(prn)
try:
    cur.execute(sql1)
    result=cur.fetchall()
    print(result)
except:
    pass
print("Thank you")

'''