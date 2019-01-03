import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","ostl" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO moodle(PRN,
         FNAME,LNAME,USERNAME,BRANCH,PASSWORD)
         VALUES ('%s','%s','%s','%s','%s','%s')"""%('116','Shubham','Koks','Koks','CE','Bunty')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()