import os, sys, datetime
import MySQLdb as mdb
from os.path import join, getsize
from warnings import filterwarnings
filterwarnings('ignore', category = mdb.Warning)
 
hostname = ""
username = "user"
password = "pass"
database = "db"
table = "files"
directory = "/home/ftpdocs2/"
tempfile = "/root/temp.txt"
port = 3306
 
class MySQLTool:
    def __init__(self):
        pass
 
    def conn(self, hostname, username, password, database, port):
        try:
            conn = mdb.connect(host = hostname, user = username, \
                                passwd = password, db = database, local_infiles = 1)
            print("Connected to %s:%s" % (hostname, port))
        except mdb.Error:
                sys.exit("Error connecting to %s:%s" % (hostname, port))
        return conn
 
    def createDB(self, conn, table, directory, tempfile):
        counter = 0
        output = open(tempfile, "w")
        print("Generating %s table" % table)
 
        cur = conn.cursor()
 
        # Drop table
        cur.execute(""" DROP TABLE IF EXISTS %s""" % table)
 
        # Create table
        cur.execute("""CREATE TABLE IF NOT EXISTS \
                %s(Id INT PRIMARY KEY AUTO_INCREMENT, FILE_ROOT VARCHAR(200), \
                FILE_NAME VARCHAR(200), FILE_SIZE INT(20), FILE_DATE datetime);""" % table)
 
        # Generate a temporary file to bulk load into the RDBMS
        for root, dirs, files in os.walk(directory):
            for name in files:
                try:
                    size = getsize(join(root, name))
                    date = modification_date(join(root, name))
                    output.write(""";"%s";%s;%s;%s\n""" % (root, name, size, date))
                    counter += 1
                except os.error:
                    continue
        output.close()
 
        # Bulk load the temporary file into RDBMS
        cur.execute("""LOAD DATA LOCAL INFILE '%s' \
                    INTO TABLE %s FIELDS TERMINATED BY ';' ENCLOSED \
                    BY '"' """ % (tempfile, table))
        conn.commit()
 
        print("The %s table has %s rows" % (table, counter))
        os.remove(tempfile)
 
# Display the modified date for file
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
 
t = MySQLTool()
conn = t.conn(hostname, username, password, database, port)
t.createDB(conn, table, directory, tempfile)
