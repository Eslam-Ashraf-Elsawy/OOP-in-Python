class Member:

    def __init__(self,first_name,middle_name,last_name,gender):

        self.fname=first_name

        self.mname=middle_name

        self.lname=last_name

        self.gender=gender


    def get_full_name(self):

        return f"{self.fname} {self.mname} {self.lname}" 

    
    def name_with_title(self):

        if self.gender == "Male":
            return f"Hello Mr.{self.fname}"

        elif self.gender == "Female":
            return f"Hello Miss.{self.fname}"
        
        else:
            return f"Hello {self.fname}"


    def get_all_info(self):

        return f"{self.name_with_title()}, Your full name is: {self.get_full_name()}"

member_one = Member("Eslam","Ashraf","Elsawy","Male")
member_two = Member("Ahmed","Ali","Mahmoud","Male")
member_three = Member("Mona","Ali","Mahmoud","Female")
member_four = Member("Sara","Ali","Mahmoud","")

# print(dir(member_one))

# print(member_one.fname,member_one.mname,member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_one.get_full_name())
# print(member_one.name_with_title())

print(member_one.get_all_info())
