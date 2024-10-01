import mysql
import mysql.connector
connection = mysql.connector.connect(host='localhost',database='python_lab', user='root', password='cdac123')
if connection.is_connected():
    cursor = connection.cursor()
    query = """select c.name, avg(sod.qtyordered) as Avg_Qty_Ordered
                from client_master c
                join sales_order so on c.clientno = so.clientno
                join sales_order_details sod on so.orderno = sod.orderno
                group by c.name
                having max(sod.qtyordered * sod.productrate) <= 15000;"""
    cursor.execute(query)
    record = cursor.fetchall()
    for row in record:
        print(f"{row[0]:<13} | {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()
