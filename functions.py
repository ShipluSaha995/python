"""
def greet_user():
    print("Hi There!")
    print('Welcome Abroad!')

print("Start")
greet_user()
print('Finish\n\n')

#peremetters
print('After using perameters: ')
def user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome abroad')

first_name=input("Enter Your first Name: ")
last_name=input("Enter Your last Name: ")

print("start")
user(first_name, last_name)
print('finish\n')

user("Marry", "Copper")

#return in function

def square(number):
    return(number*number)

print(square(3))


"""

#recursive

def emoji_converter(message):
    if not message:
        return ""
    emojis={
        ":)":"😊",
        ":(":"😞"
    }

    current=emojis.get(message[0], message[0])
    return current+" "+emoji_converter(message[1:])

message=input("Enter ypur message: ").split(" ")
print(emoji_converter(message))
