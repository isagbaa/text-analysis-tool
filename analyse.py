from random_username.generate import generate_username
#welcome message
def welcomeuser():
    print("\n welcome to my Okj text analysis tool.")
def getusername():
    usernamefrominput = input("\n Enter your username:\n ")
    if  len(usernamefrominput) < 5  or not usernamefrominput.isidentifier():  #if username is less than 5 characters or not a valid identifier
        print("Your Username must be at least 5 characters long,alphanumeric only, (A-Z/a-z/0-9) and have no space and cannot start with a number.")
        usernamefrominput = generate_username()[0] #generate a username
        print("Assigned username instead...." ) #display assigned username
        return generate_username()[0] #return generated username
    return usernamefrominput
    
def greeting(name):
    print("hello " + name + ", let's get started!")
\
#code starts here
welcomeuser() #displays welcome message check the function above
print("Please enter your username:") #print message
#username input
username = getusername()# saves the resullt of getusername function to username variable
#personalized greeting
greeting(username)