# Bigmack799 Roberto Mack

class Book:
    author = ""
    title = ""

    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    a = Book("Thorpe", "Beat the Dealer")

    b = Book("Walter Scott", "Ivanhoe")
    a.display()
    b.display()
    print("This is a assignment 1 part 2")
