'''
show databases
show tables
use database-name
create database database-name

drop database database-name
create table product (name varchar(20) primary key, price float, qty int)
describe product
drop table product # to delete the whole table

insert into product values ('Prod1', 34.56, 23)
select * from product
select * from product where qty > 20
delete from product where qty=0
update product set price=price*1.25 where name='Prod3'

commit

This user can connect remotely from any computer of the domain epfl.ch (except the local machine!) 
to the database epfl:

CREATE USER 'student'@'%.epfl.ch' IDENTIFIED BY 'Siccours02' 
GRANT ALL ON epfl.* to 'student'@'%.epfl.ch'

This user can connect from the local computer to the database epfl:

CREATE USER 'student'@'localhost' IDENTIFIED BY 'Siccours02'
GRANT ALL ON epfl.* to 'student'@'localhost'

1) Connect to the database engine (mysql)
2) Create a cursor 
3) Create and execute SQL statements (using the cursor)
4) If needed you may process the result of the SQL statement
5) Loop to step 3 or close the cursor and the connection

6 optional) Take care of the use of a transaction: if a transaction is in use you should 
commit it or roll it back

'''

import MySQLdb # the module mysqlclient

try:
    # Step 1: connection
    conn=MySQLdb.connect(host="sql7.freemysqlhosting.net", user="sql7372220", passwd="3sgiPGyWad", db="sql7372220")
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    cursor.execute("insert into produit values ('prod200', 22.3, 34)")
    print(f"{cursor.rowcount} rows were returned")
    cursor.execute("insert into produit values ('prod300', 22.3, 34)")
    print(f"{cursor.rowcount} rows were returned") 
    cursor.execute("commit")
    
    cursor.execute("select * from produit")
       
    while True:
        row = cursor.fetchone()
        if row == None:
            break
#         print("{}, {}, {}".format(row[0], row[1], row[2]))
        print(f"{row[0]}, {row[1]}, {row[2]}")
#     res=cursor.fetchall()    
#     print(res)
    print("{} rows were returned".format(cursor.rowcount))
      
    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)

