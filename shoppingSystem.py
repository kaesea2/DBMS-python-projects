#!/usr/bin/python3
#import libraries
import sqlite3 as sql 
import datetime as d
db = sql.connect('OrinocoMall.db')
cursor=db.cursor()#create a cursor handle
current_date=d.date.today().strftime('%Y-%m-%d')#get the current date and store it
#get the next id of a from the sqlite sequence table
def getID(gid):
    sql1="SELECT seq+1 FROM sqlite_sequence WHERE name=(?);"
    cursor.execute(sql1,(gid,))
    sqlRow=cursor.fetchone()
    return sqlRow[0]
#function to add row to the shopper basket and basket content table
def insertOrder(shop_id,p_id,s_id,qty,price):
    p_id = int(p_id)
    s_id = int(s_id)
    shop_id = int(shop_id)
    qty = int(qty)
    price = str(price)
    
    nextR_id=getID('shopper_baskets')
    current_date=d.date.today().strftime('%d-%m-%Y')
    sql2="INSERT INTO shopper_baskets (basket_id,shopper_id,basket_created_date_time) VALUES (?,?,?)"
    cursor.execute(sql2,(nextR_id,shop_id,current_date))

    sql3="INSERT INTO basket_contents (basket_id,product_id,seller_id,quantity,price) VALUES (?,?,?,?,?);"
    cursor.execute(sql3,(nextR_id,p_id,s_id,qty,price))
    print("\nItem Added To Your Basket!!!\n")
    db.commit()#commit the insert query to the database
#function to display options and return id of the selected option from an sql query   
def _display_options(all_options,title,string):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    for option in all_options:
        code = option[0]
        desc = option[1]
        print("{0}.\t{1}".format(option_num, desc))
        option_num = option_num + 1
        option_list.append(code)
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+string+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]
#function to display all delivery addresses stored from a query and return the address id for further use
def addr_options(all_options,title,word):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    print("{0}\t{1:30}{2:15}{3}".format("S/n","address_1","address_2","address_3"))
    for option in all_options:
        code = option[0]
        addr1 = option[1]
        addr2 = option[2]
        addr3 = option[3]
        print("{0}.\t{1:30}{2:15}{3}".format(option_num,addr1,addr2,addr3 ))
        option_num = option_num + 1
        option_list.append(code)
    if len (option_list) == 1 : #will check if the address is only one, if true, display and return the address id
        selected_option = 1
    else:
        selected_option = 0
        while selected_option > len(option_list) or selected_option == 0:
            prompt = "Enter the number against the "+word+" you want to choose: "
            selected_option = int(input(prompt))
    return option_list[selected_option - 1]
#function to add a delivery address to the delivery address table
def addAddr(address_id):
    addr1 = str(input("(**required)Enter Delivery Address 1 : "))
    addr2 = str(input("Enter Delivery Address 2 : "))
    addr3 = str(input("Enter Delivery Address 3 : "))
    country = str(input("(**required)Enter Delivery Country : "))
    post_code = str(input("(**required)Enter Delivery Post Code : "))
    
    sql2="INSERT INTO shopper_delivery_addresses \
            VALUES (?,?,?,?,?,?);"
    cursor.execute(sql2,(address_id,addr1,addr2,addr3,country,post_code))
    db.commit()
    print("\nAddress Added To Your Delivery Address!!!\n")
#function to display all orders made by a shopper
def retrieveContents(query,title):
    option_num = 1
    print("\n",title,"\n")
    print("{0:8} {1:10} {2:65} {3:17} {4:8} {5:5} {6:15}".format("order_id","order_date","description","seller_name","price","qty","status"))
    for o in query:
        order_id = o[0]
        order_date = o[1]
        description = o[2]
        seller_name = o[3]
        price = o[4]
        qty = o[5]
        status = o[6]
        print("{0:8} {1:10} {2:65} {3:17} {4:8} {5:5} {6:15}".format(order_id,order_date,description,seller_name,price,qty,status))
        option_num = option_num + 1
#function to display all basket contents
def basketDisplay(query,title):
    option_num = 1
    print("\n",title,"\n")
    print("{0:65} {1:20} {2:10} {3:5} {4:10}".format("description","seller_name","price","qty","totalPrice"))
    for b in query:
        description = b[0]
        seller_name = b[1]
        price = b[2]
        qty = b[3]
        total_price = b[4]
        print("{0:65} {1:20} {2:10} {3:5} {4:10}".format(description,seller_name,price,qty,total_price))
        option_num = option_num + 1 
#function to display all payment cards used by the shooper and return the payment id    
def payment_options(all_options,title,word):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    print("{0}\t{1:15}{2:16}".format("S/n","Card type","Card number"))
    for option in all_options:
        code = option[0]
        ctype = option[1]
        cnum = option[2]
        print("{0}.\t{1:15}{2:16}".format(option_num,ctype,cnum))
        option_num = option_num + 1
        option_list.append(code)
    if len (option_list) == 1 : #if payment card is found and its only one, this will automatically use it
        selected_option = 1
    else:
        selected_option = 0
        while selected_option > len(option_list) or selected_option == 0:
            prompt = "Enter the number against the "+word+" you want to choose: "
            selected_option = int(input(prompt))
    return option_list[selected_option - 1]
#function to add payment card to the payment card table
def addCard(payment_id):
    card_type = str(input("Enter Card Type : "))
    card_number = str(input("Enter Card Number : "))
    
    sql2="INSERT INTO shopper_payment_cards \
            VALUES (?,?,?);"
    cursor.execute(sql2,(payment_id,card_type,card_number))
    db.commit()
    print("\nPayment Card Added!!!\n")
#function to add all data in the shopper basket to the ordered product table and delete all data in the shopper basket and basket content
def insertShopOrder(o_id,shop_id):
    query="SELECT bc.quantity,bc.price,bc.product_id,bc.seller_id,bc.basket_id \
            FROM  basket_contents AS bc \
            INNER JOIN shopper_baskets AS sb ON sb.basket_id=bc.basket_id \
            WHERE sb.shopper_id=(?);"
    cursor.execute(query,(shop_id,))
    contents=cursor.fetchall()
    for i in contents:
        (qty,price,p_id,s_id,b_id)=i #to access the tuple
        
        query2="INSERT INTO ordered_products VALUES (?,?,?,?,?,?);"
        cursor.execute(query2,(o_id,p_id,s_id,qty,price,"Placed"))
        
        query3="DELETE FROM basket_contents WHERE basket_id=(?);"
        cursor.execute(query3,(b_id,))
        
        query4="DELETE FROM shopper_baskets WHERE basket_id=(?);"
        cursor.execute(query4,(b_id,))
        db.commit()
        
    print("\nCheckout Completed, Order PLaced!\n")
#function to add row to the shopper order table       
def placeOrder(shop_id,address_id,payment_id):
    o_id=getID("shopper_orders")
    query1="INSERT INTO shopper_orders VALUES (?,?,?,?,?,?);"
    cursor.execute(query1,(o_id,shop_id,address_id,payment_id,current_date,"Placed"))
    db.commit()
    insertShopOrder(o_id,shop_id)#calls the function to insert row to ordered product table and delete from basket
    return shop_id
    
sid=int(input("enter shopping id: "))#gets the shopper id 
try: 

    shop="SELECT shopper_id \
                    FROM shoppers \
                    WHERE shopper_id=(?); " 
    cursor.execute(shop,(sid,))
    shop_id=cursor.fetchone()[0]
    if shop_id: #checks if the shopper id exixts
        print("\n\t\t\t!!!WELCOME!!!\n")

        count = True;
        while count == True: #while loop to keep the menu running until shopper decides to exit
            print("\n\n\t ORINOCO - SHOPPER MAIN MENU\n\
    --------------------------------------------\n \
    1.Display Your Order History\n \
    2.Add An Item To Your Basket\n \
    3.View Your Basket\n \
    4.Checkout\n \
    5.Exit \n\n")
            choiceCount=True
            while choiceCount==True:
                try: #checks if the input is correct
                    answer=int(input("Enter : "))
                    choiceCount=False
                except:
                    print ("invalid input !!!")
                    continue;
            
            if answer < 1 or answer >5: #checks if the input is within the given range
                print ("invalid input !!!")
                continue;
            elif answer == 1:
                #retrieves all orders made by the shopper
                shop="SELECT so.order_id,strftime('%d-%m-%Y',so.order_date),p.product_description,se.seller_name,printf('€%.2f',op.price),op.quantity,so.order_status \
                        FROM shopper_orders AS so \
                        INNER JOIN ordered_products AS op ON so.order_id=op.order_id \
                        INNER JOIN products AS p ON op.product_id=p.product_id \
                        INNER JOIN sellers AS se ON op.seller_id=se.seller_id \
                        WHERE so.shopper_id = (?)\
                        ORDER BY so.order_date DESC;"
                cursor.execute(shop,(sid,))
                s_orders=cursor.fetchall()
                if s_orders:
                    retrieveContents(s_orders,"Shopper Orders") 
                else:
                    print ("No Orders Placed By This Custormer!!!")
                continue;
            elif answer == 2:
                porder=True
                while porder==True:
                    try:
                        query="SELECT category_id,category_description FROM categories GROUP BY category_code"
                        cursor.execute(query)
                        query_rows=cursor.fetchall()
                        cat_id = _display_options(query_rows,'CATEGORIES','product category') #gets the category id

                        query="SELECT product_id,product_description FROM products WHERE category_id=(?)"
                        cursor.execute(query,(cat_id,))
                        query_rows=cursor.fetchall()
                        p_id = _display_options(query_rows,'PRODUCTS','product') #gets the product id

                        query="SELECT ps.seller_id,se.seller_name ||' (' || printf('€%.2f',ps.price) ||')' AS name \
                                    FROM product_sellers AS ps\
                                    INNER JOIN sellers AS se ON ps.seller_id=se.seller_id \
                                    WHERE ps.product_id = (?)"
                        cursor.execute(query,(p_id,))
                        query_rows=cursor.fetchall()
                        s_id = _display_options(query_rows,'SELLERS','seller') #gets the seller id

                        qty=int(input("enter quantity needed : ")) #gets the quantity needed
                        porder=False
                    except:
                        print("invalid response")
                        continue;

                shop="SELECT ps.price FROM product_sellers AS ps \
                            INNER JOIN sellers AS se ON ps.seller_id=se.seller_id \
                            WHERE ps.product_id = (?) AND ps.seller_id=(?)"
                cursor.execute(shop,(p_id,s_id))
                price = cursor.fetchone()[0] #gets the price

                insertOrder(shop_id,p_id,s_id,qty,price) #passes all the data needed to the insertOrder function
                continue;

            elif answer == 3:
                query="SELECT p.product_description,se.seller_name,printf('€%.2f',bc.price) AS price,bc.quantity,printf('€%.2f',bc.price*bc.quantity) AS total_price \
                        FROM shopper_baskets AS sb \
                        LEFT JOIN basket_contents AS bc ON sb.basket_id=bc.basket_id \
                        LEFT JOIN products AS p ON bc.product_id=p.product_id \
                        LEFT JOIN sellers AS se ON bc.seller_id=se.seller_id \
                        WHERE sb.shopper_id = (?)"
                cursor.execute(query,(shop_id,))
                response=cursor.fetchall()
                if response: #checks if theres content in the basket before print out all data from the basket
                    query="SELECT printf('€%.2f',SUM(bc.price*bc.quantity)) AS basket_total \
                            FROM shopper_baskets AS sb \
                            LEFT JOIN basket_contents AS bc ON sb.basket_id=bc.basket_id \
                            LEFT JOIN products AS p ON bc.product_id=p.product_id \
                            LEFT JOIN sellers AS se ON bc.seller_id=se.seller_id \
                            WHERE sb.shopper_id =(?);"
                    cursor.execute(query,(shop_id,))
                    basket_sum=cursor.fetchone()[0] #gets the total price in the basket
                    basketDisplay(response,"Shopper Basket")
                    print("Basket Total : "+basket_sum)

                else:
                    print("No contents in your basket!!!")
                continue;

            elif answer == 4:
                query="SELECT p.product_description,se.seller_name,printf('€%.2f',bc.price) AS price,bc.quantity,printf('€%.2f',bc.price*bc.quantity) AS total_price \
                        FROM shopper_baskets AS sb \
                        LEFT JOIN basket_contents AS bc ON sb.basket_id=bc.basket_id \
                        LEFT JOIN products AS p ON bc.product_id=p.product_id \
                        LEFT JOIN sellers AS se ON bc.seller_id=se.seller_id \
                        WHERE sb.shopper_id = (?)"
                cursor.execute(query,(shop_id,))
                response=cursor.fetchall()
                if response: #checks if theres content in the basket before proceeding to checkout
                    query="SELECT sda.delivery_address_id,sda.delivery_address_line_1,sda.delivery_address_line_2,sda.delivery_address_line_3 \
                            FROM shopper_orders AS so \
                            INNER JOIN shopper_delivery_addresses AS sda ON so.delivery_address_id=sda.delivery_address_id \
                            WHERE so.shopper_id = (?)\
                            ORDER BY so.order_date DESC"
                    cursor.execute(query,(shop_id,))
                    address=cursor.fetchall()
                    if address:
                        add=True
                        while add==True:
                            try:
                                address_id = addr_options(address,'DELIVERY ADDRESSES','address') #gets the address id from the address function  
                                add=False;
                            except:
                                print("invalid response")
                                continue
                    else:
                        print("As You Have Not Yet Placed Any Orders, You Will Need To Enter A Delivery Address \n")
                        addrCount=True
                        while addrCount==True: #while loop to check and make sure all fields needed is given
                            try:
                                address_id=getID('shopper_delivery_addresses') #gets the next address id
                                addAddr(address_id) #calls the addAddr function to add a delivery address
                                addrCount=False;
                            except:
                                print("[!!!]An Error Occured! Please fill the required[**] fields")
                                continue;
                    query1="SELECT pc.payment_card_id,pc.card_type,pc.card_number\
                            FROM shopper_payment_cards AS pc \
                            INNER JOIN shopper_orders AS so ON pc.payment_card_id = so.payment_card_id\
                            WHERE so.shopper_id=(?) "
                    cursor.execute(query1,(shop_id,))
                    payment_card=cursor.fetchall()
                    if payment_card: #checks for previous payment card details
                        pcard=True
                        while pcard==True:
                            try:
                                payment_id=payment_options(payment_card,'PAYMENT CARD','payment card') #gets the payment id 
                                pcard=False
                            except:
                                print("invalid response")
                                continue;
                    else:
                        print("\n No Payment Card Found!!!\n")
                        print("As You Have Not Yet Placed Any Orders, You Will Need To Enter Your Payment Card Details \n")
                        card_count=True
                        while card_count==True: 
                            try:   
                                payment_id=getID('shopper_payment_cards') #gets the next payment id from the table
                                addCard(payment_id) #passes the payment id to the addCard function
                                
                                card_count=False;
                            except:
                                print("please check the card type.. must be ('Mastercard','Visa' or 'AMEX')")
                            continue;
                    placeOrder(shop_id,address_id,payment_id)
                else:
                    print("No contents in your basket!!!")
                continue;

            elif answer == 5:
                #exit the loop
                print("\nGOODBYE!!!")
                count = False;
except:
    print("no shopper with this ID")