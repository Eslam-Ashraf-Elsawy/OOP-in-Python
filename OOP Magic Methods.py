

class Skill:

    def __init__(self):

        self.skills = ["Html","Css","Js"]

    def __str__(self):

        return f"This my Skills => {self.skills}"

    def __len__(self):

        return len(self.skills)    

profile = Skill()
print("#" * 50)
print(profile)
print("#" * 50)
print(len(profile))
print("#" * 50)

profile.skills.append("PHP")

profile.skills.append("MySQL")

print(len(profile))

# print("#" * 50)

# print(profile.__class__)

# print("#" * 50)

# my_string = "Eslam"
# print(type(my_string))

# print("#" * 50)

# print(my_string.__class__)

# print("#" * 50)

# print(dir(str))

# print("#" * 50)

# print(str.upper(my_string))

