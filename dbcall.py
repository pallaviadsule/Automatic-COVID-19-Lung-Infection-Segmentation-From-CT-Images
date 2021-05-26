import Moduledb

a=Moduledb.Updatedata("INSERT INTO customers(name,city,address) VALUES('RAJ','RAJ','RAJ')",Moduledb.mydb)
print(a)


myresult=Moduledb.Getdata("SELECT * FROM customers",Moduledb.mydb)
for x in myresult:
    print(x[0],",",x[1])
    

