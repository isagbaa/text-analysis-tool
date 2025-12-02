#welcome message
def welcomeuser():
    print("\n welcome to my Okj text analysis tool.")
def inputusername():
    username = input("\n Enter your username: ")
    return username
def greeting(username):
    print("hello " + username + ", let's get started!")
#username message
welcomeuser()
print("Please enter your username:") 
#username input
username = inputusername()
#personalized greeting
greeting(username)