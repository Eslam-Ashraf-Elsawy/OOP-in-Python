class Member:

    not_allowed_names = ["shit", "hell", "Baloot"]

    users_num = 0

    @classmethod
    def show_users_count(cls):

        print(f"We have {cls.users_num} users in our system")

    @staticmethod
    def say_hello():

        print("Hello from static method")

    def __init__(self,first_name,middle_name,last_name,gender):

        self.fname=first_name

        self.mname=middle_name

        self.lname=last_name

        self.gender=gender

        Member.users_num += 1


    def get_full_name(self):
        if self.fname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")

        if self.mname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        
        if self.lname in Member.not_allowed_names:
            raise ValueError("Name Not Allowed")
        
        else:
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


    def delete_user(self):

        Member.users_num -= 1

        return f"User {self.fname} is Deleted."

print(Member.users_num)

member_one = Member("Eslam","Ashraf","Elsawy","Male")
member_two = Member("Ahmed","Ali","Mahmoud","Male")
member_three = Member("Mona","Ali","Mahmoud","Female")
member_four = Member("shit","Ali","Mahmoud","")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

print("#"* 50)


Member.show_users_count()

print("#"* 50)

print(member_one.get_full_name())
print(Member.get_full_name(member_one))

print("#"* 50)

Member.say_hello()

print("#" * 50)



# print(dir(member_one))

# print(member_one.fname,member_one.mname,member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_one.get_full_name())
# print(member_one.name_with_title())

# print(dir(Member))

# print(member_one.get_all_info())
