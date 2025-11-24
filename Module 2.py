a=str(input("Enter A if you want to add a new book to the collection. " 
            "\nEnter B if you want to Check Book Availability using its Book ID. "
            "\nEnter C if you want to List All Books with their details. "
            "\nEnter D if you want to Retrieve a Book’s Author using its Book ID. "
            "\nEnter E if you want to Update the number of available copies when a book is issued or returned. "
            "\nEnter F if you want to Remove a book from the collection using its Book ID. "
            "\nEnter G if you want to Clear the Entire Library Collection when needed. "))
dict1={
    101: {"Title":"The Maze Runner", "Author":"James Dashner", "Available copies":50}
}
#_______________________________________________________________
#Retrieve a Book’s Author using its Book ID.
if a=="D":
    Book_ID=int(input("Enter the Book ID: "))
    if Book_ID in dict1:
        print("Author is: ",dict1[Book_ID]["Author"])
    else:
        print("Book ID not found.")
#_______________________________________________________________
#Update the number of available copies when a book is issued or returned.
elif a=="E":
    Book_ID=int(input("Enter Product ID: "))
    if Book_ID in dict1:
        print("1. Increase Stock")
        print("2. Decrease Stock")
    choice=int(input("Enter choice: "))
    qty=int(input("Enter quantity: "))
    if choice==1:
        dict1[Book_ID]["Available copies"]+=qty
        print("Updated data:", dict1[Book_ID]["Available copies"])
    elif choice==2:
        dict1[Book_ID]["Available copies"]-=qty
        print("Updated data:", dict1[Book_ID]["Available copies"])
    else:
        print("Invalid Choice.")