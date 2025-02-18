import random
conversation=[
    "Hi",
    "how are you"
]

print("Welcome to the chatbot")
print("Hello I'm a chatbot")

user=input()

response=random.choice(conversation)
print(response)