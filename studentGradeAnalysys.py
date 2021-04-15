#!/usr/bin/python3


import numpy as np
import sqlite3 as sq
import matplotlib.pyplot as pplot


#function to print the output
def DISPLAY():
    COUNT = False
    PLAY= db.execute("SELECT * FROM studentDetails ORDER BY NAME,NUMB,GRADE,COURSE") #gets all the info from the table and outputs it in an array
    #calls a for loop and print data to the output
    for D in PLAY:
        n = D[1]
        numb = D[2]
        c = D[3]
        g = D[4]
        print ("{}{} : {}{} : {}{} : {}{}".format("Name > ", n ,"Number > ", numb,"Code > ",c,"Grade > ", g,),"\n")    
        
    score_sum = db.execute("SELECT sum(GRADE) FROM studentDetails")#gets the sum of all grade from the table
    for t in score_sum:
        t=t[0]
        print ("Sum Of All Grades : ", t ,"\n")
        
    scoreAve = db.execute("SELECT avg(GRADE) FROM studentDetails") #gets the average of the total grade
    for avg in scoreAve:
        sAv = avg[0]
        print ("Grade Average : ", sAv, "\n")
        
    highest_grade = db.execute("SELECT max(GRADE) FROM studentDetails") #gets the highest grade score from the table 
    for hs in highest_grade: 
        h = hs[0]
        print ("High Scorer :  \n")
            
        hScore=db.execute('''SELECT * FROM studentDetails WHERE GRADE =?''',(h,)) #print the data of the persons who scored highest
        for hs in hScore:
            n = hs[1]
            numb = hs[2]
            c = hs[3]
            g = hs[4]
            print ("{}{} : {}{} : {}{} : {}{}".format("Name > ", n ,"Number > ", numb,"Code > ",c,"Grade > ", g,),"\n")
def keep():
    STORE = input("Print Output To File ? Enter 'y' for yes : ")
    if (STORE == 'y'):
        storeKeep = input("Name To Save As : ")
        
        sKeep = open(storeKeep+".txt", "w") #open functon to open and write to file
        sKeep.write("[^^^^^^^^^^] GRADING SYSTEM!!![^^^^^^^^^^] \n\n")
        dbKeep = db.execute("SELECT * FROM studentDetails ORDER BY NAME,NUMB,GRADE,COURSE")
        for kp in dbKeep:
            n = kp[1]
            numb=kp[2]
            c = kp[3]
            g = kp[4]
            
            sKeep.write("Name > "+str(n)+ "  :  "+"Number > "+str(numb)+ "  :  "+"Course > "+str(c)+ "  :  "+"Grade > "+str(g)+ "\n\n")
     
        score_sum = db.execute("SELECT sum(GRADE) FROM studentDetails") #grabs and save the total grade sum scored by students to the file
        for sSum in score_sum:
            sSum = sSum[0]
            
            sKeep.write("Sum Of All Grades > "+str(sSum) +"\n\n") 
           
        scoreAve = db.execute("SELECT avg(GRADE) FROM studentDetails") #grabs and save the average grade score of students to the file
        for sAv in scoreAve:
            sAv = sAv[0]
            sKeep.write ("Grade Average > "+ str(sAv) + "\n\n")
            
        highest_grade = db.execute("SELECT max(GRADE) FROM studentDetails") #gets the highest grade score from the table
        for h in highest_grade: 
            h = h[0]
            sKeep.write ("High Scorer : \n\n")
            highestScorer=db.execute('''SELECT * FROM studentDetails WHERE GRADE =?''',(h,))  #print the data of the persons who scored highest
            for hi in highestScorer:
                n = hi[1]
                numb = hi[2]
                c = hi[3]
                g = hi[4]
                
                sKeep.write ("Name > "+str(n)+ "  :  "+"Number > "+str(numb)+ "  :  "+"Course > "+str(c)+ "  :  "+"Grade > "+str(g)+ "\n\n")
                    
        sKeep.close()  #close the file document 
        print("Saved!!!")
    else :
        print("Bye!!!")
        pass;
def myplot():
    #empty array
    data=[]
    val =[]
    nam =[]
    myid =[]
    cc=0
    dbKeep = db.execute("SELECT * FROM studentDetails ORDER BY NAME,NUMB,GRADE,COURSE")
    for kp in dbKeep:
        i = int(kp[0])
        n = str(kp[1])
        numb=str(kp[2])
        c = str(kp[3])
        g = int(kp[4])
        #grab and pass values from the db to the empty array        
        mydata=[i,n,numb,c,g]
        data.append(mydata)
        val.append(data[cc][4])
        nam.append(data[cc][1])
        myid.append(data[cc][0])
        cc += 1

    pplot.figure(figsize=[15,8]) #plot size
    pplot.grid(axis='y', alpha=0.75) #grid lines in plot
    pplot.xlabel('Student Name',fontsize=15)
    pplot.ylabel('Student Grade',fontsize=15)
    pplot.xticks(fontsize=15)
    pplot.yticks(fontsize=15)
    pplot.ylabel('Grade',fontsize=15)
    pplot.title('Student Grade System',fontsize=15)
    for r in myid:
        
        pplot.bar(nam,val,align="center")
    sa=input("Want to save plot as image? enter 'y' : ") #option to save plot as png
    if sa=='y':
        s=input("enter image name : ")
        pplot.savefig(s+".png")
        print("plot saved as : "+s+".png")
        pplot.show()
        pass    
    else:
        print("plot not saved!!!")
        pplot.show()
        pass;

    
    

#welcome note!
print ("[..........] WELLCOME [..........] \n\n");

reload = input("Existing Database ?  Enter 'y' or 'n' : ")
if reload == "y":
    rName = str(input("Type DataBase Name with extention(.db) : "))
    try:
        #connecting to database
        db = sq.connect(rName)
        print(".....Successful.....\n")
    except:
        print(".....Check File Name..... ")
else:
    #creating a db if it dosent exist
    db = sq.connect('programDb.db')
    print(".....DB Started Successfully..... \n")

#create or overwrite table in the database
db.execute('''CREATE TABLE IF NOT EXISTS studentDetails (ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,NUMB TEXT NOT NULL,COURSE TEXT NOT NULL,GRADE INT NOT NULL);''')
    
    
COUNT = True
while (COUNT == True): #infinite loop
    
    N = str(input ("Enter Name Or Enter 'quit' Or 'print' : "))
    if N == 'quit':
        break;
    elif N == 'print':
        DISPLAY()
        myplot()
        keep()
        break;
    elif len(N) < 5 or len(N) > 20: #checks if the name is an alphabet
        print("Name must not be less than 5 alphabets or greater than 20 alphabets !!")
        continue
    elif not N.isalpha(): #name must be an alphabet
        print("Please Enter A Valid Name")
        continue
    try:
        sN = str(input("Enter Number : "))
    except SyntaxError: #checks for empty response
        print ("Invalid!!!")
    try:
        C = str(input("Enter Course : "))
    except SyntaxError:
        print ("Invalid!!! ")
    try:
        G = float(input ("Enter Grade : ")) #converts and controls the input to an integer float   
    except ValueError:
        print("Is Not A Float Number!!!")
        continue

    db.execute("INSERT INTO studentDetails (NAME,NUMB,COURSE,GRADE) VALUES (?,?,?,?)",(N,sN,C,G));
    db.commit()
    print("Stored!!! \n\n")
    
    #checks if theres more student to input their data
    check = input("More Inputs ? Enter 'y' or 'n' : \n")
    if check == 'y':
        #keeps the count TRUE
        COUNT = True
    else:
        DISPLAY();
        myplot();
        keep();