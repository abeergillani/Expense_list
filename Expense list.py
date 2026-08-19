import csv
expenses=[]
try:
    with open("expenses.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            expenses.append({
                "name":row[0],
                "amount":float(row[1])
                })
except FileNotFoundError:
    pass
while True:
    print ("\n==== EXPENSE TRACKER ====")
    print ("1. Add expense")
    print ("2. View expenses")
    print ("3. View total spendings")
    print ("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        name=input("Enter your expense name(or type 'done' to finish): ")
        if name.lower() == "done":
            continue
        amount=float(input("Enter the amount: "))
        expense={
            "name":name,
            "amount":amount
        }
        expenses.append(expense)
        with open("expenses.csv","a", newline="") as file: 
            writer=csv.writer(file)
            writer.writerow([name,amount])
            print ("Expenses added successfully")
            
    elif choice=="2":
        print ("\n==== Your Expenses ====")
        for expense in expenses:
            print (expense["name"], "-", expense["amount"])
    elif choice=="3":
        total=0
        for expense in expenses:
            total+= expense["amount"] 
            print ("Total spendings:", total)
    elif choice=="4":
         print ("Goodbye!")
         break
    else:
         print ("Invalid choice, please try again.")
    
