class Human:
    
    apple_sum = 2

    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        self.apple = Human.apple_sum
        
    def introduce(self, friend):
        
        print("Hi, my name is ", self.name, " and I am ", self.age, " year old \nI have a friend called ", 
              friend.name, "and he(she) is ", friend.age, "years old")
        
    def give_apple(self, friend):
        
        print("I and my friend have ", Human.apple_sum, " apples. But, I gave my an apple to", friend.name)
        print("So I currently have ", self.apple_sum-1, "And ", friend.name, "has", friend.apple_sum+1, "apples")
        
    def action(self, friend):
        
        print("Choose your action towards", friend.name, "\n1. Introduce ", friend.name, "\n2. Give ", friend.name, "an apple\n3. Ask", friend.name," to introduce you \n4.", friend.name, "gives you an apple")
        
        act = input(" ")
        
        if act == str(1):
            user1.introduce(user2)
            
        elif act == str(2):
            user1.introduce(user2)
            
        elif act == str(3):
            user2.introduce(user1)
            
        elif act == str(4):
            user2.give_apple(user1)
            
        else:
            print("No action for the option no. ", act)    
            user1.action(user2)
        

your_name = input("What's your name? ")
your_age = input("How old are you? ")

friend_name = input("What's your friend's name? ")
friend_age = input("How old is he/she?: ")        
        
user1 = Human(your_name, your_age)
user2 = Human(friend_name, friend_age)


print(user1.action(user2))