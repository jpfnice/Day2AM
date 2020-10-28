
import MySQLdb # the module mysqlclient

try:
    # Step 1: establish a connection and create a cursor at the same time using the with statement:
    with MySQLdb.connect(host="localhost", user="user1", passwd="Siccours02", db="epfl") as cursor:
        
        # Step 2: using the cursor, execute SQL statements:
        cursor.execute("insert into produit values ('prod200', 22.3, 34)")
        print(f"{cursor.rowcount} rows were returned")
        cursor.execute("commit")
        
        cursor.execute("select * from product")
          
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print("{}, {}, {}".format(row[0], row[1], row[2]))
    #     res=cursor.fetchall()    
    #     print(res)
        print("{} rows were returned".format(cursor.rowcount))
              
    
except Exception as ex:
    print(ex)

