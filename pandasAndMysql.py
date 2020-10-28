import MySQLdb
import pandas as pd
try:
    conn=MySQLdb.connect(host="sql7.freemysqlhosting.net", user="sql7372220", passwd="3sgiPGyWad", db="sql7372220")
    df=pd.read_sql("SELECT * FROM produit", conn)
    print(df)
    conn.close()
except Exception as ex:
    print(ex)
