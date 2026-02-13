from random_username.generate import generate_username
#welcome message
def welcomeuser():
    print("\n welcome to my Okj text analysis tool.")
def getusername():
    maxattempts=3
    attempts=0

    while attempts < maxattempts:

        inputprompt = ""
        if attempts==0 :
           inputprompt = ("\n Enter your username:\n ")
        else :
           inputprompt = ("\n try again:\n ")
        usernamefrominput = input(inputprompt)
        
        #validate username
        if  len(usernamefrominput) < 5  or not usernamefrominput.isidentifier():  #if username is less than 5 characters or not a valid identifier
         print("Your Username must be at least 5 characters long,alphanumeric only, (A-Z/a-z/0-9) and have no space and cannot start with a number.")
        else :
            return usernamefrominput  #return valid username
        attempts += 1  #increment attempts
   
    
    print("\nExhuasted"+ str(maxattempts) +" attempts,Assigned username instead...." ) #display assigned username
    
    return generate_username()[0] #return generated username

    
      
    
    
def greeting(name):
    print("hello " + name + ", let's get started!")
\
#code starts here
 #displays welcome message check the function above
#print("Please enter your username:") #print message
#username input
# saves the resullt of getusername function to username variable
#personalized greeting


#get text from file
def getArticleText():
    f = open("files/article.txt", "r") #open the file in read mode
    rawtext =f.read() #print the content of the file
    f.close() #close the file
    return rawtext.replace("\n", " " ). replace("\r", " " ) #return the text with newlines replaced by spaces

welcomeuser()
username = getusername()
greeting(username)
articleTextraw = getArticleText() #get article text from function
print("GOT: ")
print(articleTextraw) #print the article text