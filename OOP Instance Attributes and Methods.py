class Member:

    def __init__(self,first_name,middle_name,last_name):

        self.fname=first_name

        self.mname=middle_name

        self.lname=last_name


member_one = Member("Eslam","Ashraf","Elsawy")
member_two = Member("Ahmed","Ali","Mahmoud")
member_three = Member("Ali","Ali","Mahmoud")

# print(dir(member_one))

print(member_one.fname,member_one.mname,member_one.lname)
print(member_two.fname)
print(member_three.fname)
