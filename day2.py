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

#3. Function with directory
def describe_person(person):
   print ("Name: " + person["name"])
   print ("City: " + person["city"])

vikram = {
   "name" : "Vikram",
   "city" : "Chennai",
   "role" : "Engineer"
}

describe_person(vikram)

#4. Loop through a list of dictionaries
employees = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]

for employee in employees:
    print("Name: " + employee["name"] + ", Age: " + str(employee["age"]) + ", City: " + employee["city"])

