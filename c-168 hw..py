

class book:
      
      def __init__(self,name,author,price,dom,dop):
                                                self.book_name= name
                                                self.book_author= author
                                                self.book_price=price
                                                self.book_dom=dom
                                                self.book_dop=dop
                                                
      def add_book(self):
                            print("Book Name:"+ self.book_name)
                            print("Book Author:"+ self.book_author)
                            print("Book Price:"+ self.book_price)
                            print("Book was Published In :"+ self.book_dom)
                            print("This Book was published :"+ self.book_dop)
                            
citizen1=   book("Harry Potter","J.K. Rowling","1928","1997","25 years ago")
citizen1.add_book()
citizen2=   book("Diary Of a Wimpy Kid","Jeff Kenny","700","2017","5 years ago")
citizen2.add_book()

