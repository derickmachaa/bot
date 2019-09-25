import sqlite3

conn=""
cursor=""


def connect():
    global conn,cursor
    conn=sqlite3.connect("./data/bot.db")
    cursor=conn.cursor()


def create_table():
    create_table = "CREATE TABLE IF NOT EXISTS bot (id INTEGER PRIMARY KEY AUTOINCREMENT , host TEXT UNIQUE,port number, username TEXT,password TEXT,pkey TEXT,session number)"
    cursor.execute(create_table)


def insert_with_password(address,port,username,password):
    insert="INSERT OR IGNORE INTO bot(host,port,username,password,session) VALUES(\'%s\',%s,\'%s\',\'%s\',1)" % (address,port,username,password)
    cursor.execute(insert)
    conn.commit()
    
    
def insert_with_key(address,port,username,pkey):
    insert="INSERT OR IGNORE INTO bot(host,port,username,pkey,session) VALUES(\'%s\',%s,\'%s\',\'%s\',1)" % (address,port,username,pkey)
    cursor.execute(insert)
    conn.commit()
    
def update_db(host,session):
    update="UPDATE bot SET session=%s WHERE host=\'%s\'" % (session,host)
    cursor.execute(update)
    conn.commit()
    
def get_online():
    sql="SELECT * FROM bot WHERE session=1"
    bots=cursor.execute(sql).fetchall()
    return bots
    
def get_ip():
    sql="SELECT host FROM bot"
    ipaddress=cursor.execute(sql).fetchall()
    return ipaddress

def get_host(ip):
    sql="SELECT * FROM bot WHERE host=\'%s\'"%ip 
    details=cursor.execute(sql).fetchone()
    return details

def get_all():
    sql="SELECT * FROM bot"
    bots=cursor.execute(sql).fetchall()
    return bots

def close():
    conn.close()
