class Book:
    def __init__(self,title,author,page):
        self.title = title
        self.author =author
        self.page = page
    def smmary(self):
        print(f"{self.title} by {self.author} , {self.page} page")
        
b1 = Book("The ant","Jim Gordon",191)
b1.smmary()
