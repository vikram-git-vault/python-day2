#1. Basic function to greet a person by name
def greet(name):
   return "Hello, " + name + "!"

result = greet("Vikram")
print(result)

#2. function with logic
def is_senior(age):
    if age >= 60:
        return "You are a senior citizen."
    else:
        return "You are not a senior citizen."
    
age = 45
result = is_senior(age)
print("Your age is " + str(age) + ". " + result)

age = 65
result = is_senior(age) 
print("Your age is " + str(age) + ". " + result)