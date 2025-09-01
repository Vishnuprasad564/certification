library = [(1,"Batman","Nolan",1999),
           (2,"Spiderman","Stanlee",2000),
           (3,"Superman","DC",2000)]
def search():
    id = int(input("Enter book id to search: "))
    for book in library:
        if book[0] == id:
            print("Book found: ",book)
            break
        else:
            print("Book not found")

def dispBook(year):
    count = 0
    for book in library:
        if book[3] == year:
            print(book)
            count+=1
    if count==0:
        print("No books")
