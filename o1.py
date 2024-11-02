class LibraryItem:

  def __init__(self,title,author,publication_year,item_id):
    self.title=title
    self.author=author
    self.publication_year=publication_year
    self.item_id=item_id

  def welcome(self):
    print("Welcome to the LMS System")

  def displayInfo(self):
    return (f"The title of the book is : {self.title} \n.The author is : {self.author}\n.The publication year is : {self.publication_year}\n.The item id is : {self.item_id}")
  
class Book(LibraryItem):
  def __init__(self,title,author,publication_year,item_id,genre):
    super().__init__(title,author,publication_year,item_id)
    self.genre=genre

  def displayInfo(self):
    base_info=super().displayInfo()
    return(f"{base_info}\n.The genre of the book is : {self.genre}")
  

class Magazines(LibraryItem):

  def __init__(self,title,author,publication_year,item_id,issu_number):
    super().__init__(title,author,publication_year,item_id)
    self.issu_number=issu_number

  def displayInfo(self):
    base_info=super().displayInfo()
    return(f"{base_info}\n. The issue date is : {self.issu_number}")
  
# l1=LibraryItem("Atomic Habits","James Clear",2018,"a17869")
# l1.welcome()
# print(l1.displayInfo())

b1=Book("Atomic Habits","James Clear",2018,"a17869","Motivational")
# print(b1.displayInfo())

m1=Magazines("Madani Guldasta","Dawateislami",2017,"a6758jk8","ak2017")
print(m1.displayInfo())

