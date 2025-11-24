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
#Remove a book from the collection using its Book ID.
if a=="F":
    Book_ID=int(input("Enter Product ID to remove: "))
    if dict1.pop(Book_ID):
        print("Book removed successfully.")
    else:
        print("Product not found.")
        print(dict1)
#_______________________________________________________________
#Clear the Entire Library Collection when needed.
elif a=="G":
    dict1.clear()
    print("Library Cleared.")
    print(dict1)
else:
    print("Invalid input or the current library might be empty, add some books.")
