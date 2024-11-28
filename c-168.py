

class citizen:
      
      def __init__(self,name,age,dob,id_number):
                                                self.citizen_name= name
                                                self.citizen_age= age
                                                self.citizen_dob=dob
                                                self.citizen_id= id_number
                                                
      def add_citizen(self):
                            print("Name:"+ self.citizen_name)
                            print("age:"+ self.citizen_age)
                            print("dob:"+ self.citizen_dob)
                            print("ID. Number :"+ self.citizen_id)
                            
citizen1=   citizen("Amulya","11.9","20Th October 2010","2010-2010")
citizen1.add_citizen()
citizen2=   citizen("Atulya","17","3rd June 2005","0306-2005")
citizen2.add_citizen()

