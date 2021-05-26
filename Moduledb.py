import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)


def Getdata(Querydata,mydb):
    mycursor = mydb.cursor()
    mycursor.execute(Querydata)
    myresult = mycursor.fetchall()
    return myresult

def Updatedata(Querydata,mydb):
    mycursor = mydb.cursor()
    mycursor.execute(Querydata)
    mydb.commit()
    return mycursor.rowcount
