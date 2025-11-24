a=str(input("Enter A if you want to add a new book to the collection. " 
            "\nEnter B if you want to Check Book Availability using its Book ID. "
            "\nEnter C if you want to List All Books with their details. "
            "\nEnter D if you want to Retrieve a Book’s Author using its Book ID. "
            "\nEnter E if you want to Update the number of available copies when a book is issued or returned. "
            "\nEnter F if you want to Remove a book from the collection using its Book ID. "
            "\nEnter G if you want to Clear the Entire Library Collection when needed. "))
#_______________________________________________________________
#Add a new book to the collection.
dict1={
    101: {"Title":"The Maze Runner", "Author":"James Dashner", "Available copies":50}
}
if a=="A":
    Book_ID=int(input("Enter the ID of the new book: "))
    Title=input("Enter the title of the new book: ")
    Author=input("Enter the name of the author of the book: ")
    Available_copies=int(input("Enter the no. of copies available: "))
    dict1[Book_ID]={"Title":Title, "Author": Author, "Available copies":Available_copies}
    print("The updates collection is: ",dict1)
#_______________________________________________________________
#Check Book Availability using its Book ID.
elif a=="B":
    Book_ID=int(input("Enter the Book ID: "))
    if Book_ID in dict1:
        print("The book is available.")
    else:
        print("The book is not available.")
#_______________________________________________________________
#List All Books with their details.
elif a=="C":
    for Book_ID, details in dict1.items():
        print(Book_ID, ":", details)