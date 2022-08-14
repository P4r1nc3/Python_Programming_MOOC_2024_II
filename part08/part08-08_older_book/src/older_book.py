# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year
        
def older_book(obj1 : Book, obj2 : Book):
    if obj1.year > obj2.year:
        print(f"{obj2.name} is older, it was published in {obj2.year}")
    elif obj1.year == obj2.year:
        print(f"{obj1.name} and {obj2.name} were published in {obj1.year}")
    else:
        print(f"{obj1.name} is older, it was published in {obj1.year}")

# -----------------------------
# Write your solution here
# -----------------------------
if __name__ == "__main__":

    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)