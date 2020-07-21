class User:
    user_id = 1
    def __init__(self, name: str = ""):
        self.name = name
        self.id = User.user_id
        User.user_id += 1


users = [User() for _ in range (10)]


for user in users:
    print(user.id)


# for idx, user in enumerate(users):
#     if user.id == 5:
#         del users[idx]
#
# for user in users:
#     print(user.id)

