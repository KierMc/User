
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points, sep='\n')

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("You have insufficient points")
        self.gold_card_points = self.gold_card_points - amount


#User Instances
first_user = User("Kiernan", "McVay", "kier@gmail.com", 27)
second_user = User("Tom", "Brady", "TB12@yahoo.com", 45)
third_user = User("LeBron", "James", "LBJ@aol.com", 39)



first_user.enroll()
first_user.spend_points(50)
second_user.enroll()
second_user.spend_points(80)
first_user.display_info()
second_user.display_info()
third_user.display_info()
first_user.enroll()
third_user.spend_points(40)