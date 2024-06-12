import mysql.connector as c
con=c.connect(host="localhost",user="root",password="mysql_dkhead69%@#",database="Hotel_Paradise")
cursor=con.cursor()
while True:
    print("------------------------------------------------")
    print("-----------------Hotel Paradise-----------------")
    print("------------------------------------------------")
    print("insert new entry = 1")
    print("update existing customer data = 2")
    print("delete existing data = 3")
    print("Show Particular Room Info = 4")
    print("End Task = 5")
    task= int(input("Enter your Task ->"))
    if task==5:
        break
    if task==2:
        alu=input("what do you want to change ?")
        if alu==('name'):
            aluun=int(input("Input the Room number to be updated ?"))
            aluuun=input("what is the new Name ?")
            queryyyy=("update customer_personal_info SET Name='{}' WHERE Room_Number={}").format(aluuun,aluun)
            cursor.execute(queryyyy) 

            con.commit()
            print("----------------------------")
            print("Data Updated Successfully")
            print("----------------------------")
        elif alu==('age'):
            aluua=int(input("Input the room number to be updated"))
            aluuua=int(input("What is the new age ?"))
            queryyyy=("update customer_personal_info SET Age={} WHERE Room_Number={}").format(aluuua,aluua)
            cursor.execute(queryyyy)            
            con.commit()
            print("----------------------------")
            print("Data Updated Successfully")
            print("----------------------------")

        elif alu==('room number'or'hotel price'or'food price'or'room price'or'service cost'or'total cost'):
            print ("Sorry these cannot be changed in existing data, please delete the previous entry and enter new one")

        elif alu==('address'):
            aluuad=int(input("Input the room number to be updated"))
            aluuuad=int(input("What is the new address ?"))
            queryyyy=("update customer_personal_info SET Address={} WHERE Room_Number={}").format(aluuuad,aluuad)
            cursor.execute(queryyyy)            
            con.commit()
            print("----------------------------")
            print("Data Updated Successfully")
            print("----------------------------")
        
            

    elif task==3:
        k=int(input("Enter The Room Number To be Deleted ->"))
        queryyyyy=("DELETE FROM customer_stay_info WHERE Room_Number={}").format(k)
        cursor.execute(queryyyyy)
        queryyy=("DELETE FROM customer_personal_info WHERE Room_Number={}").format(k)
        cursor.execute(queryyy)
        con.commit()
        print("----------------------------")
        print("Data Deleted Successfully")
        print("----------------------------")
        

    elif task==4:
        l=int(input("Enter The Room Number For Info ->"))
        queryyyy=("SELECT * FROM customer_personal_info WHERE Room_Number={}").format(l)
        
        cursor.execute(queryyyy)
        
        data=cursor.fetchone()
        import pandas as pd
        df=pd.DataFrame(data,index=('Name','Address','Room Number','Age','Arival','Booking','Departure'))
        print(df)
        
        
        print("----------------------------")
        print("Data Presented Successfully")
        print("----------------------------")
        
        

    elif task==1:
        n=input("Enter customer name----")
        a=input("Enter customer address----")
        r=int(input("Enter the room alloted----"))
        age=int(input("Enter the customer age----"))
        book=input("Enter booking date in YYYY/MM/DD format----")
        arrive=input("Enter arrival date in YYYY/MM/DD format----")
        depart=input("Enter departure date in YYYY/MM/DD format----")
        t=int(input("Enter which type of room you prefer Budget=1/Luxury=2/Delux=3----"))
        query="insert into customer_personal_info values('{}','{}',{},'{}','{}','{}','{}')".format(n,a,r,age,arrive,book,depart)
        cursor.execute(query)
        con.commit()
        print ("Data Inserted Sucessfully")

        days= int(input("Enter the No. of Nights you are Staying"))
     
        if (t==1):
            hotel_price= days*500 #Inclusive of all taxes
            food_price= days*200 #Inclusive of all taxes
            service_cost= days*0
              
        elif (t==2):
            hotel_price= days*800 #Inclusive of all taxes
            food_price= days*400 #Inclusive of all taxes
            service_cost= days*100
        
        elif (t==3):
            hotel_price= days*1300 #Inclusive of all taxes
            food_price= days*600 #Inclusive of all taxes
            service_cost= days*150
        
        Total_Amount= hotel_price+food_price+service_cost
        print ("Your Total Amount is", hotel_price+food_price+service_cost)#Inclusive of all taxes
        Total_Cost= hotel_price+food_price+service_cost
        import pandas as pd
        data=[{'Name':n,'Address':a,'Room Number':r,'age':age,'Room Cost':hotel_price,'Food Cost':food_price,'Service Cost':service_cost,'Total Amount':Total_Amount}]
        df=pd.DataFrame((data))
        query="insert into customer_stay_info values({},{},{},{},{},{})".format(r,days,hotel_price,food_price,service_cost,Total_Cost)
        cursor.execute(query)
        con.commit()
        print ("Data Inserted Sucessfully")
        print (df)
        print ("-----------------Hotel Paradise-----------------")
        
        
     
 
 
