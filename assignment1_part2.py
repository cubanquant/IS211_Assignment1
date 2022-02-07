class Book:
    author = ''
    title = ''

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ", written by " + self.author)


obj1 = Book('John Steinbeck', 'Of Mice and Men')
obj2 = Book('Harper Lee', 'To Kill a Mockingbird')

obj1.display()
print()
obj2.display()